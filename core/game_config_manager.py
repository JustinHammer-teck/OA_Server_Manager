"""
Game Configuration Manager - Handles OpenArena game settings.

Extracted from server.py to separate game configuration concerns.
"""
import logging
from typing import Callable, Dict, Any

import core.settings as settings


class GameConfigManager:
    """
    Manages OpenArena game configuration settings.
    
    Handles capturelimit, warmup settings, time limits, and other
    game-specific configuration options.
    """
    
    def __init__(self, send_command_callback: Callable[[str], None]):
        """
        Initialize Game Configuration Manager.
        
        Args:
            send_command_callback: Function to send commands to game server
        """
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)
        
        # Track current configuration
        self._current_config = {}
    
    def set_flaglimit(self, limit: int) -> bool:
        """
        Set the capturelimit (fraglimit) for matches.
        
        Args:
            limit: Number of frags/captures to end the match
            
        Returns:
            True if setting was applied successfully
        """
        try:
            self.send_command(f"set flaglimit {limit}")
            self.send_command(f"say flaglimit set to {limit}")
            self._current_config["flaglimit"] = limit
            self.logger.info(f"Flaglimit set to {limit}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting flaglimit: {e}")
            return False
    
    def set_timelimit(self, minutes: int) -> bool:
        """
        Set the time limit for matches.
        
        Args:
            minutes: Time limit in minutes
            
        Returns:
            True if setting was applied successfully
        """
        try:
            self.send_command(f"timelimit {minutes}")
            self.send_command(f"say Timelimit set to {minutes} minutes")
            self._current_config["timelimit"] = minutes
            self.logger.info(f"Timelimit set to {minutes} minutes")
            return True
        except Exception as e:
            self.logger.error(f"Error setting timelimit: {e}")
            return False
    
    def set_warmup_time(self, seconds: int) -> bool:
        """
        Set warmup duration in seconds.
        
        Args:
            seconds: Warmup duration in seconds
            
        Returns:
            True if setting was applied successfully
        """
        try:
            self.send_command(f"set g_warmup {seconds}")
            self.send_command(f"say Warmup time set to {seconds} seconds")
            self._current_config["warmup_time"] = seconds
            self.logger.info(f"Warmup time set to {seconds} seconds")
            return True
        except Exception as e:
            self.logger.error(f"Error setting warmup time: {e}")
            return False
    
    def enable_warmup(self, enable: bool = True) -> bool:
        """
        Enable or disable warmup mode.
        
        Args:
            enable: True to enable warmup, False to disable
            
        Returns:
            True if setting was applied successfully
        """
        try:
            value = "1" if enable else "0"
            self.send_command(f"set g_dowarmup {value}")
            status = "enabled" if enable else "disabled"
            self.send_command(f"say Warmup {status}")
            self._current_config["warmup_enabled"] = enable
            self.logger.info(f"Warmup {status}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting warmup mode: {e}")
            return False
    
    def set_fraglimit(self, limit: int) -> bool:
        """
        Set the fraglimit for matches.
        
        Args:
            limit: Number of frags to end the match
            
        Returns:
            True if setting was applied successfully
        """
        try:
            self.send_command(f"fraglimit {limit}")
            self.send_command(f"say Fraglimit set to {limit}")
            self._current_config["fraglimit"] = limit
            self.logger.info(f"Fraglimit set to {limit}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting fraglimit: {e}")
            return False
    
    def set_game_type(self, gametype: int) -> bool:
        """
        Set the game type.
        
        Args:
            gametype: Game type (0=FFA, 1=Tournament, 3=Team DM, 4=CTF)
            
        Returns:
            True if setting was applied successfully
        """
        game_types = {
            0: "Free For All",
            1: "Tournament", 
            3: "Team Deathmatch",
            4: "Capture The Flag"
        }
        
        try:
            self.send_command(f"g_gametype {gametype}")
            game_name = game_types.get(gametype, f"Type {gametype}")
            self.send_command(f"say Game type set to: {game_name}")
            self._current_config["gametype"] = gametype
            self.logger.info(f"Game type set to: {game_name} ({gametype})")
            return True
        except Exception as e:
            self.logger.error(f"Error setting game type: {e}")
            return False
    
    def set_max_clients(self, max_clients: int) -> bool:
        """
        Set maximum number of clients that can connect.
        
        Args:
            max_clients: Maximum client count
            
        Returns:
            True if setting was applied successfully
        """
        try:
            self.send_command(f"set sv_maxclients {max_clients}")
            self._current_config["max_clients"] = max_clients
            self.logger.info(f"Max clients set to {max_clients}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting max clients: {e}")
            return False
    
    def restart_map(self) -> bool:
        """
        Restart the current map.
        
        Returns:
            True if restart was successful
        """
        try:
            self.send_command("map_restart")
            self.send_command("say Map restarted!")
            self.logger.info("Map restarted")
            return True
        except Exception as e:
            self.logger.error(f"Error restarting map: {e}")
            return False
    
    def change_map(self, map_name: str) -> bool:
        """
        Change to a different map.
        
        Args:
            map_name: Name of the map to load (e.g., "q3dm17")
            
        Returns:
            True if map change was successful
        """
        try:
            self.send_command(f"map {map_name}")
            self.send_command(f"say Changing to map: {map_name}")
            self._current_config["current_map"] = map_name
            self.logger.info(f"Changing to map: {map_name}")
            return True
        except Exception as e:
            self.logger.error(f"Error changing map: {e}")
            return False
    
    def apply_default_config(self) -> bool:
        """
        Apply default game configuration from settings.
        
        Returns:
            True if all settings were applied successfully
        """
        try:
            success = True
            
            # Apply capture limit
            if hasattr(settings, 'flaglimit'):
                success &= self.set_flaglimit(settings.flaglimit)
            
            # Apply warmup settings
            if hasattr(settings, 'warmup_time'):
                success &= self.set_warmup_time(settings.warmup_time)
            
            if hasattr(settings, 'enable_warmup'):
                success &= self.enable_warmup(settings.enable_warmup)
            
            self.logger.info("Applied default game configuration from settings")
            return success
            
        except Exception as e:
            self.logger.error(f"Error applying default config: {e}")
            return False
    
    def apply_startup_config(self) -> Dict[str, str]:
        """
        Get startup configuration arguments for server launch.
        
        Returns:
            Dictionary of configuration arguments for server startup
        """
        config_args = {}
        
        try:
            # Add capture limit
            if hasattr(settings, 'flaglimit'):
                config_args["flaglimit"] = str(settings.flaglimit)
            
            # Add warmup settings
            if hasattr(settings, 'warmup_time'):
                config_args["g_warmup"] = str(settings.warmup_time)
            
            if hasattr(settings, 'enable_warmup'):
                config_args["g_dowarmup"] = "1" if settings.enable_warmup else "0"
            
            return config_args
            
        except Exception as e:
            self.logger.error(f"Error generating startup config: {e}")
            return {}
    
    def get_current_config(self) -> Dict[str, Any]:
        """
        Get current game configuration.
        
        Returns:
            Dictionary of current configuration settings
        """
        return self._current_config.copy()
    
    def freeze_game(self, seconds: int = 5) -> bool:
        """
        Freeze the game for specified seconds.
        
        Args:
            seconds: Number of seconds to freeze
            
        Returns:
            True if freeze was successful
        """
        try:
            self.send_command(f"freeze {seconds}")
            self.send_command(f"say Game frozen for {seconds} seconds")
            self.logger.info(f"Game frozen for {seconds} seconds")
            return True
        except Exception as e:
            self.logger.error(f"Error freezing game: {e}")
            return False
    
    def enable_cheats(self) -> bool:
        """
        Enable cheats on the server (for development/testing).
        
        Returns:
            True if cheats were enabled successfully
        """
        try:
            self.send_command("devmap")  # Loads current map with cheats
            self.send_command("say Cheats enabled for testing")
            self.logger.info("Cheats enabled")
            return True
        except Exception as e:
            self.logger.error(f"Error enabling cheats: {e}")
            return False