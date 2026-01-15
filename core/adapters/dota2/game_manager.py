"""Dota 2-specific game management."""

import asyncio
import logging
from typing import Any, Callable, Dict, List

from core.adapters.base import BaseGameManager


class Dota2GameManager(BaseGameManager):
    """
    Dota 2-specific game management.

    Handles Dota 2-specific console commands and game configuration.
    Note that Dota 2 has different concepts than arena shooters:
    - No traditional "bots" - AI players are part of game mode settings
    - Game modes (All Pick, Captain's Mode, etc.)
    - Match settings are typically preconfigured

    Common Dota 2 console commands:
    - status: Show server and player info
    - say: Send chat message
    - kick: Kick player
    - dota_create_unit: Create bot unit
    - sv_cheats: Enable cheats
    - host_timescale: Adjust game speed
    """

    def __init__(self, send_command_callback: Callable[[str], None]):
        super().__init__(send_command_callback)
        self.logger = logging.getLogger(__name__)

        self._config_applied = False
        self._bots_added = False

    def apply_startup_config(self) -> Dict[str, str]:
        """
        Get startup configuration for Dota 2 server.

        Note: Most Dota 2 server configuration is done via
        server.cfg or launch parameters, not runtime commands.
        """
        return {
            # Dota 2 specific cvars would go here
            # Most settings are in server.cfg
        }

    def apply_default_config(self) -> bool:
        """
        Apply default game configuration.

        Dota 2 server configuration is typically done through
        the server.cfg file. This method sends any runtime
        configuration commands needed.
        """
        try:
            # Example runtime config - adjust as needed
            # self.send_command("sv_cheats 1")  # If cheats needed for testing
            self._config_applied = True
            self.logger.info("Dota 2 configuration applied")
            return True
        except Exception as e:
            self.logger.error(f"Error applying Dota 2 config: {e}")
            return False

    async def add_bots(self, count: int, difficulty: int = 1) -> bool:
        """
        Add bots to Dota 2 game.

        Dota 2 bot commands differ significantly from arena shooters.
        Common approaches:
        - dota_bot_populate: Auto-fill teams with bots
        - dota_create_unit: Create specific bot units

        Args:
            count: Number of bots to add
            difficulty: Bot difficulty (not used in same way as OA)

        Returns:
            True if bots were added successfully.
        """
        if self._bots_added:
            self.logger.debug("Bots already added, skipping")
            return True

        try:
            self.logger.info(f"Adding {count} bots to Dota 2 game")

            # Use dota_bot_populate for automatic bot filling
            # This fills empty slots with bots
            self.send_command("dota_bot_populate")

            await asyncio.sleep(1.0)

            self._bots_added = True
            self.logger.info("Dota 2 bots added")
            return True

        except Exception as e:
            self.logger.error(f"Error adding Dota 2 bots: {e}")
            return False

    def kick_player(self, player_id: Any) -> bool:
        """
        Kick a player from the Dota 2 server.

        Args:
            player_id: Player's userid or steamid

        Returns:
            True if kick command was sent.
        """
        try:
            self.send_command(f"kick {player_id}")
            self.logger.info(f"Kicked player {player_id}")
            return True
        except Exception as e:
            self.logger.error(f"Error kicking player {player_id}: {e}")
            return False

    def kick_by_steamid(self, steamid: str) -> bool:
        """Kick a player by their Steam ID."""
        try:
            self.send_command(f"kickid {steamid}")
            self.logger.info(f"Kicked player with SteamID {steamid}")
            return True
        except Exception as e:
            self.logger.error(f"Error kicking SteamID {steamid}: {e}")
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
        """
        Parse status command response into player list.

        This is typically handled by the message processor,
        but provided here for direct RCON response parsing.
        """
        players = []
        lines = response.strip().split("\n")

        in_player_section = False
        for line in lines:
            if "userid" in line and "name" in line:
                in_player_section = True
                continue

            if in_player_section and line.strip():
                player = self._parse_player_line(line)
                if player:
                    players.append(player)

        return players

    def _parse_player_line(self, line: str) -> Dict[str, Any]:
        """Parse a single player line from status output."""
        parts = line.split()
        if len(parts) < 4:
            return {}

        try:
            return {
                "userid": parts[0].lstrip("#"),
                "name": parts[1],
                "steamid": parts[2] if len(parts) > 2 else "",
                "connected": parts[3] if len(parts) > 3 else "",
                "ping": int(parts[4]) if len(parts) > 4 and parts[4].isdigit() else 0,
            }
        except (ValueError, IndexError):
            return {}

    def pause_game(self) -> bool:
        """Pause the game."""
        try:
            self.send_command("dota_pause")
            self.logger.info("Game paused")
            return True
        except Exception as e:
            self.logger.error(f"Error pausing game: {e}")
            return False

    def unpause_game(self) -> bool:
        """Unpause the game."""
        try:
            self.send_command("dota_unpause")
            self.logger.info("Game unpaused")
            return True
        except Exception as e:
            self.logger.error(f"Error unpausing game: {e}")
            return False

    def restart_game(self) -> bool:
        """Restart the current game."""
        try:
            self.send_command("dota_force_gamemode 1")  # Reset to All Pick
            self.send_command("dota_start_ai_game 1")   # Start new game
            self.logger.info("Game restarted")
            return True
        except Exception as e:
            self.logger.error(f"Error restarting game: {e}")
            return False

    def set_game_mode(self, mode: int) -> bool:
        """
        Set the game mode.

        Common modes:
        1 = All Pick
        2 = Captain's Mode
        3 = Random Draft
        4 = Single Draft
        5 = All Random
        """
        try:
            self.send_command(f"dota_force_gamemode {mode}")
            self.logger.info(f"Game mode set to {mode}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting game mode: {e}")
            return False

    def enable_cheats(self) -> bool:
        """Enable cheats on the server."""
        try:
            self.send_command("sv_cheats 1")
            self.logger.info("Cheats enabled")
            return True
        except Exception as e:
            self.logger.error(f"Error enabling cheats: {e}")
            return False

    def set_timescale(self, scale: float) -> bool:
        """Set game time scale (requires sv_cheats)."""
        try:
            self.send_command(f"host_timescale {scale}")
            self.logger.info(f"Timescale set to {scale}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting timescale: {e}")
            return False
