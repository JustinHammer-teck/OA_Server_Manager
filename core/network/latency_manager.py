"""
Latency Management - Handles network latency simulation and rotation.

Extracted from server.py to separate network latency concerns.
"""
import logging
from typing import Dict, List, Callable, Optional

import core.utils.settings as settings
from core.network.network_utils import NetworkUtils


class LatencyManager:
    """
    Manages network latency simulation and rotation for experiments.
    
    Handles latency rule application, rotation strategies, and 
    integration with client management.
    """
    
    def __init__(self, interface: str = "enp1s0", send_command_callback: Optional[Callable[[str], None]] = None):
        """
        Initialize Latency Manager.
        
        Args:
            interface: Network interface for traffic control
            send_command_callback: Function to send commands to game server
        """
        self.interface = interface
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)
        
        # Current latency configuration
        self._current_latencies = list(settings.latencies)
        self._round_count = 0
        self._enabled = settings.enable_latency_control
    
    def set_interface(self, interface: str) -> None:
        """
        Set the network interface for latency control.
        
        Args:
            interface: Network interface name (e.g., "enp1s0")
        """
        self.interface = interface
        self.logger.info(f"Network interface set to: {interface}")
    
    def apply_latency_rules(self, client_manager) -> bool:
        """
        Apply current latency rules to all connected clients.
        
        Args:
            client_manager: ClientManager instance containing IP to latency mapping
            
        Returns:
            True if latency rules were applied successfully
        """
        if not self._enabled:
            self.logger.info("Latency control is disabled, skipping latency application")
            if self.send_command:
                self.send_command("say Latency control disabled")
            return True
            
        try:
            latency_map = client_manager.get_latency_map()
            if not latency_map:
                self.logger.warning("No clients available for latency application")
                return False
            
            NetworkUtils.apply_latency_rules(latency_map, self.interface)
            
            self.logger.info(f"Applied latency rules to {len(latency_map)} clients on interface {self.interface}")
            
            # Notify players
            if self.send_command:
                self.send_command(f"say Latency rules applied to {len(latency_map)} clients")
            
            # Log current latency mapping
            for ip, latency in latency_map.items():
                self.logger.debug(f"Client {ip}: {latency}ms latency")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error applying latency rules: {e}", exc_info=True)
            return False
    
    def rotate_latencies(self, client_manager) -> bool:
        """
        Rotate latency assignments for the next round.
        
        Args:
            client_manager: ClientManager instance to update latency assignments
            
        Returns:
            True if latencies were rotated successfully
        """
        if not self._enabled:
            self.logger.info("Latency control is disabled, skipping latency rotation")
            return True
            
        try:
            self._current_latencies = self._current_latencies[1:] + self._current_latencies[:1]
            self._round_count += 1
            
            client_manager.assign_latencies(self._current_latencies)
            
            self.logger.info(f"Round {self._round_count}: Rotated latencies to {self._current_latencies}")
            
            if self.send_command:
                latency_str = ", ".join(f"{lat}ms" for lat in self._current_latencies)
                self.send_command(f"say Round {self._round_count}: New latencies - {latency_str}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error rotating latencies: {e}", exc_info=True)
            return False
    
    def apply_specific_latencies(self, latency_map: Dict[str, int]) -> bool:
        """
        Apply specific latency values to clients.
        
        Args:
            latency_map: Dictionary mapping client IPs to latency values in ms
            
        Returns:
            True if latencies were applied successfully
        """
        if not self._enabled:
            self.logger.info("Latency control is disabled, skipping specific latency application")
            return True
            
        try:
            if not latency_map:
                self.logger.warning("Empty latency map provided")
                return False
            
            NetworkUtils.apply_latency_rules(latency_map, self.interface)
            
            self.logger.info(f"Applied specific latency rules to {len(latency_map)} clients")
            
            for ip, latency in latency_map.items():
                self.logger.info(f"Applied {latency}ms latency to client {ip}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error applying specific latencies: {e}", exc_info=True)
            return False
    
    def clear_latency_rules(self) -> bool:
        """
        Clear all latency rules from the network interface.
        
        Returns:
            True if rules were cleared successfully
        """
        try:
            NetworkUtils.dispose(self.interface)
            self.logger.info("Cleared all latency rules from network interface")
            
            if self.send_command:
                self.send_command("say Network latency rules cleared")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error clearing latency rules: {e}", exc_info=True)
            return False
    
    def get_current_latencies(self) -> List[int]:
        """
        Get current latency configuration.
        
        Returns:
            List of current latency values in ms
        """
        return self._current_latencies.copy()
    
    def set_latency_configuration(self, latencies: List[int]) -> bool:
        """
        Set a new latency configuration.
        
        Args:
            latencies: List of latency values in milliseconds
            
        Returns:
            True if configuration was set successfully
        """
        try:
            if not latencies:
                self.logger.error("Empty latency list provided")
                return False
            
            # Validate latency values
            for latency in latencies:
                if not isinstance(latency, int) or latency < 0:
                    self.logger.error(f"Invalid latency value: {latency}")
                    return False
            
            self._current_latencies = list(latencies)
            self._round_count = 0
            
            self.logger.info(f"Set new latency configuration: {self._current_latencies}")
            
            if self.send_command:
                latency_str = ", ".join(f"{lat}ms" for lat in latencies)
                self.send_command(f"say New latency configuration: {latency_str}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error setting latency configuration: {e}")
            return False
    
    def get_round_count(self) -> int:
        """
        Get current round count for latency rotation.
        
        Returns:
            Current round number
        """
        return self._round_count
    
    def reset_rotation(self) -> None:
        """Reset latency rotation to initial state."""
        self._current_latencies = list(settings.latencies)
        self._round_count = 0
        self.logger.info("Reset latency rotation to initial state")
    
    def shuffle_latencies(self, client_manager) -> bool:
        """
        Randomly shuffle latency assignments.
        
        Args:
            client_manager: ClientManager instance to update latency assignments
            
        Returns:
            True if latencies were shuffled successfully
        """
        try:
            import random
            
            # Shuffle the current latencies
            shuffled_latencies = self._current_latencies.copy()
            random.shuffle(shuffled_latencies)
            
            self._current_latencies = shuffled_latencies
            
            # Update client manager with shuffled assignments
            client_manager.assign_latencies(self._current_latencies)
            
            self.logger.info(f"Shuffled latencies to: {self._current_latencies}")
            
            if self.send_command:
                latency_str = ", ".join(f"{lat}ms" for lat in shuffled_latencies)
                self.send_command(f"say Latencies shuffled: {latency_str}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error shuffling latencies: {e}")
            return False
    
    def apply_per_client_latency(self, client_ip: str, latency: int) -> bool:
        """
        Apply latency to a specific client.
        
        Args:
            client_ip: IP address of the client
            latency: Latency value in milliseconds
            
        Returns:
            True if latency was applied successfully
        """
        try:
            latency_map = {client_ip: latency}
            success = self.apply_specific_latencies(latency_map)
            
            if success:
                self.logger.info(f"Applied {latency}ms latency to client {client_ip}")
                
                if self.send_command:
                    self.send_command(f"say Applied {latency}ms latency to client {client_ip}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error applying latency to client {client_ip}: {e}")
            return False
    
    def get_interface(self) -> str:
        """
        Get current network interface.
        
        Returns:
            Current network interface name
        """
        return self.interface
    
    def is_enabled(self) -> bool:
        """
        Check if latency control is enabled.
        
        Returns:
            True if latency control is enabled
        """
        return self._enabled
    
    def enable_latency_control(self) -> None:
        """Enable latency control."""
        self._enabled = True
        self.logger.info("Latency control enabled")
        if self.send_command:
            self.send_command("say Latency control enabled")
    
    def disable_latency_control(self) -> None:
        """Disable latency control and clear existing rules."""
        self._enabled = False
        self.logger.info("Latency control disabled")
        
        # Clear existing latency rules when disabling
        try:
            self.clear_latency_rules()
        except Exception as e:
            self.logger.warning(f"Failed to clear latency rules when disabling: {e}")
        
        if self.send_command:
            self.send_command("say Latency control disabled")
    
    def set_enabled(self, enabled: bool) -> None:
        """
        Set latency control enabled/disabled state.
        
        Args:
            enabled: True to enable, False to disable latency control
        """
        if enabled:
            self.enable_latency_control()
        else:
            self.disable_latency_control()
    
    def validate_interface(self) -> bool:
        """
        Validate that the current network interface exists and is usable.
        
        Returns:
            True if interface is valid
        """
        try:
            import subprocess
            
            # Check if interface exists
            result = subprocess.run(
                ["ip", "link", "show", self.interface],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                self.logger.info(f"Network interface {self.interface} is valid")
                return True
            else:
                self.logger.error(f"Network interface {self.interface} not found")
                return False
                
        except Exception as e:
            self.logger.error(f"Error validating interface: {e}")
            return False