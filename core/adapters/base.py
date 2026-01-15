"""Abstract base classes for game adapters."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, AsyncIterator, Callable, Dict, List, Optional


class ConnectionType(Enum):
    """Type of connection to game server."""
    SUBPROCESS = "subprocess"  # stdin/stdout/stderr (OpenArena)
    RCON = "rcon"              # Source RCON TCP protocol (Dota 2, CS2)
    WEBSOCKET = "websocket"    # For future games


class MessageType(Enum):
    """Game-agnostic message types."""
    CLIENT_CONNECT = "client_connect"
    CLIENT_DISCONNECT = "client_disconnect"
    GAME_START = "game_start"
    GAME_END = "game_end"
    WARMUP_START = "warmup_start"
    WARMUP_END = "warmup_end"
    PLAYER_KILL = "player_kill"
    CHAT_MESSAGE = "chat_message"
    STATUS_UPDATE = "status_update"
    SERVER_SHUTDOWN = "server_shutdown"
    GAME_INITIALIZATION = "game_initialization"
    UNKNOWN = "unknown"


@dataclass
class ParsedMessage:
    """Normalized parsed message structure."""
    message_type: MessageType
    raw_message: str
    data: Dict[str, Any] = field(default_factory=dict)
    timestamp: Optional[float] = None


@dataclass
class GameAdapterConfig:
    """Configuration for game adapter initialization."""
    game_type: str
    host: str = "localhost"
    port: int = 27015
    password: Optional[str] = None
    binary_path: Optional[str] = None
    startup_args: Optional[List[str]] = None
    poll_interval: float = 5.0


class GameAdapter(ABC):
    """
    Abstract interface for game server communication.

    Responsibilities:
    - Server lifecycle (start, stop, connect, disconnect)
    - Command sending (game-specific encoding)
    - Message reading (async generator pattern)
    """

    @property
    @abstractmethod
    def connection_type(self) -> ConnectionType:
        """Return the connection type for this adapter."""
        pass

    @property
    @abstractmethod
    def is_connected(self) -> bool:
        """Check if adapter is connected to game server."""
        pass

    @abstractmethod
    async def connect(self) -> bool:
        """Establish connection to game server. Returns success status."""
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """Gracefully disconnect from game server."""
        pass

    @abstractmethod
    async def send_command(self, command: str) -> Optional[str]:
        """
        Send command to game server.
        Returns response for RCON, None for subprocess (async response via read).
        """
        pass

    @abstractmethod
    async def read_messages(self) -> AsyncIterator[str]:
        """
        Async generator yielding server messages.
        For subprocess: reads from stderr
        For RCON: may need polling or log streaming
        """
        pass

    @abstractmethod
    def start_server(self) -> bool:
        """
        Start the game server process (if applicable).
        For RCON: may be no-op if connecting to existing server.
        """
        pass

    @abstractmethod
    def stop_server(self) -> None:
        """Stop/terminate the game server."""
        pass


class BaseMessageProcessor(ABC):
    """
    Abstract interface for parsing game server output.
    Each game adapter implements game-specific regex/parsing.
    """

    def __init__(self, send_command_callback: Optional[Callable[[str], None]] = None):
        self.send_command = send_command_callback

    @abstractmethod
    def process_message(self, raw_message: str) -> ParsedMessage:
        """Parse raw server output into normalized ParsedMessage."""
        pass

    @abstractmethod
    def get_supported_message_types(self) -> List[MessageType]:
        """Return list of message types this processor can detect."""
        pass


class BaseGameManager(ABC):
    """
    Abstract interface for game-specific operations.
    Encapsulates commands like adding bots, setting game rules, etc.
    """

    def __init__(self, send_command_callback: Callable[[str], None]):
        self.send_command = send_command_callback

    @abstractmethod
    def apply_startup_config(self) -> Dict[str, str]:
        """Return game-specific startup configuration."""
        pass

    @abstractmethod
    def apply_default_config(self) -> bool:
        """Apply default game configuration."""
        pass

    @abstractmethod
    async def add_bots(self, count: int, difficulty: int = 1) -> bool:
        """Add AI bots to the game."""
        pass

    @abstractmethod
    def kick_player(self, player_id: Any) -> bool:
        """Kick a player from the server."""
        pass

    @abstractmethod
    def broadcast_message(self, message: str) -> bool:
        """Send message to all players."""
        pass

    @abstractmethod
    def parse_status_response(self, response: str) -> List[Dict[str, Any]]:
        """Parse status command response into player list."""
        pass
