"""
Bot Management - Handles all bot-related operations.

Extracted from server.py to separate bot management concerns.
"""
import asyncio
import logging
from typing import List, Dict, Optional, Callable

import core.utils.settings as settings


class BotManager:
    def __init__(self, send_command_callback: Callable[[str], None]):
        """
        Initialize Bot Manager.

        Args:
            send_command_callback: Function to send commands to game server
        """
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)

        self._bots_added = False
        self._bot_config: Optional[Dict] = None
        self._bot_addition_task: Optional[asyncio.Task] = None
        self._bot_addition_in_progress = False
    
    def should_add_bots(self) -> bool:
        return settings.bot_enable and settings.bot_count > 0

    async def add_bots_to_server_async(self) -> bool:
        """
        Add bots to the server asynchronously without blocking the main thread.

        Returns:
            True if bot addition was successful, False otherwise
        """
        if self._bots_added:
            self.logger.debug("Bots already added, skipping")
            return True

        if not self.should_add_bots():
            self.logger.info("Bot addition disabled or count is 0")
            return False

        if self._bot_addition_in_progress:
            self.logger.info("Bot addition already in progress")
            return False

        self.logger.info("Starting asynchronous bot addition")
        self._bot_addition_in_progress = True
        try:
            result = await self._add_bots_async_impl()
            return result
        finally:
            self._bot_addition_in_progress = False

    async def _add_bots_async_impl(self) -> bool:
        """
        Implementation of asynchronous bot addition.

        Returns:
            True if all bots were added successfully
        """
        try:
            if self._bot_config:
                bot_count = self._bot_config["count"]
                bot_difficulty = self._bot_config["difficulty"]
                bot_names = self._bot_config["names"]
            else:
                bot_count = settings.bot_count
                bot_difficulty = settings.bot_difficulty
                bot_names = (
                    settings.bot_names
                    if settings.bot_names[0]
                    else ["Sarge", "Bones", "Slash", "Grunt", "Major", "Ranger"]
                )

            self.logger.info(f"Adding {bot_count} bots asynchronously...")
            success = await self._add_bots_async(bot_count, bot_difficulty, bot_names)

            if success:
                self._bots_added = True
                await asyncio.sleep(2)  # Non-blocking sleep
                self.logger.info("Async bot addition completed successfully")

            return success

        except asyncio.CancelledError:
            self.logger.info("Bot addition cancelled")
            return False
        except Exception as e:
            self.logger.error(f"Error in async bot addition: {e}", exc_info=True)
            return False

    async def _add_bots_async(self, num_bots: int, difficulty: int, bot_names: List[str]) -> bool:
        """
        Add bots to the server asynchronously with the specified difficulty level.

        Args:
            num_bots: Number of bots to add
            difficulty: Single difficulty level for all bots (1-5)
            bot_names: List of valid bot names

        Returns:
            True if all bots were added successfully
        """
        try:
            self.logger.info(f"Adding {num_bots} bots to the server asynchronously with difficulty {difficulty}...")

            while len(bot_names) < num_bots:
                bot_names.extend(bot_names)
            bot_names = bot_names[:num_bots]

            for i in range(num_bots):
                name = bot_names[i]

                self.logger.debug(f"Adding bot {name} with difficulty {difficulty}")
                self.send_command(f"addbot {name} {difficulty}")
                await asyncio.sleep(1)  # Non-blocking sleep between bot additions

            self.logger.info("All bots added successfully (async)")
            return True

        except asyncio.CancelledError:
            self.logger.info("Bot addition cancelled during process")
            return False
        except Exception as e:
            self.logger.error(f"Error adding bots asynchronously: {e}", exc_info=True)
            return False
    
    def initialize_bot_settings(self, nplayers_threshold: int) -> None:
        """
        Initialize bot-related server settings.
        
        Args:
            nplayers_threshold: Minimum number of human players needed
        """
        bot_enable = settings.bot_enable
        bot_count = settings.bot_count
        
        if bot_enable:
            max_clients = nplayers_threshold + bot_count
            self.logger.debug(f"Setting maximum number of clients to {max_clients}")
            self.send_command(f"set sv_maxclients {max_clients}")
            
            self.send_command("set bot_enable 1")
            self.send_command("set bot_nochat 1")
            self.send_command("set bot_minplayers 0")
        else:
            self.logger.info("Bots are disabled")
            self.send_command("set bot_enable 0")
    
    def remove_bot(self, bot_name: str) -> bool:
        """
        Remove a specific bot from the server.
        
        Args:
            bot_name: Name of the bot to remove
            
        Returns:
            True if bot was removed successfully
        """
        try:
            self.send_command(f"kick {bot_name}")
            self.logger.info(f"Removed bot: {bot_name}")
            return True
        except Exception as e:
            self.logger.error(f"Error removing bot {bot_name}: {e}")
            return False
    
    def are_bots_added(self) -> bool:
        """
        Check if bots have been added to the server.

        Returns:
            True if bots have been added
        """
        return self._bots_added

    def is_bot_addition_in_progress(self) -> bool:
        """
        Check if async bot addition is currently in progress.

        Returns:
            True if bot addition is running
        """
        return self._bot_addition_in_progress
    
    def reset_bot_state(self) -> None:
        """Reset bot state (useful for server restart)."""
        self._bots_added = False
        self._bot_addition_in_progress = False

        # Cancel any ongoing bot addition task
        if self._bot_addition_task and not self._bot_addition_task.done():
            self._bot_addition_task.cancel()
            self._bot_addition_task = None

        self.logger.info("Bot state reset")