"""
Game Configuration Manager - Handles OpenArena game settings.

Extracted from server.py to separate game configuration concerns.
"""
import logging
from typing import Callable, Dict, Any

import core.utils.settings as settings


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
                config_args["g_doWarmup"] = "1" if settings.enable_warmup else "0"
            
            return config_args
            
        except Exception as e:
            self.logger.error(f"Error generating startup config: {e}")
            return {}

    def start_warmup_phase(self) -> bool:
        """
        Start warmup phase by enabling warmup and restarting map.

        Returns:
            True if warmup was started successfully
        """
        try:
            self.send_command(f"set g_warmup {settings.warmup_time}")
            self.send_command("set g_doWarmup 1")
            self.send_command(f"say Starting {settings.warmup_time}s warmup - waiting for all players and OBS connections")
            self.logger.info(f"Started warmup phase ({settings.warmup_time}s)")
            return True
        except Exception as e:
            self.logger.error(f"Error starting warmup phase: {e}")
            return False

    def restart_warmup(self) -> bool:
        """
        Restart warmup with fresh timer when conditions aren't met.

        Returns:
            True if warmup was restarted successfully
        """
        try:
            self.send_command(f"set g_warmup {settings.warmup_time}")
            self.send_command("set g_doWarmup 1")
            self.logger.info(f"Restarted warmup with {settings.warmup_time}s timer")
            return True
        except Exception as e:
            self.logger.error(f"Error restarting warmup: {e}")
            return False