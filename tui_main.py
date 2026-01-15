import asyncio
import logging
from logging.handlers import RotatingFileHandler
import signal
import sys
import threading
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Button, Label, DataTable
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.binding import Binding
from textual import work

import core.utils.settings as settings
from core.network.network_utils import NetworkUtils
from core.server.server import Server
from core.adapters import (
    register_default_adapters,
)
from core.adapters.dota2.rcon_client import SourceRCONClient

# Register available game adapters
register_default_adapters()

# OpenArena server (used when game_type is openarena)
server = Server()

# Dota 2 RCON client (used when game_type is dota2)
rcon_client: SourceRCONClient | None = None
rcon_connected = False

async_loop = None
async_thread = None
cleanup_done = False
game_type = settings.game_type

def cleanup():
    global cleanup_done, rcon_client, rcon_connected
    if cleanup_done:
        return
    cleanup_done = True

    logging.info("Starting cleanup...")

    if game_type == "dota2":
        # Disconnect RCON
        if rcon_client and rcon_connected:
            try:
                if async_loop and async_loop.is_running():
                    future = asyncio.run_coroutine_threadsafe(
                        rcon_client.disconnect(), async_loop
                    )
                    future.result(timeout=5)
            except Exception as e:
                logging.warning(f"RCON disconnect error: {e}")
            rcon_connected = False
    else:
        # OpenArena cleanup
        server.dispose()

    if getattr(settings, 'enable_latency_control', False):
        try:
            NetworkUtils.dispose(settings.interface)
        except Exception as e:
            logging.warning(f"Network cleanup skipped: {e}")

    if async_loop and async_loop.is_running():
        async_loop.call_soon_threadsafe(async_loop.stop)

    logging.info("Cleanup completed")

def run_async_loop():
    global async_loop
    async_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(async_loop)
    server.set_async_loop(async_loop)
    async_loop.run_forever()


class TUILogHandler(logging.Handler):
    def __init__(self, log_widget):
        super().__init__()
        self.log_widget = log_widget

    def emit(self, record):
        try:
            msg = self.format(record)
            self.log_widget.write_line(msg)
        except Exception as e:
            print(f"TUI log error: {e}", file=sys.stderr)

class QuitConfirmScreen(ModalScreen[bool]):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Shutdown server and exit?"),
            Horizontal(
                Button("Yes", variant="error", id="yes"),
                Button("Cancel", variant="default", id="cancel"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")

class AdminApp(App):
    CSS_PATH = "tui_main.tcss"
    BINDINGS = [Binding("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        # Show different controls based on game type
        is_dota2 = game_type == "dota2"
        game_label = f"Game: {game_type.upper()}"

        # Different button labels for Dota 2
        start_label = "Connect RCON" if is_dota2 else "Start Server"
        stop_label = "Disconnect" if is_dota2 else "Kill Server"

        yield Vertical(
            Horizontal(
                Label(game_label, id="game-type-label"),
                Input(placeholder="Enter command...", id="input"),
                Label("State: Disconnected" if is_dota2 else "State: Warmup", id="status-state"),
                Label("" if is_dota2 else "Round: 0/5", id="status-round"),
                # Only show bot controls for OpenArena
                Button("Add Bot", id="add-bot-btn", variant="primary", disabled=is_dota2),
                Button("Remove All Bot", id="remove-bot-btn", variant="default", disabled=is_dota2),
                id="top-panel",
            ),
            Horizontal(
                Vertical(
                    Horizontal(
                        Button(start_label, id="start-server-btn", variant="success"),
                        Button(stop_label, id="kill-server-btn", variant="error"),
                        id="server-control-buttons",
                    ),
                    DataTable(id="user-table"),
                    id="left-panel",
                ),
                Vertical(Log(id="app-log"), Log(id="server-log"), id="right-panel"),
                id="content-panel",
            ),
            id="main-container",
        )

    @work(thread=True)
    def run_server_worker(self):
        """Run server process in background thread using Textual Worker."""
        logging.info("Server worker starting...")
        server.start_server()
        logging.info("Server process started, entering message loop...")
        server.run_server_loop()

    @work(thread=True)
    def connect_rcon_worker(self):
        """Connect to Dota 2 server via RCON in background thread."""
        global rcon_client, rcon_connected

        logging.info(f"Connecting to RCON at {settings.dota2_rcon_host}:{settings.dota2_rcon_port}...")

        rcon_client = SourceRCONClient(
            host=settings.dota2_rcon_host,
            port=settings.dota2_rcon_port,
            password=settings.dota2_rcon_password,
            timeout=10.0,
        )

        # Run async connect in the async loop
        async def do_connect():
            global rcon_connected
            try:
                await rcon_client.connect()
                rcon_connected = True
                logging.info("RCON connected successfully!")

                # Get initial status
                status = await rcon_client.execute("status")
                self.call_from_thread(self._update_server_log, f"Connected!\n{status}")
                self.call_from_thread(self._update_connection_state, True)

            except Exception as e:
                logging.error(f"RCON connection failed: {e}")
                rcon_connected = False
                self.call_from_thread(self._update_connection_state, False)

        if async_loop and async_loop.is_running():
            future = asyncio.run_coroutine_threadsafe(do_connect(), async_loop)
            try:
                future.result(timeout=15)
            except Exception as e:
                logging.error(f"RCON connect error: {e}")

    def _update_server_log(self, message: str):
        """Update server log from worker thread."""
        try:
            server_log = self.query_one("#server-log", Log)
            for line in message.split('\n'):
                server_log.write_line(line)
        except Exception:
            pass

    def _update_connection_state(self, connected: bool):
        """Update UI to reflect connection state."""
        try:
            state_label = self.query_one("#status-state", Label)
            start_btn = self.query_one("#start-server-btn", Button)

            if connected:
                state_label.update("State: Connected")
                start_btn.disabled = True
            else:
                state_label.update("State: Disconnected")
                start_btn.disabled = False
        except Exception:
            pass

    def on_mount(self) -> None:
        global async_thread

        app_log = self.query_one("#app-log", Log)
        server_log = self.query_one("#server-log", Log)

        app_log.border_title = "App Logs"
        server_log.border_title = "Server Output"

        input_widget = self.query_one("#input", Input)
        input_widget.border_title = "Command Input"

        user_table = self.query_one("#user-table", DataTable)
        user_table.border_title = "Connected Users"
        user_table.cursor_type = "row"
        user_table.add_columns("ID", "Name", "OBS", "Action")

        handler = TUILogHandler(app_log)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)

        server.set_output_handler(lambda msg: server_log.write_line(msg))

        self.update_status_display()

        async_thread = threading.Thread(target=run_async_loop, daemon=True)
        async_thread.start()

        self.setup_periodic_updates()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        input_id = message.input.id
        value = message.value.strip()

        if not value:
            return

        if input_id == "input":
            if value.lower() in ['quit', 'exit']:
                self.action_quit()
            else:
                if game_type == "dota2":
                    self.send_rcon_command(value)
                else:
                    server.send_command(value)
                message.input.value = ""

    def send_rcon_command(self, command: str):
        """Send command via RCON and display response."""
        logging.info(f"send_rcon_command called with: {command}")
        logging.info(f"rcon_connected={rcon_connected}, rcon_client={rcon_client is not None}")

        if not rcon_connected or not rcon_client:
            logging.warning("RCON not connected - cannot send command")
            return

        if not async_loop or not async_loop.is_running():
            logging.warning("Async loop not running - cannot send command")
            return

        logging.info(f"Scheduling RCON command: {command}")

        async def do_command():
            try:
                logging.info(f"Executing RCON command: {command}")
                response = await rcon_client.execute(command)
                logging.info(f"RCON response received: {response[:100] if response else '(empty)'}...")
                # Use call_from_thread for thread-safe UI update
                self.call_from_thread(self._update_server_log, f"> {command}\n{response}")
            except Exception as e:
                logging.error(f"RCON command error: {e}", exc_info=True)

        future = asyncio.run_coroutine_threadsafe(do_command(), async_loop)
        logging.info(f"Command scheduled, future: {future}")

    def action_quit(self) -> None:
        def check_quit(confirmed: bool | None) -> None:
            if confirmed:
                cleanup()
                self.exit()

        self.push_screen(QuitConfirmScreen(), check_quit)

    def update_status_display(self):
        try:
            state_label = self.query_one("#status-state", Label)
            round_label = self.query_one("#status-round", Label)

            current_state = "Warmup"
            current_round = 0
            max_rounds = 0

            if hasattr(server, 'game_state_manager') and server.game_state_manager:
                current_state = server.game_state_manager.get_current_state().name
                current_round = server.game_state_manager.round_count
                max_rounds = server.game_state_manager.max_rounds

            state_label.update(f"State: {current_state}")
            round_label.update(f"Round: {current_round}/{max_rounds}")
        except Exception as e:
            logging.error(f"Error updating status display: {e}")

    def update_user_table(self):
        try:
            user_table = self.query_one("#user-table", DataTable)
            user_table.clear()

            if hasattr(server, 'network_manager') and server.network_manager:
                network_mgr = server.network_manager

                for client_id, client_type in network_mgr.client_type_map.items():
                    name = network_mgr.client_name_map.get(client_id, f"Client_{client_id}")

                    if client_type == "BOT":
                        obs_status = "N/A"
                    else:
                        client_ip = network_mgr.client_ip_map.get(client_id)
                        obs_status = "✓" if (client_ip and hasattr(server, 'obs_connection_manager')
                                           and server.obs_connection_manager.is_client_connected(client_ip)) else "✗"

                    user_table.add_row(str(client_id), name, obs_status, "Kick")
        except Exception as e:
            logging.error(f"Error updating user table: {e}")

    def update_start_button(self):
        try:
            start_btn = self.query_one("#start-server-btn", Button)
            start_btn.disabled = server.is_running()
        except Exception as e:
            logging.error(f"Error updating start button: {e}")

    def setup_periodic_updates(self):
        def periodic_update():
            if not cleanup_done:
                self.update_status_display()
                self.update_user_table()
                self.update_start_button()
                timer = threading.Timer(2.0, periodic_update)
                timer.daemon = True
                timer.start()

        timer = threading.Timer(2.0, periodic_update)
        timer.daemon = True
        timer.start()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-bot-btn":
            bot_names = ["Angelyss", "Arachna", "Major", "Sarge", "Skelebot", "Merman", "Beret", "Kyonshi"]
            import random
            bot_name = random.choice(bot_names)
            difficulty = settings.bot_difficulty
            server.send_command(f"addbot {bot_name} {difficulty}")
            logging.info(f"Bot addition requested: {bot_name} (difficulty {difficulty})")

        elif event.button.id == "remove-bot-btn":
            server.send_command("kick allbots")
            logging.info("All bots removal requested")

        elif event.button.id == "start-server-btn":
            if game_type == "dota2":
                # Connect via RCON
                self.connect_rcon_worker()
            else:
                # Start OpenArena server
                self.run_server_worker()
                self.update_start_button()

        elif event.button.id == "kill-server-btn":
            if game_type == "dota2":
                # Disconnect RCON
                self.disconnect_rcon()
            else:
                server.send_command("killserver")
                logging.info("Kill server command sent")

    def disconnect_rcon(self):
        """Disconnect from RCON server."""
        global rcon_connected

        if not rcon_client:
            return

        async def do_disconnect():
            global rcon_connected
            try:
                await rcon_client.disconnect()
                rcon_connected = False
                logging.info("RCON disconnected")
                self.call_from_thread(self._update_connection_state, False)
            except Exception as e:
                logging.error(f"RCON disconnect error: {e}")

        if async_loop and async_loop.is_running():
            asyncio.run_coroutine_threadsafe(do_disconnect(), async_loop)

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        if event.data_table.id == "user-table":
            try:
                user_table = self.query_one("#user-table", DataTable)
                row_data = user_table.get_row(event.row_key)
                client_id = int(row_data[0])
                user_name = row_data[1]

                logging.info(f"Kicking user: {user_name} (ID: {client_id})")
                server.kick_client(client_id)
            except Exception as e:
                logging.error(f"Error kicking user: {e}")

def signal_handler(sig, frame):
    cleanup()
    sys.exit(0)

def main():
    file_handler = RotatingFileHandler(
        "tui_app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logging.getLogger().addHandler(file_handler)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    app = AdminApp()
    app.run()

if __name__ == "__main__":
    main()