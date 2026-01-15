"""OpenArena game adapter implementation."""

from core.adapters.openarena.adapter import OAGameAdapter
from core.adapters.openarena.message_processor import OAMessageProcessor
from core.adapters.openarena.game_manager import OAGameManager

__all__ = ["OAGameAdapter", "OAMessageProcessor", "OAGameManager"]
