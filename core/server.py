"""
Refactored Server - Core OpenArena server process management.

This refactored version focuses only on core server responsibilities:
- Server process lifecycle management
- Command sending and message reading
- Message processing coordination
- Component orchestration

All specialized logic has been extracted to dedicated managers.
"""

import asyncio
import logging
import subprocess
import time
from subprocess import PIPE, Popen
from typing import Optional

import core.settings as settings
from core.bot_manager import BotManager
from core.client_manager import ClientManager
from core.display_utils import DisplayUtils
from core.game_config_manager import GameConfigManager
from core.game_state_manager import GameStateManager
from core.latency_manager import LatencyManager
from core.message_processor import MessageProcessor, MessageType
from core.obs_connection_manager import OBSConnectionManager


class Server:
    """
    Refactored OpenArena server management with separated concerns.

    This class now focuses solely on:
    - Server process management
    - Message processing coordination
    - Component integration
    """

    def __init__(self):
        """Initialize server with all specialized managers."""
        self.logger = logging.getLogger(__name__)
        self.nplayers_threshold = settings.nplayers_threshold

        self._process: Optional[Popen] = None
        self._async_loop: Optional[asyncio.AbstractEventLoop] = None

        self.client_manager = ClientManager()
        self.game_state_manager = GameStateManager(self.send_command)
        self.message_processor = MessageProcessor(self.send_command)
        self.display_utils = DisplayUtils()

        self._init_specialized_managers()

    def _init_specialized_managers(self):
        """Initialize all specialized management components."""
        # OBS Connection Manager
        obs_port = int(settings.obs_port) if hasattr(settings, "obs_port") else 4455
        obs_password = (
            settings.obs_password if hasattr(settings, "obs_password") else None
        )
        obs_timeout = (
            int(settings.obs_connection_timeout)
            if hasattr(settings, "obs_connection_timeout")
            else 30
        )

        self.obs_connection_manager = OBSConnectionManager(
            obs_port=obs_port,
            obs_password=obs_password,
            obs_timeout=obs_timeout,
            send_command_callback=self.send_command,
        )

        # Bot Manager
        self.bot_manager = BotManager(send_command_callback=self.send_command)

        # Game Configuration Manager
        self.game_config_manager = GameConfigManager(
            send_command_callback=self.send_command
        )

        # Latency Manager (default interface, will be configured later)
        self.latency_manager = LatencyManager(
            interface="enp1s0", send_command_callback=self.send_command
        )

    # =============================================================================
    # Core Server Process Management
    # =============================================================================

    def start_server(self):
        """Start the OpenArena dedicated server process."""
        self.logger.info("Starting OpenArena server process")

        # Get startup configuration from game config manager
        startup_config = self.game_config_manager.apply_startup_config()

        # Build server arguments
        server_args = [
            "oa_ded",
            "+set",
            "dedicated",
            "1",
            "+set",
            "net_port",
            "27960",
            "+set",
            "com_legacyprotocol",
            "71",
            "+set",
            "com_protocol",
            "71",
            "+set",
            "sv_master1",
            "dpmaster.deathmask.net",
            "+set",
            "cl_motd",
            "Welcome To ASTRID lab",
        ]

        for key, value in startup_config.items():
            server_args.extend(["+set", key, value])

        server_args.extend(["+exec", "t_server.cfg"])

        self._process = Popen(
            server_args,
            stdout=PIPE,
            stdin=PIPE,
            stderr=PIPE,
            universal_newlines=False,
        )

        self._initialize_server()

    def _initialize_server(self):
        """Initialize server with bot and game settings."""
        self.bot_manager.initialize_bot_settings(self.nplayers_threshold)

        self.game_config_manager.apply_default_config()

    def send_command(self, command: str):
        """Send a command to the server's stdin."""
        if self._process and self._process.poll() is None:
            self.logger.debug(f"CMD_SEND: {command}")
            self._process.stdin.write(f"{command}\r\n".encode())
            self._process.stdin.flush()

    def read_server(self) -> str:
        """Read a message from the server's stderr."""
        return (
            self._process.stderr.readline().decode("utf-8", errors="replace").rstrip()
        )

    def dispose(self):
        """Shut down the server process gracefully."""
        if self._process and self._process.poll() is None:
            self._process.terminate()
            try:
                self._process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.logger.error(
                    f"Cannot properly terminate process {self._process.pid}"
                )
                self._process.kill()
                self._process.wait()

        self.logger.info("Server process disposed successfully")

    def configure_bots(self, bot_config):
        """Configure bot settings from command line arguments."""
        self.bot_manager.configure_bots(bot_config)
        self.logger.info(f"Bot configuration updated: {bot_config}")

    def configure_interface(self, interface: str):
        """Configure network interface for latency control."""
        self.latency_manager.set_interface(interface)
        self.logger.info(f"Network interface set to: {interface}")

    def set_async_loop(self, loop: asyncio.AbstractEventLoop):
        """Set the async event loop for OBS operations."""
        self._async_loop = loop
        self.logger.debug("Async event loop set for OBS operations")

    def process_server_message(self, raw_message: str):
        """Process a server message and coordinate responses."""
        parsed_message = self.message_processor.process_message(raw_message)

        # Dispatch to appropriate handlers
        if parsed_message.message_type == MessageType.CLIENT_CONNECTING:
            self._handle_client_connecting(parsed_message)
        elif parsed_message.message_type == MessageType.CLIENT_DISCONNECT:
            self._handle_client_disconnect(parsed_message)
        elif parsed_message.message_type == MessageType.MAP_INITIALIZED:
            self._handle_map_initialized(parsed_message)
        elif parsed_message.message_type == MessageType.MATCH_END_FRAGLIMIT:
            self._handle_match_end_fraglimit(parsed_message)
        elif parsed_message.message_type == MessageType.STATUS_LINE:
            self._handle_status_line(parsed_message)

    def _handle_client_connecting(self, parsed_message):
        """Handle client connection event."""
        client_id = parsed_message.data["client_id"]
        self.logger.info(f"Processing client {client_id} connection")
        # Status parsing handled by subsequent STATUS_LINE messages

    def _handle_client_disconnect(self, parsed_message):
        """Handle client disconnection event."""
        client_id = parsed_message.data["client_id"]
        client_ip = self.client_manager.get_client_ip(client_id)

        # Disconnect OBS if client had connection
        if client_ip and self.obs_connection_manager.is_client_connected(client_ip):
            if self._async_loop:
                self._async_loop.create_task(
                    self.obs_connection_manager.disconnect_client(client_ip)
                )

        # Remove from client manager
        self.client_manager.remove_client(client_id)

        # Update game state and display
        current_players = self.client_manager.get_client_count()
        self.logger.info(
            f"Client {client_id} disconnected. Current players: {current_players}"
        )

        if self.game_state_manager.get_current_state().name == "WAITING":
            self.game_state_manager.send_waiting_message(
                current_players, self.nplayers_threshold
            )

        if current_players > 0:
            self.display_utils.display_client_table(
                self.client_manager, "CLIENT STATUS AFTER DISCONNECTION"
            )

    def _handle_map_initialized(self, parsed_message):
        """Handle map initialization event."""
        self.logger.info("Map initialized - processing state transitions")

        if not self.bot_manager.are_bots_added() and self.bot_manager.should_add_bots():
            self.bot_manager.add_bots_to_server()

        result = self.game_state_manager.handle_map_initialized()

        if result.get("experiment_finished"):
            self.logger.info("Experiment sequence completed!")
            if self._async_loop:
                self._async_loop.create_task(
                    self.obs_connection_manager.stop_match_recording(
                        self.game_state_manager
                    )
                )
            return

        if self.game_state_manager.should_start_match_recording():
            if self._async_loop:
                self._async_loop.create_task(
                    self.obs_connection_manager.start_match_recording(
                        self.game_state_manager
                    )
                )

        if "apply_latency" in result.get("actions", []):
            self.latency_manager.apply_latency_rules(self.client_manager)

        if "rotate_latency" in result.get("actions", []):
            self.latency_manager.rotate_latencies(self.client_manager)

    def _handle_match_end_fraglimit(self, parsed_message):
        """Handle match end due to fraglimit hit."""
        self.logger.info("Match ended - Fraglimit hit! Stopping OBS recordings...")

        if self._async_loop:
            self._async_loop.create_task(
                self.obs_connection_manager.stop_match_recording(
                    self.game_state_manager
                )
            )

        self.send_command("say Match ended! Recordings stopped.")

        result = self.game_state_manager.handle_match_end()

        if result and "actions" in result:
            actions = result["actions"]

            if "rotate_latency" in actions:
                self.latency_manager.rotate_latencies(self.client_manager)
                self.logger.info("Latency rotated for next match")

            if "restart_match" in actions:
                time.sleep(2)  # Brief delay
                self.game_config_manager.restart_map()
                self.logger.info("Match restarted")

    def _handle_status_line(self, parsed_message):
        """Handle server status output."""
        if parsed_message.data.get("status_complete"):
            client_ips = parsed_message.data.get("client_ips", [])
            self._process_discovered_clients(client_ips)
        elif parsed_message.data.get("client_ip"):
            client_ip = parsed_message.data["client_ip"]
            self.logger.debug(f"Discovered client IP: {client_ip}")

    def _process_discovered_clients(self, client_ips):
        """Process newly discovered client IPs and update game state."""
        newly_added_humans = []

        for ip in client_ips:
            client_id = hash(ip) % 1000  # Simple hash-based ID
            latency = settings.latencies[
                len(self.client_manager.ip_latency_map) % len(settings.latencies)
            ]

            if ip not in self.client_manager.ip_latency_map:
                self.client_manager.add_client(client_id, ip, latency)
                newly_added_humans.append(ip)
                self.logger.info(f"New human client discovered: {ip}")

        if newly_added_humans and self._async_loop:
            for ip in newly_added_humans:
                self._async_loop.create_task(
                    self.obs_connection_manager.connect_single_client_immediately(
                        ip, self.client_manager
                    )
                )

        current_players = self.client_manager.get_client_count()
        current_state = self.game_state_manager.get_current_state()
        self.logger.info(
            f"Updated player count: {current_players}, threshold: {self.nplayers_threshold}, state: {current_state}"
        )

        if self.game_state_manager.should_transition_to_warmup(
            current_players, self.nplayers_threshold
        ):
            self.logger.info("Triggering warmup phase transition")
            self._start_warmup_phase()
        else:
            if current_state.name == "WAITING":
                self.game_state_manager.send_waiting_message(
                    current_players, self.nplayers_threshold
                )

    def _start_warmup_phase(self):
        """Start the warmup phase with OBS connections."""
        self.game_state_manager.transition_to_warmup()
        self.display_utils.display_client_table(self.client_manager)

        # Schedule OBS connections during warmup
        if self._async_loop:
            self._async_loop.create_task(
                self.obs_connection_manager.handle_warmup_connections(
                    self.client_manager, self.nplayers_threshold
                )
            )

    def run_server_loop(self):
        """Main server message processing loop."""
        self.logger.info("Starting server message processing loop")

        try:
            while True:
                message = self.read_server()
                if message:
                    self.logger.debug(f"SERVER: {message}")
                    self.process_server_message(message)

                    if self.game_state_manager.is_experiment_finished():
                        self.logger.info("Experiment completed, exiting loop")
                        break

                time.sleep(0.01)  # Prevent CPU spinning

        except KeyboardInterrupt:
            self.logger.info("Server loop interrupted by user")
        except Exception as e:
            self.logger.error(f"Error in server loop: {e}", exc_info=True)
        finally:
            self.logger.info("Server loop ended")

    async def cleanup_async(self):
        """Clean up all async resources."""
        try:
            await self.obs_connection_manager.cleanup_all()
            self.latency_manager.clear_latency_rules()
            self.logger.info("Async cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during async cleanup: {e}")

    def get_obs_manager(self):
        """Get OBS connection manager for external access."""
        return self.obs_connection_manager

    def get_bot_manager(self):
        """Get bot manager for external access."""
        return self.bot_manager

    def get_game_config_manager(self):
        """Get game configuration manager for external access."""
        return self.game_config_manager

    def get_latency_manager(self):
        """Get latency manager for external access."""
        return self.latency_manager

