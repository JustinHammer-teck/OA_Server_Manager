import logging
import time
from enum import Enum
from typing import Callable, Optional, Dict

import core.settings as settings


class GameState(Enum):
    WAITING = 1
    WARMUP = 2
    RUNNING = 3


class GameStateManager:
    """Manages game state transitions and match progression."""
    
    def __init__(self, send_command_callback: Callable[[str], None]):
        self.current_state = GameState.WAITING
        self.round_count: int = 0
        self.warmup_round_count: int = 0
        self.max_rounds: int = len(settings.latencies) * settings.repeats
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)
        
    def should_transition_to_warmup(self, current_players: int, threshold: int) -> bool:
        """Check if we should transition from WAITING to WARMUP state."""
        return (self.current_state == GameState.WAITING and 
                current_players >= threshold)
    
    def should_transition_to_running(self) -> bool:
        """Check if we should transition from WARMUP to RUNNING state."""
        return (self.current_state == GameState.WARMUP and 
                self.warmup_round_count >= 1)
    
    def transition_to_warmup(self) -> None:
        """Transition from WAITING to WARMUP state."""
        if self.current_state != GameState.WAITING:
            self.logger.warning(f"Invalid transition to WARMUP from {self.current_state}")
            return
            
        self.current_state = GameState.WARMUP
        self.warmup_round_count = 0
        
        # Server commands for warmup phase
        self.send_command("vstr m0")  # Load first map
        self.send_command(f"timelimit {settings.warmup_timelimit}")
        self.send_command(f"say Starting warmup round: {settings.warmup_timelimit} minute(s)!")
        self.send_command(f"say Connecting to OBS instances...")
        
        self.logger.info("State changed from WAITING to WARMUP")
    
    def transition_to_running(self) -> None:
        """Transition from WARMUP to RUNNING state."""
        if self.current_state != GameState.WARMUP:
            self.logger.warning(f"Invalid transition to RUNNING from {self.current_state}")
            return
            
        self.current_state = GameState.RUNNING
        self.round_count = 0
        
        # Server commands for running phase
        self.send_command(f"set timelimit {settings.timelimit}")
        self.send_command(f"say Experiment starting! Round {self.round_count + 1}/{self.max_rounds}")
        
        self.logger.info("State changed from WARMUP to RUNNING")
    
    def handle_map_initialized(self) -> dict:
        """Handle map initialization event and determine actions needed."""
        result = {
            'state_changed': False,
            'round_completed': False,
            'experiment_finished': False,
            'actions': []
        }
        
        if self.current_state == GameState.WARMUP:
            self.warmup_round_count += 1
            if self.should_transition_to_running():
                self.transition_to_running()
                result['state_changed'] = True
                result['actions'].append('apply_latency')
        
        elif self.current_state == GameState.RUNNING:
            if self.round_count >= self.max_rounds:
                result['experiment_finished'] = True
                self.logger.info(f"Final round {self.round_count} completed.")
            else:
                self.round_count += 1
                result['round_completed'] = True
                result['actions'].append('rotate_latency')
                result['actions'].append('apply_latency')
                
                self.send_command(f"say Round {self.round_count}/{self.max_rounds}")
                self.logger.info(f"Starting round {self.round_count}")
        
        return result
    
    def handle_match_end(self) -> dict:
        """Handle match end event (fraglimit hit) and determine next actions."""
        result = {
            'state_changed': False,
            'round_completed': False,
            'experiment_finished': False,
            'actions': []
        }
        
        if self.current_state == GameState.RUNNING:
            if self.round_count >= self.max_rounds:
                # Experiment complete
                result['experiment_finished'] = True
                self.logger.info(f"Experiment completed after {self.round_count} rounds")
            else:
                # More rounds to go
                self.round_count += 1
                result['round_completed'] = True
                result['actions'].append('rotate_latency')
                result['actions'].append('restart_match')
                
                self.send_command(f"say Round {self.round_count}/{self.max_rounds} starting...")
                self.logger.info(f"Round {self.round_count} starting after fraglimit")
        
        return result
    
    def send_waiting_message(self, current_players: int, threshold: int) -> None:
        """Send waiting room message to players."""
        if self.current_state == GameState.WAITING:
            self.send_command(f"say WAITING ROOM: {current_players}/{threshold} players connected")
    
    def get_current_state(self) -> GameState:
        """Get the current game state."""
        return self.current_state
    
    def get_round_info(self) -> dict:
        """Get current round information."""
        return {
            'current_round': self.round_count,
            'max_rounds': self.max_rounds,
            'warmup_rounds': self.warmup_round_count,
            'state': self.current_state.name
        }
    
    def reset_state(self) -> None:
        """Reset the game state manager to initial state."""
        self.current_state = GameState.WAITING
        self.round_count = 0
        self.warmup_round_count = 0
        self.logger.info("Game state reset to WAITING")
    
    def is_experiment_finished(self) -> bool:
        """Check if the experiment sequence is complete."""
        return (self.current_state == GameState.RUNNING and 
                self.round_count >= self.max_rounds)
    
    def check_obs_ready(self, obs_manager, client_manager) -> bool:
        """
        Check if all human clients have OBS connected.
        
        Args:
            obs_manager: OBSManager instance to check connections
            client_manager: ClientManager instance to get human clients
            
        Returns:
            True if all human clients have OBS connected
        """
        human_ips = client_manager.get_human_clients()
        if not human_ips:
            self.logger.warning("No human clients to check OBS status")
            return False
        
        # Check if all human IPs are connected in OBS manager
        all_connected = all(
            obs_manager.is_client_connected(ip) for ip in human_ips
        )
        
        if all_connected:
            self.logger.info(f"All {len(human_ips)} human clients have OBS connected")
        else:
            connected_count = sum(1 for ip in human_ips if obs_manager.is_client_connected(ip))
            self.logger.info(f"OBS connections: {connected_count}/{len(human_ips)} ready")
        
        return all_connected
    
    def should_start_match_recording(self) -> bool:
        """Check if we should start recording for a new match."""
        return self.current_state == GameState.RUNNING
    
    def should_stop_match_recording(self) -> bool:
        """Check if we should stop recording after a match."""
        return self.current_state == GameState.RUNNING and self.round_count > 0