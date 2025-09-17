import asyncio
import logging
import signal
import sys
import threading
import time
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Button, Label
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
    BINDINGS = [Binding("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Log(id="app-log"),
            Log(id="server-log"),
            id="log-panel"
        )
        yield Input(placeholder="Admin command...", id="input")

    def on_mount(self) -> None:
        global async_thread, server_thread

        app_log = self.query_one("#app-log", Log)
        server_log = self.query_one("#server-log", Log)

        app_log.border_title = "App Logs"
        server_log.border_title = "Server Output"

        # Setup app logging
        handler = TUILogHandler(app_log)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.DEBUG)

        # Setup server output handler
        server.set_output_handler(lambda msg: server_log.write_line(msg))

        async_thread = threading.Thread(target=run_async_loop, daemon=True)
        async_thread.start()

        time.sleep(0.2)

        server_thread = threading.Thread(target=run_server_thread, daemon=True)
        server_thread.start()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        command = message.value.strip()
        if command:
            if command.lower() in ['quit', 'exit']:
                self.action_quit()
            else:
                server.send_command(command)
                self.query_one("#input", Input).value = ""

    def action_quit(self) -> None:
        def check_quit(confirmed: bool | None) -> None:
            if confirmed:
                cleanup()
                self.exit()

        self.push_screen(QuitConfirmScreen(), check_quit)

def signal_handler(sig, frame):
    cleanup()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    app = AdminApp()
    app.run()

if __name__ == "__main__":
    main()