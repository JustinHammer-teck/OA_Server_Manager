"""OpenArena game adapter using subprocess/stdin communication."""

import asyncio
import logging
import subprocess
import threading
from subprocess import PIPE, Popen
from typing import AsyncIterator, Optional

from core.adapters.base import ConnectionType, GameAdapter, GameAdapterConfig
import core.utils.settings as settings


class OAGameAdapter(GameAdapter):
    """
    OpenArena game adapter using subprocess/stdin communication.

    This adapter manages the oa_ded (OpenArena dedicated server) process,
    sending commands via stdin and reading responses from stderr.
    """

    def __init__(self, config: GameAdapterConfig):
        self.config = config
        self._process: Optional[Popen] = None
        self._shutdown_event = threading.Event()
        self.logger = logging.getLogger(__name__)

    @property
    def connection_type(self) -> ConnectionType:
        return ConnectionType.SUBPROCESS

    @property
    def is_connected(self) -> bool:
        return self._process is not None and self._process.poll() is None

    async def connect(self) -> bool:
        """For subprocess, 'connect' means starting the server."""
        return self.start_server()

    async def disconnect(self) -> None:
        """Stop the server process."""
        self.stop_server()

    async def send_command(self, command: str) -> Optional[str]:
        """
        Send command via stdin. Returns None (responses come via stderr).
        """
        if self._process and self._process.poll() is None:
            try:
                self.logger.debug(f"CMD_SEND: {command}")
                self._process.stdin.write(f"{command}\r\n".encode())
                self._process.stdin.flush()
                return None
            except (BrokenPipeError, OSError) as e:
                self.logger.error(f"Failed to send command: {e}")
        return None

    def send_command_sync(self, command: str) -> None:
        """Synchronous command sending for callback compatibility."""
        if self._process and self._process.poll() is None:
            try:
                self.logger.debug(f"CMD_SEND: {command}")
                self._process.stdin.write(f"{command}\r\n".encode())
                self._process.stdin.flush()
            except (BrokenPipeError, OSError) as e:
                self.logger.error(f"Failed to send command: {e}")

    async def read_messages(self) -> AsyncIterator[str]:
        """Yield messages from stderr."""
        while not self._shutdown_event.is_set() and self.is_connected:
            try:
                line = self._process.stderr.readline().decode(
                    "utf-8", errors="replace"
                ).rstrip()
                if line:
                    yield line
            except (OSError, ValueError):
                break
            await asyncio.sleep(0.01)

    def read_message_sync(self) -> str:
        """Synchronous message reading for the main loop."""
        try:
            return (
                self._process.stderr.readline()
                .decode("utf-8", errors="replace")
                .rstrip()
            )
        except (OSError, ValueError) as e:
            self.logger.error(f"Failed to read from server: {e}")
            return ""

    def start_server(self) -> bool:
        """Start the OpenArena dedicated server process."""
        self.logger.info("Starting OpenArena server process")

        # Build server arguments
        binary_path = self.config.binary_path or "oa_ded"
        port = self.config.port or 27960

        server_args = [
            binary_path,
            "+set", "dedicated", "1",
            "+set", "net_port", str(port),
            "+set", "com_legacyprotocol", "71",
            "+set", "com_protocol", "71",
            "+set", "sv_pure", "0",
            "+set", "sv_master1", "dpmaster.deathmask.net",
            "+set", "sv_maxclients", "4",
            "+set", "cl_motd", "Welcome To ASTRID lab",
        ]

        # Add startup config from settings
        startup_config = {
            "timelimit": str(settings.timelimit),
            "capturelimit": str(settings.fraglimit),
            "g_doWarmup": "1" if settings.enable_warmup else "0",
            "g_warmup": str(settings.warmup_time),
        }

        for key, value in startup_config.items():
            server_args.extend(["+set", key, value])

        server_args.extend(["+exec", "t_server.cfg"])

        try:
            self._process = Popen(
                server_args,
                stdout=PIPE,
                stdin=PIPE,
                stderr=PIPE,
                universal_newlines=False,
            )
            self.logger.info(f"OpenArena server started with PID {self._process.pid}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to start OpenArena server: {e}")
            return False

    def stop_server(self) -> None:
        """Stop/terminate the game server."""
        self._shutdown_event.set()

        if self._process and self._process.poll() is None:
            self.logger.info("Terminating OpenArena server process")
            self._process.terminate()
            try:
                self._process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._process.kill()
                self._process.wait()
            self.logger.info("OpenArena server stopped")

    def request_shutdown(self) -> None:
        """Request graceful shutdown."""
        self._shutdown_event.set()

    def is_shutdown_requested(self) -> bool:
        """Check if shutdown has been requested."""
        return self._shutdown_event.is_set()
