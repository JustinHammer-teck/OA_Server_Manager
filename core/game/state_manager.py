import logging
from enum import Enum
from typing import Callable

import core.utils.settings as settings


class GameState(Enum):
    WAITING = 1
    WARMUP = 2
    RUNNING = 3


class GameStateManager:
    """Reactive game state tracking and match progression."""

    def __init__(self, send_command_callback: Callable[[str], None]):
        self.current_state = GameState.WAITING
        self.round_count: int = 0
        self.warmup_round_count: int = 0
        self.max_rounds: int = len(settings.latencies) * settings.repeats
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)
        
        self.logger.info(f"GameStateManager initialized: latencies={settings.latencies}, repeats={settings.repeats}, max_rounds={self.max_rounds}")

    def handle_warmup_detected(self) -> dict:
        """React to server warmup message - purely reactive state tracking."""
        result = {
            "state_changed": False,
            "actions": [],
        }

        if self.current_state == GameState.WAITING:
            self.current_state = GameState.WARMUP
            self.warmup_round_count = 0
            result["state_changed"] = True
            self.logger.info("State tracked: WAITING -> WARMUP")
        elif self.current_state == GameState.WARMUP:
            self.warmup_round_count += 1
            self.logger.info(f"Warmup restarted (round {self.warmup_round_count})")
        else:
            self.logger.warning(f"Unexpected warmup from state {self.current_state}")

        return result

    def handle_match_start_detected(self) -> dict:
        """React to server match start - purely reactive state tracking."""
        result = {
            "state_changed": False,
            "actions": [],
        }

        if self.current_state == GameState.WARMUP:
            self.current_state = GameState.RUNNING
            result["state_changed"] = True
            result["actions"].extend(["start_match_recording", "apply_latency"])
            self.logger.info(f"State tracked: WARMUP -> RUNNING (starting round {self.round_count + 1})")
        else:
            self.logger.warning(f"Unexpected match start from state {self.current_state}")

        return result

    def handle_fraglimit_detected(self) -> dict:
        """React to fraglimit hit - prepare for next round or experiment end."""
        result = {
            "state_changed": False,
            "round_completed": False,
            "experiment_finished": False,
            "actions": [],
        }

        if self.current_state == GameState.RUNNING:
            self.round_count += 1
            
            if self.round_count >= self.max_rounds:
                result["experiment_finished"] = True
                self.logger.info(
                    f"Experiment completed after {self.round_count} rounds (max: {self.max_rounds})"
                )
            else:
                result["round_completed"] = True
                result["actions"].extend(["rotate_latency", "restart_match"])
                self.logger.info(f"Round {self.round_count} completed, preparing round {self.round_count + 1} (max: {self.max_rounds})")

        return result

    def handle_match_end_detected(self) -> dict:
        """React to match completely ending - prepare for next round."""
        result = {
            "round_completed": False,
            "experiment_finished": False,
            "actions": [],
        }

        if self.current_state == GameState.RUNNING:
            self.round_count += 1
            
            if self.round_count > self.max_rounds:
                result["experiment_finished"] = True
                self.logger.info(f"Experiment finished after {self.round_count - 1} rounds")
            else:
                result["round_completed"] = True
                result["actions"].extend(["rotate_latency", "restart_match"])
                self.logger.info(f"Match ended, starting round {self.round_count}")

        return result

    def get_current_state(self) -> GameState:
        """Get the current game state."""
        return self.current_state

    def get_round_info(self) -> dict:
        """Get current round information."""
        if self.current_state == GameState.RUNNING:
            current_round = self.round_count + 1  # Round in progress
        else:
            current_round = self.round_count  # Completed rounds
            
        return {
            "current_round": current_round,
            "max_rounds": self.max_rounds,
            "warmup_rounds": self.warmup_round_count,
            "state": self.current_state.name,
        }

    def is_experiment_finished(self) -> bool:
        """Check if the experiment sequence is complete."""
        return (
            self.current_state == GameState.RUNNING
            and self.round_count >= self.max_rounds
        )

    def get_obs_status(self, obs_manager, client_manager) -> dict:
        """Get OBS connection status for all human clients."""
        human_ips = client_manager.get_human_clients()
        if not human_ips:
            return {"connected": 0, "total": 0, "all_connected": False}

        connected_count = sum(
            1 for ip in human_ips if obs_manager.is_client_connected(ip)
        )
        all_connected = connected_count == len(human_ips)

        self.logger.info(
            f"OBS status: {connected_count}/{len(human_ips)} connected"
        )

        return {
            "connected": connected_count,
            "total": len(human_ips),
            "all_connected": all_connected,
        }

    def should_start_warmup(self, client_manager, obs_manager) -> bool:
        """Check if warmup should start based on player count and OBS connections."""
        if self.current_state != GameState.WAITING:
            return False

        human_count = client_manager.get_human_count()
        obs_status = self.get_obs_status(obs_manager, client_manager)

        # Start warmup if we don't have enough human players OR not all OBS connected
        if human_count < settings.nplayers_threshold or (human_count > 0 and not obs_status["all_connected"]):
            return True

        return False