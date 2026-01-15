"""OpenArena-specific game management."""

import asyncio
import logging
from typing import Any, Callable, Dict, List

from core.adapters.base import BaseGameManager
import core.utils.settings as settings


class OAGameManager(BaseGameManager):
    """
    OpenArena-specific game management.

    Handles bot addition, game configuration, and OA-specific console commands.
    """

    # Default OpenArena bot names
    OA_BOT_NAMES = [
        "Angelyss",
        "Arachna",
        "Major",
        "Sarge",
        "Skelebot",
        "Merman",
        "Beret",
        "Kyonshi",
    ]

    def __init__(self, send_command_callback: Callable[[str], None]):
        super().__init__(send_command_callback)
        self.logger = logging.getLogger(__name__)

        self._current_config: Dict[str, str] = {}
        self._bots_added = False
        self._bot_addition_in_progress = False

    def should_add_bots(self) -> bool:
        """Check if bots should be added based on settings."""
        return settings.bot_enable and settings.bot_count > 0

    def are_bots_added(self) -> bool:
        """Check if bots have been added."""
        return self._bots_added

    def is_bot_addition_in_progress(self) -> bool:
        """Check if bot addition is in progress."""
        return self._bot_addition_in_progress

    def apply_startup_config(self) -> Dict[str, str]:
        """Get startup configuration for server."""
        return {
            "timelimit": str(settings.timelimit),
            "capturelimit": str(settings.fraglimit),
            "g_doWarmup": "1" if settings.enable_warmup else "0",
            "g_warmup": str(settings.warmup_time),
        }

    def apply_default_config(self) -> bool:
        """Apply default game configuration."""
        try:
            self.send_command(f"set timelimit {settings.timelimit}")
            self.send_command(f"set fraglimit {settings.fraglimit}")

            if settings.enable_warmup:
                self.send_command("set g_doWarmup 1")
                self.send_command(f"set g_warmup {settings.warmup_time}")

            self.logger.info("Default game configuration applied")
            return True

        except Exception as e:
            self.logger.error(f"Error applying default config: {e}")
            return False

    async def add_bots(self, count: int, difficulty: int = 1) -> bool:
        """Add bots to the server asynchronously."""
        if self._bots_added:
            self.logger.debug("Bots already added, skipping")
            return True

        if self._bot_addition_in_progress:
            self.logger.info("Bot addition already in progress")
            return False

        self.logger.info(f"Starting asynchronous bot addition: {count} bots")
        self._bot_addition_in_progress = True

        try:
            for i in range(count):
                # Use custom bot names from settings if available
                if i < len(settings.bot_names) and settings.bot_names[i]:
                    bot_name = settings.bot_names[i]
                else:
                    bot_name = self.OA_BOT_NAMES[i % len(self.OA_BOT_NAMES)]

                self.send_command(f"addbot {bot_name} {difficulty}")
                self.logger.info(f"Added bot {bot_name} with difficulty {difficulty}")
                await asyncio.sleep(0.1)

            self._bots_added = True
            self.send_command(f"say Added {count} bots to the server")
            self.logger.info(f"Successfully added {count} bots")
            return True

        except Exception as e:
            self.logger.error(f"Error adding bots: {e}")
            return False
        finally:
            self._bot_addition_in_progress = False

    async def add_bots_to_server_async(self) -> bool:
        """Legacy method for compatibility with existing code."""
        if not self.should_add_bots():
            self.logger.info("Bot addition disabled or count is 0")
            return False
        return await self.add_bots(settings.bot_count, settings.bot_difficulty)

    def kick_player(self, player_id: Any) -> bool:
        """Kick a player from the server."""
        try:
            self.send_command(f"clientkick {player_id}")
            self.logger.info(f"Kicked player {player_id}")
            return True
        except Exception as e:
            self.logger.error(f"Error kicking player {player_id}: {e}")
            return False

    def broadcast_message(self, message: str) -> bool:
        """Send message to all players."""
        try:
            self.send_command(f"say {message}")
            return True
        except Exception as e:
            self.logger.error(f"Error broadcasting message: {e}")
            return False

    def parse_status_response(self, response: str) -> List[Dict[str, Any]]:
        """Parse status command response into player list."""
        # This is typically handled by the message processor for OA
        # since status comes through stderr, not as command response
        return []

    def initialize_bot_settings(self, nplayers_threshold: int) -> bool:
        """Initialize bot-related settings."""
        try:
            if self.should_add_bots():
                self.send_command("set bot_minplayers 0")
                self.logger.info(
                    f"Bot settings initialized for {settings.bot_count} bots"
                )
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error initializing bot settings: {e}")
            return False

    def reset_bot_state(self) -> None:
        """Reset bot-related state."""
        self._bots_added = False
        self._bot_addition_in_progress = False
        self.logger.info("Bot state reset")

    def set_flaglimit(self, limit: int) -> bool:
        """Set the capturelimit for matches."""
        try:
            self.send_command(f"set fraglimit {limit}")
            self.send_command(f"say flaglimit set to {limit}")
            self.logger.info(f"Flaglimit set to {limit}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting flaglimit: {e}")
            return False

    def disable_next_round_warmup(self) -> bool:
        """Disable warmup for next round."""
        try:
            self.send_command("set g_doWarmup 0")
            self.logger.info("Warmup disabled")
            return True
        except Exception as e:
            self.logger.error(f"Error disabling warmup: {e}")
            return False

    def set_next_round_with_warmup_phase(self) -> bool:
        """Set the next round with a warmup phase."""
        try:
            self.send_command("set g_doWarmup 1")
            self.send_command(f"set g_warmup {settings.warmup_time}")
            self.logger.info("Warmup phase enabled")
            return True
        except Exception as e:
            self.logger.error(f"Error enabling warmup phase: {e}")
            return False

    def restart_map(self) -> bool:
        """Restart the current map."""
        try:
            self.send_command("map_restart")
            self.logger.info("Map restarted")
            return True
        except Exception as e:
            self.logger.error(f"Error restarting map: {e}")
            return False
