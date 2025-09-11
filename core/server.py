import asyncio
import logging
import subprocess
import time
from subprocess import PIPE, Popen
from typing import Optional

import core.settings as settings
from core.client_manager import ClientManager
from core.game_state_manager import GameStateManager
from core.message_processor import MessageProcessor, MessageType
from core.network_utils import NetworkUtils
from core.obs_manager import OBSManager
from core.display_utils import DisplayUtils


class Server:
    __slots__ = (
        "_process",
        "logger",
        "nplayers_threshold",
        "client_manager",
        "game_state_manager",
        "message_processor",
        "obs_manager",
        "display_utils",
        "_async_loop",
        "_obs_task",
    )

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nplayers_threshold: int = settings.nplayers_threshold
        self.client_manager = ClientManager()
        self.game_state_manager = GameStateManager(self.send_command)
        self.message_processor = MessageProcessor(self.send_command)
        
        # OBS management
        obs_port = int(settings.obs_port) if hasattr(settings, 'obs_port') else 4455
        obs_password = settings.obs_password if hasattr(settings, 'obs_password') else None
        obs_timeout = int(settings.obs_connection_timeout) if hasattr(settings, 'obs_connection_timeout') else 30
        self.obs_manager = OBSManager(obs_port=obs_port, obs_password=obs_password, 
                                       connection_timeout=obs_timeout)
        self.display_utils = DisplayUtils()
        
        # Async support
        self._async_loop: Optional[asyncio.AbstractEventLoop] = None
        self._obs_task: Optional[asyncio.Task] = None

    def start_server(self):
        self.logger.info("Start OA Server process")
        self._process = Popen(
            [
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
                "+exec",
                "t_server.cfg",
                "+map",
                "aggressor",
            ],
            stdout=PIPE,
            stdin=PIPE,
            stderr=PIPE,
            universal_newlines=False,
        )

        self._server_init()

    def _server_init(self):
        if settings.bot_enable:
            max_clients = self.nplayers_threshold + settings.bot_count
            self.logger.debug(f"Setting maximum number of clients to {max_clients}")
            self.send_command(f"set sv_maxclients {max_clients}")

            self.send_command("set bot_enable 1")
            self.send_command("set bot_nochat 1")
            self.send_command("set bot_minplayers 0")
        else:
            self.logger.info("Bots are disable")

    def send_command(self, command: str):
        """Sends a command to the server's stdin."""
        if self._process and self._process.poll() is None:
            self.logger.debug(f"CMD_SEND: {command}")
            self._process.stdin.write(f"{command}\r\n".encode())
            self._process.stdin.flush()

    def read_server(self) -> str:
        return (
            self._process.stderr.readline().decode("utf-8", errors="replace").rstrip()
        )

    def dispose(self):
        if self._process and self._process.poll() is None:
            self._process.terminate()
            try:
                self._process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.logger.error(
                    f"Cannot properly terminal process {self._process.pid}"
                )
                self.logger.info("Gracefully kill the process")
                self._process.kill()
                self._process.wait()

        self.logger.info("Successfully dispose server process")

    def add_bots(self, num_bots, difficulty, bot_names):
        """
        Add bots to the server with the same difficulty level.

        Args:
            num_bots: Number of bots to add
            difficulty: Single difficulty level for all bots (1-5)
            bot_names: List of valid bot names
        """
        self.logger.info(
            f"Adding {num_bots} bots to the server with difficulty {difficulty}..."
        )

        # Make sure there are enough names
        while len(bot_names) < num_bots:
            bot_names.extend(bot_names)
        bot_names = bot_names[:num_bots]

        for i in range(num_bots):
            name = bot_names[i]

            self.logger.debug(f"Adding bot {name} with difficulty {difficulty}")
            # Format: "addbot [name] [difficulty]"
            self.send_command(f"addbot {name} {difficulty}")
            time.sleep(1)  # Small delay between adding bots

        self.logger.info("All bots added successfully")

    def process_server_message(self, raw_message: str):
        """Process a single server message through the message processor and handle events."""
        parsed_message = self.message_processor.process_message(raw_message)

        if parsed_message.message_type == MessageType.CLIENT_CONNECTING:
            self._handle_client_connecting(parsed_message)
        elif parsed_message.message_type == MessageType.CLIENT_DISCONNECT:
            self._handle_client_disconnect(parsed_message)
        elif parsed_message.message_type == MessageType.MAP_INITIALIZED:
            self._handle_map_initialized(parsed_message)
        elif parsed_message.message_type == MessageType.STATUS_LINE:
            self._handle_status_line(parsed_message)

    def _handle_client_connecting(self, parsed_message):
        """Handle client connection event."""
        client_id = parsed_message.data["client_id"]
        self.logger.info(f"Processing client {client_id} connection")

        # Status parsing will be handled by subsequent STATUS_LINE messages

    def _handle_client_disconnect(self, parsed_message):
        """Handle client disconnection event."""
        client_id = parsed_message.data["client_id"]
        self.client_manager.remove_client(client_id)

        # Check if we need to update game state based on player count
        current_players = self.client_manager.get_client_count()
        self.logger.info(
            f"Client {client_id} disconnected. Current players: {current_players}"
        )

        # Send waiting message if in WAITING state
        if self.game_state_manager.get_current_state().name == "WAITING":
            self.game_state_manager.send_waiting_message(
                current_players, self.nplayers_threshold
            )

    def _handle_map_initialized(self, parsed_message):
        """Handle map initialization event."""
        self.logger.info("Map initialized - processing state transitions")

        current_players = self.client_manager.get_client_count()

        # Check for state transitions
        result = self.game_state_manager.handle_map_initialized()

        if result.get("experiment_finished"):
            self.logger.info("Experiment sequence completed!")
            # Stop any active recordings
            if self._async_loop:
                self._async_loop.create_task(self.stop_match_recording_async())
            return

        # Handle recording for match transitions
        if self.game_state_manager.should_start_match_recording():
            if self._async_loop:
                self._async_loop.create_task(self.start_match_recording_async())
        
        # Apply actions based on state manager response
        if "apply_latency" in result.get("actions", []):
            self._apply_latency_rules()

        if "rotate_latency" in result.get("actions", []):
            self._rotate_latencies()
            # Stop and restart recording for new match
            if self._async_loop and self.game_state_manager.should_stop_match_recording():
                async def restart_recording():
                    await self.stop_match_recording_async()
                    await asyncio.sleep(2)  # Brief pause between recordings
                    await self.start_match_recording_async()
                self._async_loop.create_task(restart_recording())

    def _handle_status_line(self, parsed_message):
        """Handle server status output."""
        if parsed_message.data.get("status_complete"):
            # Status parsing complete, process all discovered client IPs
            client_ips = parsed_message.data.get("client_ips", [])
            self._process_discovered_clients(client_ips)
        elif parsed_message.data.get("client_ip"):
            # Individual client IP discovered
            client_ip = parsed_message.data["client_ip"]
            self.logger.debug(f"Discovered client IP: {client_ip}")

    def _process_discovered_clients(self, client_ips):
        """Process newly discovered client IPs and update game state."""
        # Add clients to client manager with latency assignment
        for i, ip in enumerate(client_ips):
            # Use a placeholder client ID (in real scenario, we'd track this better)
            client_id = hash(ip) % 1000  # Simple hash-based ID
            latency = settings.latencies[
                len(self.client_manager.ip_latency_map) % len(settings.latencies)
            ]
            self.client_manager.add_client(client_id, ip, latency)

        current_players = self.client_manager.get_client_count()
        self.logger.info(f"Updated player count: {current_players}")

        # Check for state transitions
        if self.game_state_manager.should_transition_to_warmup(
            current_players, self.nplayers_threshold
        ):
            self._start_warmup_phase()

    def _start_warmup_phase(self):
        """Start the warmup phase with OBS connections."""
        self.game_state_manager.transition_to_warmup()
        
        # Display current client status
        self.display_utils.display_client_table(self.client_manager)
        
        # Schedule OBS connection attempts for human clients
        if self._async_loop:
            self._obs_task = self._async_loop.create_task(
                self._handle_obs_connections_async()
            )

    def _apply_latency_rules(self):
        """Apply current latency rules to all connected clients."""
        latency_map = self.client_manager.get_latency_map()
        if latency_map:
            # Use default interface from settings or environment
            interface = "enp1s0"  # Could be made configurable
            NetworkUtils.apply_latency_rules(latency_map, interface)
            self.logger.info(f"Applied latency rules to {len(latency_map)} clients")

    def _rotate_latencies(self):
        """Rotate latency assignments for the next round."""
        # Simple rotation strategy - could be enhanced
        current_latencies = list(settings.latencies)
        rotated_latencies = current_latencies[1:] + current_latencies[:1]

        self.client_manager.assign_latencies(rotated_latencies)
        self.logger.info(f"Rotated latencies: {rotated_latencies}")

    def run_server_loop(self):
        """Main server message processing loop."""
        self.logger.info("Starting server message processing loop")

        try:
            while True:
                # Read message from server
                message = self.read_server()
                if message:
                    # Log the raw message
                    self.logger.debug(f"SERVER: {message}")

                    # Process through our message processor
                    self.process_server_message(message)

                    # Check for experiment completion
                    if self.game_state_manager.is_experiment_finished():
                        self.logger.info("Experiment completed, exiting loop")
                        break

                # Small delay to prevent CPU spinning
                time.sleep(0.01)

        except KeyboardInterrupt:
            self.logger.info("Server loop interrupted by user")
        except Exception as e:
            self.logger.error(f"Error in server loop: {e}", exc_info=True)
        finally:
            self.logger.info("Server loop ended")
            # Clean up async tasks
            if self._obs_task and not self._obs_task.done():
                self._obs_task.cancel()
    
    async def _handle_obs_connections_async(self):
        """Handle OBS connections asynchronously during warmup."""
        try:
            # Get human client IPs
            human_ips = self.client_manager.get_human_clients()
            
            if not human_ips:
                self.logger.info("No human clients to connect OBS")
                return
            
            self.logger.info(f"Attempting OBS connections for {len(human_ips)} human clients")
            self.display_utils.display_warmup_status(
                self.client_manager.get_human_count(),
                self.nplayers_threshold,
                obs_connecting=True
            )
            
            # Attempt connections to all human clients
            connection_results = await self.obs_manager.connect_all_clients(human_ips)
            
            # Update client manager with OBS status
            for ip, connected in connection_results.items():
                self.client_manager.set_obs_status(ip, connected)
            
            # Display connection results
            self.display_utils.display_obs_connection_results(connection_results)
            
            # Kick clients with failed OBS connections
            for ip, connected in connection_results.items():
                if not connected:
                    client_id = self.client_manager.get_client_id_by_ip(ip)
                    if client_id:
                        self.send_command(f"kick {client_id}")
                        self.logger.info(f"Kicked client {client_id} (IP: {ip}) - OBS connection failed")
                        self.client_manager.remove_client(client_id)
            
            # Check if we have any successful connections
            successful_connections = [ip for ip, connected in connection_results.items() if connected]
            
            if successful_connections:
                # Start recording for connected clients
                self.logger.info("Starting recording for connected OBS clients")
                recording_results = await self.obs_manager.start_all_recordings()
                
                # Display recording status
                status_dict = await self.obs_manager.get_all_recording_status()
                self.display_utils.display_recording_status(status_dict)
                
                # Check if ready to proceed
                if self.game_state_manager.check_obs_ready(self.obs_manager, self.client_manager):
                    self.logger.info("All OBS connections ready, warmup can proceed")
                    self.send_command("say OBS recording started for all clients!")
            else:
                self.logger.warning("No successful OBS connections, experiment may not proceed")
                self.send_command("say WARNING: No OBS connections established!")
                
        except Exception as e:
            self.logger.error(f"Error handling OBS connections: {e}", exc_info=True)
    
    async def start_match_recording_async(self):
        """Start recording for all connected OBS clients at match start."""
        try:
            if not self.obs_manager.get_connected_clients():
                self.logger.warning("No OBS clients connected for recording")
                return
            
            round_info = self.game_state_manager.get_round_info()
            self.display_utils.display_match_start(
                round_info['current_round'],
                round_info['max_rounds']
            )
            
            self.logger.info(f"Starting recording for match {round_info['current_round']}")
            recording_results = await self.obs_manager.start_all_recordings()
            
            # Log results
            for ip, success in recording_results.items():
                if success:
                    self.logger.info(f"Recording started for {ip}")
                else:
                    self.logger.warning(f"Failed to start recording for {ip}")
                    
        except Exception as e:
            self.logger.error(f"Error starting match recording: {e}", exc_info=True)
    
    async def stop_match_recording_async(self):
        """Stop recording for all connected OBS clients at match end."""
        try:
            if not self.obs_manager.get_connected_clients():
                return
            
            round_info = self.game_state_manager.get_round_info()
            self.display_utils.display_match_end(
                round_info['current_round'],
                round_info['max_rounds']
            )
            
            self.logger.info(f"Stopping recording for match {round_info['current_round']}")
            recording_results = await self.obs_manager.stop_all_recordings()
            
            # Log results
            for ip, success in recording_results.items():
                if success:
                    self.logger.info(f"Recording stopped for {ip}")
                else:
                    self.logger.warning(f"Failed to stop recording for {ip}")
                    
        except Exception as e:
            self.logger.error(f"Error stopping match recording: {e}", exc_info=True)
    
    def set_async_loop(self, loop: asyncio.AbstractEventLoop):
        """Set the async event loop for OBS operations."""
        self._async_loop = loop
        self.logger.debug("Async event loop set for OBS operations")
    
    async def cleanup_obs_async(self):
        """Clean up all OBS connections."""
        try:
            await self.obs_manager.disconnect_all()
            self.logger.info("All OBS connections cleaned up")
        except Exception as e:
            self.logger.error(f"Error cleaning up OBS connections: {e}")
