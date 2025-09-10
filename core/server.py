import logging
import subprocess
import time
from enum import Enum
from subprocess import PIPE, Popen

import core.settings as settings
from core.client_manager import ClientManager


class ServerState(Enum):
    WAITING = 1
    WARMUP = 2
    RUNNING = 3


class Server:
    __slots__ = ("_process", "i", "state", "logger", "nplayers_threshold", "client_manager")

    def __init__(self):
        self.i: int = 0
        self.state: ServerState = ServerState.WAITING
        self.logger = logging.getLogger(__name__)
        self.nplayers_threshold: int = settings.nplayers_threshold
        self.client_manager = ClientManager()

    def start_server(self):
        self.logger.info("Start OA Server process")
        self._process = Popen(
            [
                "oa_ded",
                "+set",
                "dedicated",
                "1",
                "+set",
                "net_port",
                "27960",
                "+set",
                "com_legacyprotocol",
                "71",
                "+set",
                "com_protocol",
                "71",
                "+set",
                "sv_master1",
                "dpmaster.deathmask.net",
                "+set",
                "cl_motd",
                "0",
                "+set",
                "com_homepath",
                "server.oa",
                "+exec",
                "t_server.cfg",
            ],
            stdout=PIPE,
            stdin=PIPE,
            stderr=PIPE,
            universal_newlines=False,
        )

        self._server_init()

    def _server_init(self):
        if settings.bot_enable:
            max_clients = self.nplayers_threshold + settings.bot_count
            self.logger.debug(f"Setting maximum number of clients to {max_clients}")
            self.send_command(f"set sv_maxclients {max_clients}")

            self.send_command("set bot_enable 1")
            self.send_command("set bot_nochat 1")
            self.send_command("set bot_minplayers 0")
        else:
            self.logger.info("Bots are disable")

    def send_command(self, command: str):
        """Sends a command to the server's stdin."""
        if self._process and self._process.poll() is None:
            self.logger.debug(f"CMD_SEND: {command}")
            self._process.stdin.write(f"{command}\r\n".encode())
            self._process.stdin.flush()

    def read_server(self) -> str:
        return (
            self._process.stderr.readline().decode("utf-8", errors="replace").rstrip()
        )

    def dispose(self):
        if self._process and self._process.poll() is None:
            self._process.terminate()
            try:
                self._process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.logger.error(
                    f"Cannot properly terminal process {self._process.pid}"
                )
                self.logger.info("Gracefully kill the process")
                self._process.kill()
                self._process.wait()

        self.logger.info("Successfully dispose server process")

    def add_bots(self, num_bots, difficulty, bot_names):
        """
        Add bots to the server with the same difficulty level.

        Args:
            num_bots: Number of bots to add
            difficulty: Single difficulty level for all bots (1-5)
            bot_names: List of valid bot names
        """
        self.logger.info(
            f"Adding {num_bots} bots to the server with difficulty {difficulty}..."
        )

        # Make sure there are enough names
        while len(bot_names) < num_bots:
            bot_names.extend(bot_names)
        bot_names = bot_names[:num_bots]

        for i in range(num_bots):
            name = bot_names[i]

            self.logger.debug(f"Adding bot {name} with difficulty {difficulty}")
            # Format: "addbot [name] [difficulty]"
            self.send_command(f"addbot {name} {difficulty}")
            time.sleep(1)  # Small delay between adding bots

        self.logger.info("All bots added successfully")
