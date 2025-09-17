import os
import asyncio
import logging
import signal
import sys
import threading
import time
from textual.app import App, ComposeResult
from textual.widgets import Input, Log
from textual.binding import Binding

import core.utils.settings as settings
from core.network.network_utils import NetworkUtils
from core.server.server import Server

server = Server()
async_loop = None
interface = settings.interface

def cleanup():
    if async_loop and async_loop.is_running():
        try:
            future = asyncio.run_coroutine_threadsafe(
                server.cleanup_obs_async(), async_loop
            )
            future.result(timeout=5)
        except Exception as e:
            pass

    try:
        NetworkUtils.dispose(interface)
    except Exception as e:
        pass

    server.dispose()

    if async_loop and async_loop.is_running():
        async_loop.call_soon_threadsafe(async_loop.stop)

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
        except:
            pass

class AdminApp(App):
    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Log(id="log")
        yield Input(placeholder="Admin command...", id="input")

    def on_mount(self) -> None:
        log_widget = self.query_one("#log", Log)
        handler = TUILogHandler(log_widget)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.DEBUG)

        async_thread = threading.Thread(target=run_async_loop, daemon=True)
        async_thread.start()

        time.sleep(0.2)

        server_thread = threading.Thread(target=run_server_thread, name="ServerThread")
        server_thread.start()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        command = message.value.strip()
        if command:
            if command.lower() in ['quit', 'exit']:
                cleanup()
                self.exit()
            else:
                server.send_command(command)
                self.query_one("#input", Input).value = ""

    def action_quit(self) -> None:
        cleanup()
        self.exit()

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