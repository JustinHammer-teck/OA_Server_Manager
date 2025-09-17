import os
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
from textual.message import Message

import core.utils.settings as settings
from core.network.network_utils import NetworkUtils
from core.server.server import Server

server = Server()
async_loop = None
interface = settings.interface
async_thread = None
server_thread = None
cleanup_done = False
tui_app = None

def cleanup():
    global cleanup_done
    if cleanup_done:
        return
    cleanup_done = True

    logging.info("Starting cleanup...")

    try:
        server.dispose()
    except Exception as e:
        logging.error(f"Error disposing server: {e}")

    if async_loop and async_loop.is_running():
        try:
            future = asyncio.run_coroutine_threadsafe(
                server.cleanup_obs_async(), async_loop
            )
            future.result(timeout=2)
        except Exception as e:
            logging.error(f"Error cleaning up OBS: {e}")

    try:
        NetworkUtils.dispose(interface)
    except Exception as e:
        logging.error(f"Error cleaning up network: {e}")

    if async_loop and async_loop.is_running():
        try:
            async_loop.call_soon_threadsafe(async_loop.stop)
        except Exception as e:
            logging.error(f"Error stopping async loop: {e}")

    if async_thread and async_thread.is_alive():
        try:
            async_thread.join(timeout=2)
            if async_thread.is_alive():
                logging.warning("Async thread did not finish within timeout")
        except Exception as e:
            logging.error(f"Error joining async thread: {e}")

    if server_thread and server_thread.is_alive():
        try:
            server_thread.join(timeout=2)
            if server_thread.is_alive():
                logging.warning("Server thread did not finish within timeout")
        except Exception as e:
            logging.error(f"Error joining server thread: {e}")

    logging.info("Cleanup completed")

def run_async_loop():
    global async_loop
    async_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(async_loop)
    server.set_async_loop(async_loop)

    try:
        async_loop.run_forever()
    except Exception as e:
        logging.error(f"Async loop error: {e}")
    finally:
        async_loop.close()

def run_server_thread():
    try:
        server.start_server()
        server.run_server_loop()
    except Exception as e:
        logging.error(f"Server thread error: {e}")
        cleanup()

class TUILogHandler(logging.Handler):
    def __init__(self, log_widget):
        super().__init__()
        self.log_widget = log_widget

    def emit(self, record):
        try:
            msg = self.format(record)
            self.log_widget.write_line(msg)
        except Exception as e:
            print(f"TUI log handler error: {e}", file=sys.stderr)

class QuitRequest(Message):
    """Message to request quit action."""
    pass

class ShutdownConfirmScreen(ModalScreen[bool]):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Shutdown Background Processes?", id="confirm-label"),
            Label("This will stop the server and async processes.", id="warning-label"),
            Horizontal(
                Button("Yes, Shutdown", variant="error", id="shutdown-btn"),
                Button("Cancel", variant="default", id="cancel-btn"),
                id="button-container"
            ),
            id="shutdown-dialog"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "shutdown-btn")

class ExitConfirmScreen(ModalScreen[bool]):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Processes Shutdown Complete", id="status-label"),
            Label("You can now safely exit the application.", id="info-label"),
            Button("Exit App", variant="success", id="exit-btn"),
            id="exit-dialog"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(True)

class AdminApp(App):
    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Log(id="log")
        yield Input(placeholder="Admin command...", id="input")

    def on_mount(self) -> None:
        global async_thread, server_thread

        log_widget = self.query_one("#log", Log)
        handler = TUILogHandler(log_widget)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.DEBUG)

        try:
            async_thread = threading.Thread(target=run_async_loop, daemon=True)
            async_thread.start()

            time.sleep(0.2)

            server_thread = threading.Thread(target=run_server_thread, name="ServerThread")
            server_thread.start()
        except Exception as e:
            logging.error(f"Error starting threads: {e}")

    def on_input_submitted(self, message: Input.Submitted) -> None:
        command = message.value.strip()
        if command:
            if command.lower() in ['quit', 'exit']:
                self.action_quit()
            else:
                try:
                    server.send_command(command)
                    self.query_one("#input", Input).value = ""
                except Exception as e:
                    logging.error(f"Error sending command '{command}': {e}")

    def action_quit(self) -> None:
        def check_shutdown(shutdown: bool | None) -> None:
            if shutdown:
                cleanup()
                def check_exit(exit_confirmed: bool | None) -> None:
                    if exit_confirmed:
                        self.exit()
                self.push_screen(ExitConfirmScreen(), check_exit)

        self.push_screen(ShutdownConfirmScreen(), check_shutdown)

    def on_quit_request(self, message: QuitRequest) -> None:
        """Handle quit request from signal handler."""
        self.action_quit()

def signal_handler(sig, frame):
    global tui_app
    if tui_app and tui_app.is_running:
        try:
            # Post quit request message to the TUI
            tui_app.post_message(QuitRequest())
            return
        except Exception as e:
            logging.error(f"Error posting quit request: {e}")

    # Fallback to immediate cleanup if TUI is not running
    cleanup()
    sys.exit(0)

def main():
    global tui_app
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)

    app = AdminApp()
    tui_app = app
    app.run()

if __name__ == "__main__":
    main()