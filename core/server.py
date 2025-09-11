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

        self.bot_manager = BotManager(send_command_callback=self.send_command)

        self.game_config_manager = GameConfigManager(
            send_command_callback=self.send_command
        )

        self.latency_manager = LatencyManager(
            interface="enp1s0", send_command_callback=self.send_command
        )

    def start_server(self):
        """Start the OpenArena dedicated server process."""
        self.logger.info("Starting OpenArena server process")

        startup_config = self.game_config_manager.apply_startup_config()

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

        if parsed_message.message_type == MessageType.CLIENT_CONNECTING:
            self._handle_client_connecting(parsed_message)
        elif parsed_message.message_type == MessageType.CLIENT_DISCONNECT:
            self._handle_client_disconnect(parsed_message)
        elif parsed_message.message_type == MessageType.GAME_INITIALIZATION:
            self._handle_game_initialization(parsed_message)
        elif parsed_message.message_type == MessageType.MATCH_END_FRAGLIMIT:
            self._handle_match_end_fraglimit(parsed_message)
        elif parsed_message.message_type == MessageType.WARMUP_STATE:
            self._handle_warmup_state(parsed_message)
        elif parsed_message.message_type == MessageType.SHUTDOWN_GAME:
            self._handle_shutdown_game(parsed_message)
        elif parsed_message.message_type == MessageType.STATUS_LINE:
            self._handle_status_line(parsed_message)

    def _handle_client_connecting(self, parsed_message):
        """Handle client connection event."""
        client_id = parsed_message.data["client_id"]
        self.logger.info(f"Processing client {client_id} connection")

    def _handle_client_disconnect(self, parsed_message):
        """Handle client disconnection event."""
        client_id = parsed_message.data["client_id"]
        client_ip = self.client_manager.get_client_ip(client_id)

        if client_ip and self.obs_connection_manager.is_client_connected(client_ip):
            if self._async_loop:
                self._async_loop.create_task(
                    self.obs_connection_manager.disconnect_client(client_ip)
                )

        self.client_manager.remove_client(client_id)

        current_players = self.client_manager.get_client_count()
        self.logger.info(
            f"Client {client_id} disconnected. Current players: {current_players}"
        )

        if self.game_state_manager.get_current_state().name == "WAITING":
            self.send_command(f"say WAITING ROOM: {current_players}/{self.nplayers_threshold} players connected")

        if current_players > 0:
            self.display_utils.display_client_table(
                self.client_manager, "CLIENT STATUS AFTER DISCONNECTION"
            )

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

        result = self.game_state_manager.handle_match_end_detected()

        if result and "actions" in result:
            actions = result["actions"]

            if "rotate_latency" in actions:
                self.latency_manager.rotate_latencies(self.client_manager)
                self.logger.info("Latency rotated for next match")

            if "restart_match" in actions:
                time.sleep(2)  # Brief delay
                self.game_config_manager.restart_map()
                self.logger.info("Match restarted")

    def _handle_game_initialization(self, parsed_message):
        """Handle game initialization event - waiting to see if warmup or match follows."""
        self.logger.info("Game Initialization detected - determining initialization type")
        
        self.send_command("say Game initializing...")

    def _handle_warmup_state(self, parsed_message):
        """Handle warmup state transition."""
        warmup_info = parsed_message.data.get("warmup_info", "")
        self.logger.info(f"Warmup phase started: {warmup_info}")

        if self.bot_manager.should_add_bots() and not self.bot_manager.are_bots_added():
            self.logger.info("Adding bots")
            self.bot_manager.add_bots_to_server()
        
        self.send_command("say Warmup phase active!")

    def _handle_shutdown_game(self, parsed_message):
        """Handle game shutdown - either warmup end or match end."""
        event_type = parsed_message.data.get("event", "unknown")

        if event_type == "match_end":
            self.logger.info("ShutdownGame: Match ended completely")
            result = self.game_state_manager.handle_match_end_detected()
            
            if result and "actions" in result:
                actions = result["actions"]
                
                if "rotate_latency" in actions:
                    self.latency_manager.rotate_latencies(self.client_manager)
                    
                if "restart_match" in actions:
                    time.sleep(2)
                    self.game_config_manager.restart_map()
                    
            self.send_command("say Match completed!")
            
        elif event_type == "warmup_end":
            self.logger.info("ShutdownGame: Warmup ended, match starting")
            result = self.game_state_manager.handle_match_start_detected()
            
            if result and "actions" in result:
                actions = result["actions"]
                
                if "start_match_recording" in actions:
                    if self._async_loop:
                        self._async_loop.create_task(
                            self.obs_connection_manager.start_match_recording(
                                self.game_state_manager
                            )
                        )
                
                if "apply_latency" in actions:
                    self.latency_manager.apply_latency_rules(self.client_manager)
            
            self.send_command("say Match is starting!")
            
        else:
            self.logger.warning(f"Unknown shutdown game event: {event_type}")

    def _handle_status_line(self, parsed_message):
        """Handle server status output."""
        if parsed_message.data.get("status_complete"):
            client_data_list = parsed_message.data.get("client_data", [])
            self._process_discovered_clients(client_data_list)
        elif parsed_message.data.get("client_data"):
            client_data = parsed_message.data["client_data"]
            self.logger.debug(f"Discovered client: ID={client_data.get('client_id')}, IP={client_data.get('ip')}, Type={client_data.get('type')}")

    def _process_discovered_clients(self, client_data_list):
        """Process newly discovered clients from status output."""
        newly_added_humans = []
        
        self.logger.info(f"[CLIENT] Processing {len(client_data_list)} discovered clients")

        for client_data in client_data_list:
            client_id = client_data["client_id"]
            client_type = client_data["type"]
            client_name = client_data["name"]
            client_ip = client_data["ip"]
            
            if client_type == "HUMAN" and client_ip:
                # Assign latency for human clients
                latency = settings.latencies[
                    len(self.client_manager.ip_latency_map) % len(settings.latencies)
                ]

                if client_ip not in self.client_manager.ip_latency_map:
                    self.client_manager.add_client(
                        client_id=client_id,
                        ip=client_ip,
                        latency=latency,
                        name=client_name,
                        is_bot=False
                    )
                    newly_added_humans.append(client_ip)
                    self.logger.info(f"[CLIENT] New HUMAN client: ID={client_id}, Name={client_name}, IP={client_ip}, Latency={latency}ms")
                else:
                    self.logger.debug(f"[CLIENT] HUMAN client IP {client_ip} already tracked")
                    
            elif client_type == "BOT":
                # Add bot client (no IP needed)
                self.client_manager.add_client(
                    client_id=client_id,
                    ip=None,
                    latency=None,
                    name=client_name,
                    is_bot=True
                )
                self.logger.info(f"[CLIENT] BOT client: ID={client_id}, Name={client_name}")

        if newly_added_humans and self._async_loop:
            for ip in newly_added_humans:
                self._async_loop.create_task(
                    self.obs_connection_manager.connect_single_client_immediately(
                        ip, self.client_manager
                    )
                )

        current_players = self.client_manager.get_client_count()
        human_count = self.client_manager.get_human_count()
        bot_count = self.client_manager.get_bot_count()
        current_state = self.game_state_manager.get_current_state()
        
        self.logger.info(
            f"[CLIENT] Updated player count: {current_players} total ({human_count} humans, {bot_count} bots), threshold: {self.nplayers_threshold}, state: {current_state.name}"
        )

        if current_state.name == "WAITING":
            self.send_command(f"say WAITING ROOM: {human_count}/{self.nplayers_threshold} players connected")
            
        if current_players > 0:
            self.display_utils.display_client_table(self.client_manager, "CLIENT STATUS UPDATE")
            
            round_info = self.game_state_manager.get_round_info()
            self.logger.info(f"Experiment status: {round_info}")

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

