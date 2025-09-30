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

import core.utils.settings as settings
from core.network.network_utils import NetworkUtils
from core.server.server import Server

server = Server()
async_loop = None
async_thread = None
server_thread = None
cleanup_done = False

def cleanup():
    global cleanup_done
    if cleanup_done:
        return
    cleanup_done = True

    logging.info("Starting cleanup...")

    server.dispose()
    NetworkUtils.dispose(settings.interface)

    if async_loop and async_loop.is_running():
        async_loop.call_soon_threadsafe(async_loop.stop)

    logging.info("Cleanup completed")

def run_async_loop():
    global async_loop
    async_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(async_loop)
    server.set_async_loop(async_loop)
    async_loop.run_forever()

def run_server_thread():
    server.start_server()
    server.run_server_loop()

def start_server_process():
    global server_thread

    logging.info("Starting server process...")

    server_thread = threading.Thread(target=run_server_thread, daemon=True)
    server_thread.start()

    logging.info("Server process started")

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
        yield Vertical(
            Horizontal(
                Input(placeholder="Enter command...", id="input"),
                Label("State: Warmup", id="status-state"),
                Label("Round: 0/5", id="status-round"),
                Button("Add Bot", id="add-bot-btn", variant="primary"),
                Button("Remove All Bot", id="remove-bot-btn", variant="default"),
                id="top-panel",
            ),
            Horizontal(
                Vertical(
                    Horizontal(
                        Button("Start Server", id="start-server-btn", variant="success"),
                        Button("Kill Server", id="kill-server-btn", variant="error"),
                    ),
                    DataTable(id="user-table"),
                ),
                Vertical(Log(id="app-log"), Log(id="server-log"), id="right-panel"),
                id="content-panel",
            ),
            id="main-container",
        )

    def on_mount(self) -> None:
        global async_thread, server_thread

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
                server.send_command(value)
                message.input.value = ""

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
            max_rounds = 5

            if hasattr(server, 'game_state_manager') and server.game_state_manager:
                current_state = server.game_state_manager.get_current_state().name

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
            is_running = server._process and server._process.poll() is None
            start_btn.disabled = is_running
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
            start_server_process()
            self.update_start_button()

        elif event.button.id == "kill-server-btn":
            server.send_command("killserver")
            logging.info("Kill server command sent")

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