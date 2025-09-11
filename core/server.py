import logging
import subprocess
import time
from subprocess import PIPE, Popen

import core.settings as settings
from core.client_manager import ClientManager
from core.game_state_manager import GameStateManager
from core.message_processor import MessageProcessor, MessageType
from core.network_utils import NetworkUtils


class Server:
    __slots__ = (
        "_process",
        "logger",
        "nplayers_threshold",
        "client_manager",
        "game_state_manager",
        "message_processor",
    )

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nplayers_threshold: int = settings.nplayers_threshold
        self.client_manager = ClientManager()
        self.game_state_manager = GameStateManager(self.send_command)
        self.message_processor = MessageProcessor(self.send_command)

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
            return

        # Apply actions based on state manager response
        if "apply_latency" in result.get("actions", []):
            self._apply_latency_rules()

        if "rotate_latency" in result.get("actions", []):
            self._rotate_latencies()

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
        """Start the warmup phase with bots if enabled."""
        self.game_state_manager.transition_to_warmup()

        # Add bots if enabled
        if settings.bot_enable and settings.bot_count > 0:
            self.logger.info("Adding bots before warmup")
            self.add_bots(
                settings.bot_count, settings.bot_difficulty, settings.bot_names
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
