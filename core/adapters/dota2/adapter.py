"""Dota 2 game adapter using Source RCON protocol."""

import asyncio
import logging
from typing import AsyncIterator, Optional

from core.adapters.base import ConnectionType, GameAdapter, GameAdapterConfig
from core.adapters.dota2.rcon_client import SourceRCONClient, RCONError


class Dota2GameAdapter(GameAdapter):
    """
    Dota 2 game adapter using Source RCON protocol.

    This adapter connects to an already-running Dota 2 dedicated server
    via RCON for remote administration. Unlike the OpenArena adapter,
    it does not manage the server process lifecycle.

    Key differences from subprocess-based adapters:
    - Connects to existing server (doesn't start subprocess)
    - Commands are request/response (not fire-and-forget)
    - Password-based authentication required
    """

    def __init__(self, config: GameAdapterConfig):
        self.config = config
        self.rcon = SourceRCONClient(
            host=config.host,
            port=config.port,
            password=config.password or "",
            timeout=10.0,
        )
        self._polling = False
        self._poll_interval = config.poll_interval or 5.0
        self._shutdown_requested = False
        self.logger = logging.getLogger(__name__)

    @property
    def connection_type(self) -> ConnectionType:
        return ConnectionType.RCON

    @property
    def is_connected(self) -> bool:
        return self.rcon.is_authenticated

    async def connect(self) -> bool:
        """
        Connect and authenticate with Dota 2 RCON server.

        Returns:
            True if connection and authentication succeeded.
        """
        try:
            self.logger.info(
                f"Connecting to Dota 2 server at {self.config.host}:{self.config.port}"
            )
            await self.rcon.connect()
            self.logger.info("Successfully connected to Dota 2 server via RCON")
            return True
        except RCONError as e:
            self.logger.error(f"Failed to connect to Dota 2 server: {e}")
            return False

    async def disconnect(self) -> None:
        """Disconnect from Dota 2 server."""
        self._polling = False
        self._shutdown_requested = True
        await self.rcon.disconnect()
        self.logger.info("Disconnected from Dota 2 server")

    async def send_command(self, command: str) -> Optional[str]:
        """
        Send RCON command and return response.

        Unlike subprocess-based adapters, RCON is request/response,
        so we get the response directly.

        Args:
            command: The RCON command to execute.

        Returns:
            The server's response, or None if failed.
        """
        try:
            response = await self.rcon.execute(command)
            return response
        except RCONError as e:
            self.logger.error(f"RCON command failed: {e}")
            return None

    def send_command_sync(self, command: str) -> None:
        """
        Synchronous command sending for callback compatibility.

        Creates a task to send the command asynchronously.
        """
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(self.send_command(command))
            else:
                loop.run_until_complete(self.send_command(command))
        except RuntimeError:
            # No event loop - create one
            asyncio.run(self.send_command(command))

    async def read_messages(self) -> AsyncIterator[str]:
        """
        Read messages from server via RCON polling.

        Yields status poll responses at configured interval.
        """
        self._polling = True

        while self._polling and self.is_connected and not self._shutdown_requested:
            try:
                status = await self.rcon.get_status()
                if status:
                    yield f"STATUS_POLL:{status}"

            except RCONError as e:
                self.logger.error(f"Status poll failed: {e}")
                try:
                    await self.rcon.connect()
                except RCONError:
                    self.logger.error("Reconnection failed, stopping polling")
                    break

            await asyncio.sleep(self._poll_interval)

    def start_server(self) -> bool:
        """
        For Dota 2, server is assumed to already be running.

        This is a no-op since the adapter connects to an existing server.
        Returns True to indicate "ready to connect".
        """
        self.logger.info(
            "Dota 2 adapter assumes server is already running. "
            f"Will connect to {self.config.host}:{self.config.port}"
        )
        return True

    def stop_server(self) -> None:
        """
        Request server shutdown via RCON.

        Note: This sends a quit command but the server process
        management is external to this adapter.
        """
        self._shutdown_requested = True
        self._polling = False
        try:
            # Try to send quit command
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(self.send_command("quit"))
            else:
                loop.run_until_complete(self.send_command("quit"))
        except Exception as e:
            self.logger.debug(f"Error sending quit command: {e}")

    def request_shutdown(self) -> None:
        """Request graceful shutdown."""
        self._shutdown_requested = True
        self._polling = False

    def is_shutdown_requested(self) -> bool:
        """Check if shutdown has been requested."""
        return self._shutdown_requested
