"""
Source RCON Protocol Client.

Implementation of Valve's Source RCON protocol for communicating with
Source engine game servers (Dota 2, CS2, TF2, etc.).

Protocol specification:
https://developer.valvesoftware.com/wiki/Source_RCON_Protocol
"""

import asyncio
import logging
import struct
from enum import IntEnum
from typing import Optional, Tuple


class RCONPacketType(IntEnum):
    """RCON packet types as defined by the Source RCON protocol."""
    SERVERDATA_AUTH = 3
    SERVERDATA_AUTH_RESPONSE = 2
    SERVERDATA_EXECCOMMAND = 2
    SERVERDATA_RESPONSE_VALUE = 0


class RCONError(Exception):
    """Base exception for RCON errors."""
    pass


class RCONAuthError(RCONError):
    """Authentication failed."""
    pass


class RCONConnectionError(RCONError):
    """Connection error."""
    pass


class SourceRCONClient:
    """
    Async Source RCON protocol client.

    Provides TCP-based communication with Source engine game servers
    using the RCON protocol for remote administration.

    Packet structure:
    - Size (4 bytes, little endian) - size of packet body (id + type + body + nulls)
    - ID (4 bytes, little endian) - request ID for matching responses
    - Type (4 bytes, little endian) - packet type
    - Body (variable) - null-terminated ASCII string
    - Empty string (1 byte) - null terminator

    Example usage:
        async with SourceRCONClient("localhost", 27015, "password") as rcon:
            response = await rcon.execute("status")
            print(response)
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 27015,
        password: str = "",
        timeout: float = 10.0,
    ):
        self.host = host
        self.port = port
        self.password = password
        self.timeout = timeout

        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._request_id = 0
        self._authenticated = False
        self._lock = asyncio.Lock()
        self.logger = logging.getLogger(__name__)

    @property
    def is_connected(self) -> bool:
        """Check if connected to server."""
        return self._writer is not None and not self._writer.is_closing()

    @property
    def is_authenticated(self) -> bool:
        """Check if authenticated with server."""
        return self._authenticated and self.is_connected

    async def __aenter__(self) -> "SourceRCONClient":
        """Async context manager entry."""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.disconnect()

    async def connect(self) -> bool:
        """
        Connect and authenticate with RCON server.

        Returns:
            True if connection and authentication succeeded.

        Raises:
            RCONConnectionError: If connection fails.
            RCONAuthError: If authentication fails.
        """
        try:
            self.logger.info(f"Connecting to RCON server at {self.host}:{self.port}")

            self._reader, self._writer = await asyncio.wait_for(
                asyncio.open_connection(self.host, self.port),
                timeout=self.timeout,
            )

            self.logger.debug("TCP connection established, authenticating...")
            authenticated = await self._authenticate()

            if authenticated:
                self.logger.info(
                    f"Successfully connected and authenticated to {self.host}:{self.port}"
                )
            return authenticated

        except asyncio.TimeoutError:
            self.logger.error(f"Connection timeout to {self.host}:{self.port}")
            raise RCONConnectionError(
                f"Connection timeout to {self.host}:{self.port}"
            )
        except ConnectionRefusedError:
            self.logger.error(f"Connection refused by {self.host}:{self.port}")
            raise RCONConnectionError(
                f"Connection refused by {self.host}:{self.port}"
            )
        except OSError as e:
            self.logger.error(f"Connection error: {e}")
            raise RCONConnectionError(f"Connection error: {e}")

    async def _authenticate(self) -> bool:
        """
        Send authentication packet and verify response.

        Returns:
            True if authentication succeeded.

        Raises:
            RCONAuthError: If authentication fails.
        """
        auth_id = self._get_next_id()

        await self._send_packet(
            auth_id, RCONPacketType.SERVERDATA_AUTH, self.password
        )

        # Read auth response - may receive empty packet first
        response_id, response_type, _ = await self._receive_packet()

        # Check for auth failure (-1 response ID)
        if response_id == -1:
            self._authenticated = False
            self.logger.error("RCON authentication failed - invalid password")
            raise RCONAuthError("Authentication failed - invalid password")

        # Some servers send an empty SERVERDATA_RESPONSE_VALUE before the auth response
        if response_type == RCONPacketType.SERVERDATA_RESPONSE_VALUE:
            response_id, response_type, _ = await self._receive_packet()

        if response_id == -1:
            self._authenticated = False
            self.logger.error("RCON authentication failed - invalid password")
            raise RCONAuthError("Authentication failed - invalid password")

        self._authenticated = True
        self.logger.debug("RCON authentication successful")
        return True

    async def execute(self, command: str) -> str:
        """
        Execute RCON command and return response.

        Args:
            command: The command to execute on the server.

        Returns:
            The server's response as a string.

        Raises:
            RCONError: If not authenticated or command fails.
        """
        if not self._authenticated:
            raise RCONError("Not authenticated - call connect() first")

        async with self._lock:
            request_id = self._get_next_id()

            self.logger.info(f"Executing RCON command: {command} (request_id={request_id})")

            await self._send_packet(
                request_id, RCONPacketType.SERVERDATA_EXECCOMMAND, command
            )

            # Collect response packets - wait for response with matching ID
            # Some servers don't support the end marker technique
            response_parts = []
            packets_received = 0

            while True:
                try:
                    resp_id, resp_type, body = await asyncio.wait_for(
                        self._receive_packet(), timeout=2.0  # Short timeout per packet
                    )
                    packets_received += 1

                    self.logger.info(
                        f"Received packet #{packets_received}: id={resp_id}, type={resp_type}, "
                        f"body_len={len(body)}, body_preview={body[:50] if body else '(empty)'}..."
                    )

                    if resp_id == request_id:
                        response_parts.append(body)
                        self.logger.info(f"Matched request_id, added to response parts")
                    else:
                        self.logger.info(f"ID mismatch: got {resp_id}, expected {request_id}")

                except asyncio.TimeoutError:
                    self.logger.info(f"Read timeout after {packets_received} packets, returning collected data")
                    break

            response = "".join(response_parts)
            self.logger.info(f"RCON response ({len(response)} chars): {response[:200]}...")
            return response

    async def disconnect(self) -> None:
        """Close RCON connection."""
        if self._writer:
            self.logger.info("Disconnecting from RCON server")
            try:
                self._writer.close()
                await self._writer.wait_closed()
            except Exception as e:
                self.logger.debug(f"Error during disconnect: {e}")

        self._reader = None
        self._writer = None
        self._authenticated = False

    def _get_next_id(self) -> int:
        """Generate next request ID."""
        self._request_id = (self._request_id + 1) % 0x7FFFFFFF
        return self._request_id

    async def _send_packet(
        self, request_id: int, packet_type: int, body: str
    ) -> None:
        """
        Encode and send RCON packet.

        Packet format:
        - Size (4 bytes) = len(body) + 10 (for id, type, and 2 null terminators)
        - ID (4 bytes)
        - Type (4 bytes)
        - Body (variable, null-terminated)
        - Empty string (1 byte null)
        """
        body_bytes = body.encode("utf-8") + b"\x00\x00"
        size = 4 + 4 + len(body_bytes)  # id + type + body with nulls

        packet = struct.pack("<iii", size, request_id, packet_type) + body_bytes

        self._writer.write(packet)
        await self._writer.drain()

    async def _receive_packet(self) -> Tuple[int, int, str]:
        """
        Receive and decode RCON packet.

        Returns:
            Tuple of (request_id, packet_type, body).
        """
        # Read packet size
        size_data = await self._reader.readexactly(4)
        size = struct.unpack("<i", size_data)[0]

        # Read packet body
        body_data = await self._reader.readexactly(size)

        # Unpack ID and type
        request_id, packet_type = struct.unpack("<ii", body_data[:8])

        # Extract body (strip null terminators)
        body = body_data[8:-2].decode("utf-8", errors="replace")

        return request_id, packet_type, body

    async def get_status(self) -> str:
        """Get server status."""
        return await self.execute("status")

    async def say(self, message: str) -> str:
        """Send chat message to all players."""
        return await self.execute(f"say {message}")

    async def kick(self, player_id: str) -> str:
        """Kick a player by ID."""
        return await self.execute(f"kick {player_id}")
