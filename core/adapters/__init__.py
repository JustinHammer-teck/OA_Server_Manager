"""Game adapter abstraction layer for multi-game support."""

from core.adapters.base import (
    ConnectionType,
    GameAdapter,
    GameAdapterConfig,
    BaseMessageProcessor,
    BaseGameManager,
    MessageType,
    ParsedMessage,
)
from core.adapters.registry import GameAdapterRegistry, register_default_adapters

__all__ = [
    "ConnectionType",
    "GameAdapter",
    "GameAdapterConfig",
    "BaseMessageProcessor",
    "BaseGameManager",
    "MessageType",
    "ParsedMessage",
    "GameAdapterRegistry",
    "register_default_adapters",
]
