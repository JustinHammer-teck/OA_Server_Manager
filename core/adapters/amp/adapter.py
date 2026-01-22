"""AMP (CubeCoders) game adapter using HTTP API."""
from __future__ import annotations

import asyncio
import logging
from collections import OrderedDict
from typing import Any, AsyncIterator, Callable, Optional, TypeVar

from core.adapters.base import ConnectionType, GameAdapter, GameAdapterConfig
from core.adapters.amp.amp_api_client import AMPAPIClient, AMPAPIError

T = TypeVar("T")
from core.adapters.amp.message_processor import AMPMessageProcessor


def _parse_credentials(password_field: str | None) -> tuple[str, str]:
    """Parse 'username:password' format from config password field."""
    if not password_field:
        return "", ""
    if ":" in password_field:
        parts = password_field.split(":", 1)
        return parts[0], parts[1]
    return "", password_field


def _run_async(coro_fn: Callable[[], Any]) -> Any:
    """Run an async coroutine from sync context, handling event loop scenarios."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            asyncio.create_task(coro_fn())
            return None
        return loop.run_until_complete(coro_fn())
    except RuntimeError:
        return asyncio.run(coro_fn())


class AMPGameAdapter(GameAdapter):
    """
    Game adapter for servers managed by CubeCoders AMP.

    Uses the AMP HTTP API to:
    - Stream console messages via Core.GetUpdates polling
    - Send commands via Core.SendConsoleMessage
    - Control server lifecycle (start/stop/restart)

    Key differences from direct RCON:
    - Connects to AMP panel, not game server directly
    - Console messages retrieved via polling (not real-time)
    - Unified interface for any game AMP supports
    """

    def __init__(self, config: GameAdapterConfig):
        self.config = config
        username, password = _parse_credentials(config.password)
        self.api = AMPAPIClient(
            base_url=config.host,
            username=username,
            password=password,
            instance_id=getattr(config, "instance_id", None),
            timeout=30.0,
        )
        self._polling = False
        self._poll_interval = config.poll_interval or 2.0
        self._shutdown_requested = False
        self._seen_messages: OrderedDict[str, None] = (
            OrderedDict()
        )  # Ordered for proper LRU eviction
        self._max_seen_cache = 1000
        self.logger = logging.getLogger(__name__)

        self.message_processor = AMPMessageProcessor(
            send_command_callback=lambda cmd: asyncio.create_task(self.send_command(cmd))
            )

    @property
    def connection_type(self) -> ConnectionType:
        return ConnectionType.WEBSOCKET  # Closest match - HTTP polling

    @property
    def is_connected(self) -> bool:
        return self.api.is_authenticated

    async def connect(self) -> bool:
        """
        Connect and authenticate with AMP API.

        Returns:
            True if authentication succeeded.
        """
        try:
            self.logger.info(f"Connecting to AMP at {self.config.host}")
            await self.api.login()
            self.logger.info("Successfully authenticated with AMP")
            return True
        except AMPAPIError as e:
            self.logger.error(f"Failed to connect to AMP: {e}")
            return False

    async def disconnect(self) -> None:
        """Disconnect from AMP API."""
        self._polling = False
        self._shutdown_requested = True
        await self.api.close()
        self._seen_messages.clear()
        self.logger.info("Disconnected from AMP")

    async def send_command(self, command: str) -> Optional[str]:
        """
        Send command to game server via AMP console.

        Args:
            command: The command to execute.

        Returns:
            None (AMP console commands are fire-and-forget).
        """
        try:
            await self.api.send_console_message(command)
            self.logger.debug(f"Sent command: {command}")
            return None  # AMP doesn't return command output directly
        except AMPAPIError as e:
            self.logger.error(f"Failed to send command: {e}")
            return None

    async def read_messages(self) -> AsyncIterator[str]:
        """
        Read console messages from AMP via polling.

        Yields console entries as they appear.
        """
        self._polling = True
        self._seen_messages.clear()

        while self._polling and self.is_connected and not self._shutdown_requested:
            try:
                updates = await self.api.get_updates()

                for entry in updates.console_entries:
                    msg_key = f"{entry.timestamp.isoformat()}:{entry.contents}"

                    if msg_key not in self._seen_messages:
                        self._seen_messages[msg_key] = None

                        # Evict oldest entries when cache exceeds limit (proper FIFO)
                        while len(self._seen_messages) > self._max_seen_cache:
                            self._seen_messages.popitem(last=False)

                        parsed = self.message_processor.process_message(entry.contents)
                        yield parsed


                if updates.status:
                    state = updates.status.get("State", "Unknown")
                    yield f"STATUS_POLL:State={state}"

            except AMPAPIError as e:
                self.logger.error(f"GetUpdates failed: {e}")
                try:
                    await self.api.login()
                    self.logger.info("Reconnected to AMP")
                except AMPAPIError:
                    self.logger.error("Reconnection failed, stopping polling")
                    break

            await asyncio.sleep(self._poll_interval)

    def start_server(self) -> bool:
        """Start game server via AMP."""
        self.logger.info("Requesting server start via AMP")
        try:
            _run_async(self._start_server_async)
            return True
        except Exception as e:
            self.logger.error(f"Failed to start server: {e}")
            return False

    async def _start_server_async(self) -> None:
        """Async helper for starting server."""
        try:
            await self.api.start_instance()
            self.logger.info("Server start command sent")
        except AMPAPIError as e:
            self.logger.error(f"Failed to start server: {e}")

    def stop_server(self) -> None:
        """Stop game server via AMP."""
        self._shutdown_requested = True
        self._polling = False
        _run_async(self._stop_server_async)

    async def _stop_server_async(self) -> None:
        """Async helper for stopping server."""
        try:
            await self.api.stop_instance()
            self.logger.info("Server stop command sent")
        except AMPAPIError as e:
            self.logger.debug(f"Error stopping server: {e}")

    def request_shutdown(self) -> None:
        """Request graceful shutdown."""
        self._shutdown_requested = True
        self._polling = False

    def is_shutdown_requested(self) -> bool:
        """Check if shutdown has been requested."""
        return self._shutdown_requested

    async def get_server_status(self) -> Optional[dict]:
        """
        Get detailed server status from AMP.

        Returns:
            Status dict or None if failed.
        """
        try:
            return await self.api.get_status()
        except AMPAPIError as e:
            self.logger.error(f"Failed to get status: {e}")
            return None