import asyncio
import random
import time
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Button, Label, DataTable
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.binding import Binding

class MockServer:
    def __init__(self):
        self.output_handler = None
        self.running = False
        self.state = "Warmup"
        self.current_round = 0
        self.max_rounds = 5
        self.bot_count = 0

    def set_output_handler(self, handler):
        self.output_handler = handler

    def send_command(self, command):
        if self.output_handler:
            self.output_handler(f"Server received: {command}")

    def set_async_loop(self, loop):
        pass

    def start_server(self):
        self.running = True

    def run_server_loop(self):
        while self.running:
            if self.output_handler:
                messages = [
                    "Player connected from 192.168.1.100",
                    "Match started on map dm17",
                    "Player fragged by rail gun",
                    "Bot added: Anarki",
                    "Latency changed to 50ms",
                    "OBS recording started",
                    "Player disconnected",
                    "Match ended",
                ]
                msg = random.choice(messages)
                self.output_handler(f"[{time.strftime('%H:%M:%S')}] {msg}")
            time.sleep(2)

    def dispose(self):
        self.running = False

class QuitConfirmScreen(ModalScreen[bool]):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Exit TUI test?"),
            Horizontal(
                Button("Yes", variant="error", id="yes"),
                Button("Cancel", variant="default", id="cancel"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")

class MockTUIApp(App):
    CSS_PATH = "tui_test.tcss"
    BINDINGS = [Binding("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Vertical(
            Horizontal(
                Input(placeholder="Enter command...", id="input"),
                Label("State: Warmup", id="status-state"),
                Label("Round: 0/5", id="status-round"),
                Button("Add Bot", id="add-bot-btn", variant="primary"),
                Button("Remove Bot", id="remove-bot-btn", variant="default"),
                id="top-panel"
            ),
            Horizontal(
                DataTable(id="user-table"),
                Vertical(
                    Log(id="app-log"),
                    Log(id="server-log"),
                    id="right-panel"
                ),
                id="content-panel"
            ),
            id="main-container"
        )

    def on_mount(self) -> None:
        app_log = self.query_one("#app-log", Log)
        server_log = self.query_one("#server-log", Log)

        app_log.border_title = "App Logs"
        server_log.border_title = "Server Output"

        input_widget = self.query_one("#input", Input)
        input_widget.border_title = "Command Input"

        user_table = self.query_one("#user-table", DataTable)
        user_table.border_title = "Connected Users"
        user_table.add_columns("Name", "OBS", "Action")

        self.server = MockServer()
        self.server.set_output_handler(lambda msg: server_log.write_line(msg))

        app_log.write_line("Mock TUI started")
        app_log.write_line("Type commands to test input")
        app_log.write_line("Press 'q' to quit")

        self.update_status_display()
        self.populate_user_table()

        import threading
        server_thread = threading.Thread(target=self.server.run_server_loop, daemon=True)
        server_thread.start()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        command = message.value.strip()
        if command:
            app_log = self.query_one("#app-log", Log)
            app_log.write_line(f"Command entered: {command}")

            if command.lower() in ['quit', 'exit']:
                self.action_quit()
            else:
                self.server.send_command(command)
                self.query_one("#input", Input).value = ""

    def action_quit(self) -> None:
        def check_quit(confirmed: bool | None) -> None:
            if confirmed:
                self.server.dispose()
                self.exit()

        self.push_screen(QuitConfirmScreen(), check_quit)

    def update_status_display(self):
        state_label = self.query_one("#status-state", Label)
        round_label = self.query_one("#status-round", Label)

        state_label.update(f"State: {self.server.state}")
        round_label.update(f"Round: {self.server.current_round}/{self.server.max_rounds}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-bot-btn":
            self.server.bot_count += 1
            app_log = self.query_one("#app-log", Log)
            app_log.write_line(f"Bot added! Total bots: {self.server.bot_count}")
            self.server.send_command(f"addbot")
        elif event.button.id == "remove-bot-btn":
            if self.server.bot_count > 0:
                self.server.bot_count -= 1
                app_log = self.query_one("#app-log", Log)
                app_log.write_line(f"Bot removed! Total bots: {self.server.bot_count}")
                self.server.send_command(f"kick bot")

    def populate_user_table(self):
        user_table = self.query_one("#user-table", DataTable)

        mock_users = [
            ("Player1", "✓", "Kick"),
            ("Player2", "✗", "Kick"),
            ("Player3", "✓", "Kick"),
            ("Bot_Anarki", "N/A", "Kick"),
        ]

        for name, obs_status, action in mock_users:
            user_table.add_row(name, obs_status, action)

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        if event.data_table.id == "user-table":
            row_key = event.row_key
            user_table = self.query_one("#user-table", DataTable)
            row_data = user_table.get_row(row_key)
            user_name = row_data[0]

            app_log = self.query_one("#app-log", Log)
            app_log.write_line(f"Kicking user: {user_name}")
            self.server.send_command(f"kick {user_name}")

def main():
    app = MockTUIApp()
    app.run()

if __name__ == "__main__":
    main()