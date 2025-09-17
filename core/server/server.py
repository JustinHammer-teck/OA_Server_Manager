import asyncio
import logging
import subprocess
import threading
import time
from subprocess import PIPE, Popen
from typing import Optional

import core.utils.settings as settings
from core.game.game_manager import GameManager
from core.game.state_manager import GameStateManager
from core.messaging.message_processor import MessageProcessor, MessageType
from core.network.network_manager import NetworkManager
from core.obs.connection_manager import OBSConnectionManager
from core.utils.display_utils import DisplayUtils


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
        self._active_tasks = set()
        self._shutdown_event = threading.Event()

        self.network_manager = NetworkManager(
            interface=settings.interface, send_command_callback=self.send_command
        )
        self.game_manager = GameManager(send_command_callback=self.send_command)
        self.game_state_manager = GameStateManager(self.send_command)
        self.message_processor = MessageProcessor(self.send_command)
        self.display_utils = DisplayUtils()

        self.obs_connection_manager = OBSConnectionManager(
            obs_port=int(getattr(settings, "obs_port", 4455)),
            obs_password=getattr(settings, "obs_password", None),
            obs_timeout=int(getattr(settings, "obs_connection_timeout", 30)),
            send_command_callback=self.send_command,
        )

        self.message_handlers = {
            MessageType.CLIENT_CONNECTING: self._on_client_connect,
            MessageType.CLIENT_DISCONNECT: self._on_client_disconnect,
            MessageType.MATCH_END_FRAGLIMIT: self._on_match_end,
            MessageType.WARMUP_STATE: self._on_warmup,
            MessageType.SHUTDOWN_GAME: self._on_shutdown,
            MessageType.STATUS_LINE: self._on_status,
        }

    def start_server(self):
        """Start the OpenArena dedicated server process."""
        self.logger.info("Starting OpenArena server process")

        startup_config = self.game_manager.apply_startup_config()

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
        self.game_manager.initialize_bot_settings(self.nplayers_threshold)
        self.game_manager.apply_default_config()

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
        self.logger.info("Starting graceful server shutdown...")

        self._shutdown_event.set()
        self._cancel_all_async_tasks()

        self.game_manager.reset_bot_state()

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

    def _cancel_all_async_tasks(self):
        """Cancel all active async tasks."""
        if not self._active_tasks:
            return

        self.logger.info(f"Cancelling {len(self._active_tasks)} active async tasks...")

        for task in list(self._active_tasks):
            try:
                task.cancel()
                self.logger.debug(f"Cancelled async task: {task}")
            except Exception as e:
                self.logger.error(f"Error cancelling task {task}: {e}")

        timeout = 3.0
        start_time = time.time()
        while self._active_tasks and (time.time() - start_time) < timeout:
            time.sleep(0.1)

        remaining_tasks = len(self._active_tasks)
        if remaining_tasks > 0:
            self.logger.warning(
                f"{remaining_tasks} async tasks did not cancel within {timeout}s"
            )
        else:
            self.logger.info("All async tasks cancelled successfully")

    def set_async_loop(self, loop: asyncio.AbstractEventLoop):
        """Set the async event loop for OBS operations."""
        self._async_loop = loop
        self.logger.debug("Async event loop set for OBS operations")

    async def cleanup_obs_async(self):
        """Clean up OBS connections asynchronously."""
        try:
            await self.obs_connection_manager.cleanup_all()
            self.logger.info("OBS connections cleaned up successfully")
        except Exception as e:
            self.logger.error(f"Error cleaning up OBS connections: {e}", exc_info=True)

    def _create_async_task_safe(self, coro, name: str = None):
        """Safely create an async task with exception handling."""
        if not self._async_loop or self._shutdown_event.is_set():
            self.logger.warning(
                f"No async loop available or shutdown in progress for task: {name or 'unnamed'}"
            )
            return None

        future = asyncio.run_coroutine_threadsafe(coro, self._async_loop)
        self._active_tasks.add(future)

        def handle_task_exception(future_result):
            self._active_tasks.discard(future_result)
            try:
                future_result.result()
                self.logger.debug(f"Task {name or 'unnamed'} completed successfully")
            except asyncio.CancelledError:
                self.logger.debug(f"Task {name or 'unnamed'} was cancelled")
            except Exception as e:
                self.logger.error(
                    f"Unhandled exception in task {name or 'unnamed'}: {e}",
                    exc_info=True,
                )

        future.add_done_callback(handle_task_exception)
        return future

    def is_shutdown_requested(self):
        """Check if shutdown has been requested."""
        return self._shutdown_event.is_set()

    def process_server_message(self, raw_message: str):
        """Process server message using dispatch dictionary."""
        parsed = self.message_processor.process_message(raw_message)

        handler = self.message_handlers.get(parsed.message_type)
        if handler:
            handler(parsed)

    def _update_player_status(self):
        """Common player status update logic."""
        current_players = self.network_manager.get_client_count()
        human_count = self.network_manager.get_human_count()
        current_state = self.game_state_manager.get_current_state().name

        if current_state == "WAITING":
            self.send_command(
                f"say WAITING ROOM: {human_count}/{self.nplayers_threshold} players connected"
            )

        if current_players > 0:
            self.display_utils.display_client_table(
                self.network_manager, "CLIENT STATUS UPDATE"
            )

    def _on_client_connect(self, msg):
        """Handle client connection event."""
        client_id = msg.data["client_id"]
        self.logger.info(f"Processing client {client_id} connection")

    def _on_client_disconnect(self, msg):
        """Handle client disconnection event."""
        client_id = msg.data["client_id"]
        client_ip = self.network_manager.get_client_ip(client_id)

        if client_ip and self.obs_connection_manager.is_client_connected(client_ip):
            self._create_async_task_safe(
                self.obs_connection_manager.disconnect_client(client_ip),
                f"disconnect_{client_ip}",
            )

        self.network_manager.remove_client(client_id)
        self.logger.info(
            f"Client {client_id} disconnected. Current players: {self.network_manager.get_client_count()}"
        )
        self._update_player_status()

    def _on_match_end(self, msg):
        """Handle match end due to fraglimit hit."""
        self.logger.info("Match ended - Fraglimit hit! Stopping OBS recordings...")

        self._create_async_task_safe(
            self.obs_connection_manager.stop_match_recording(self.game_state_manager),
            "stop_match_recording",
        )

        self.send_command("say Match ended! Recordings stopped.")

        result = self.game_state_manager.handle_fraglimit_detected()
        if result and "actions" in result:
            self._process_match_end_actions(result["actions"])
        if result and result.get("experiment_finished"):
            self.logger.info("Experiment completed after fraglimit hit")

    def _on_warmup(self, msg):
        """Handle warmup state transition."""
        warmup_info = msg.data.get("warmup_info", "")
        self.logger.info(f"Warmup phase started: {warmup_info}")

        result = self.game_state_manager.handle_warmup_detected()
        if result.get("state_changed"):
            self.logger.info("Game state updated to WARMUP")

        if (
            self.game_manager.should_add_bots()
            and not self.game_manager.are_bots_added()
            and not self.game_manager.is_bot_addition_in_progress()
        ):
            self.logger.info("Starting async bot addition")
            self._create_async_task_safe(
                self.game_manager.add_bots_to_server_async(), "add_bots_async"
            )

        human_count = self.network_manager.get_human_count()
        obs_status = self.game_state_manager.get_obs_status(
            self.obs_connection_manager.obs_manager, self.network_manager
        )

        if human_count >= self.nplayers_threshold and (
            human_count == 0 or obs_status["all_connected"]
        ):
            self.send_command("set g_doWarmup 0")
            self.send_command(
                "say All players connected and OBS ready - starting match!"
            )
            self.logger.info(
                "Warmup conditions satisfied - disabling warmup to start match"
            )
        else:
            reasons = []
            if human_count < self.nplayers_threshold:
                reasons.append(f"players {human_count}/{self.nplayers_threshold}")
            if human_count > 0 and not obs_status["all_connected"]:
                reasons.append(f"OBS {obs_status['connected']}/{obs_status['total']}")

            self.send_command(
                f"say Warmup continues - waiting for: {', '.join(reasons)}"
            )
            self.logger.info(f"Warmup continues due to: {', '.join(reasons)}")
            self.game_manager.restart_warmup()

    def _process_match_end_actions(self, actions):
        if "rotate_latency" in actions:
            self.network_manager.rotate_latencies()
            self.logger.info("Latency rotated for next match")

        if "restart_match" in actions:
            time.sleep(2)
            self.game_manager.restart_map()
            self.logger.info("Match restarted")

    def _on_shutdown(self, msg):
        """Handle game shutdown - either warmup end or match end."""
        event_type = msg.data.get("event", "unknown")

        if event_type == "match_end":
            self.logger.info("ShutdownGame: Match ended completely")
            result = self.game_state_manager.handle_match_end_detected()
            if result and "actions" in result:
                self._process_match_end_actions(result["actions"])
            self.send_command("say Match completed!")
        elif event_type == "warmup_end":
            self.logger.info("ShutdownGame: Warmup ended, match starting")
            result = self.game_state_manager.handle_match_start_detected()
            if result and "actions" in result:
                actions = result["actions"]
                if "start_match_recording" in actions:
                    self._create_async_task_safe(
                        self.obs_connection_manager.start_match_recording(
                            self.game_state_manager
                        ),
                        "start_match_recording",
                    )
                if "apply_latency" in actions:
                    if self.network_manager.is_enabled():
                        self.network_manager.apply_latency_rules()
                    else:
                        self.logger.info(
                            "Latency control disabled, skipping latency application"
                        )
            self.send_command("say Match is starting!")
        else:
            self.logger.warning(f"Unknown shutdown game event: {event_type}")

    def _on_status(self, msg):
        """Handle server status output."""
        if msg.data.get("status_complete"):
            client_data_list = msg.data.get("client_data", [])
            self._process_discovered_clients(client_data_list)
        elif msg.data.get("client_data"):
            client_data = msg.data["client_data"]
            self.logger.debug(
                f"Discovered client: ID={client_data.get('client_id')}, IP={client_data.get('ip')}, Type={client_data.get('type')}"
            )

    def _process_discovered_clients(self, client_data_list):
        """Process newly discovered clients from status output."""
        newly_added_humans = []

        self.logger.info(
            f"[CLIENT] Processing {len(client_data_list)} discovered clients"
        )

        for client_data in client_data_list:
            client_id = client_data["client_id"]
            client_type = client_data["type"]
            client_name = client_data["name"]
            client_ip = client_data["ip"]

            if client_type == "HUMAN" and client_ip:
                latency = settings.latencies[
                    len(self.network_manager.ip_latency_map) % len(settings.latencies)
                ]

                if client_ip not in self.network_manager.ip_latency_map:
                    self.network_manager.add_client(
                        client_id=client_id,
                        ip=client_ip,
                        latency=latency,
                        name=client_name,
                        is_bot=False,
                    )
                    newly_added_humans.append(client_ip)
                    self.logger.info(
                        f"[CLIENT] New HUMAN client: ID={client_id}, Name={client_name}, IP={client_ip}, Latency={latency}ms"
                    )
                else:
                    self.logger.debug(
                        f"[CLIENT] HUMAN client IP {client_ip} already tracked"
                    )

            elif client_type == "BOT":
                self.network_manager.add_client(
                    client_id=client_id,
                    ip=None,
                    latency=None,
                    name=client_name,
                    is_bot=True,
                )
                self.logger.info(
                    f"[CLIENT] BOT client: ID={client_id}, Name={client_name}"
                )

        if newly_added_humans:
            for ip in newly_added_humans:
                self._create_async_task_safe(
                    self.obs_connection_manager.connect_single_client_immediately(
                        ip, self.network_manager
                    ),
                    f"connect_client_{ip}",
                )

        current_players = self.network_manager.get_client_count()
        human_count = self.network_manager.get_human_count()
        bot_count = self.network_manager.get_bot_count()
        current_state = self.game_state_manager.get_current_state()

        self.logger.info(
            f"[CLIENT] Updated player count: {current_players} total ({human_count} humans, {bot_count} bots), threshold: {self.nplayers_threshold}, state: {current_state.name}"
        )

        if current_state.name == "WAITING":
            self.send_command(
                f"say WAITING ROOM: {human_count}/{self.nplayers_threshold} players connected"
            )

            if self.game_state_manager.should_start_warmup(
                self.network_manager, self.obs_connection_manager.obs_manager
            ):
                self.logger.info(
                    "Starting warmup due to player threshold or incomplete OBS connections"
                )
                self.game_manager.start_warmup_phase()

        if current_players > 0:
            self.display_utils.display_client_table(
                self.network_manager, "CLIENT STATUS UPDATE"
            )

            round_info = self.game_state_manager.get_round_info()
            self.logger.info(f"Experiment status: {round_info}")

    def run_server_loop(self):
        """Main server message processing loop."""
        self.logger.info("Starting server message processing loop")

        try:
            while not self.is_shutdown_requested():
                message = self.read_server()
                if message:
                    self.logger.debug(f"SERVER: {message}")
                    self.process_server_message(message)

                    if self.game_state_manager.is_experiment_finished():
                        human_count = self.network_manager.get_human_count()
                        if human_count > 0:
                            self.logger.info("Experiment completed, exiting loop")
                        else:
                            self.logger.debug(
                                "Experiment marked as finished but no human players - continuing to run"
                            )

                        break

                time.sleep(0.01)

        except KeyboardInterrupt:
            self.logger.info("Server loop interrupted by user")
        except Exception as e:
            self.logger.error(f"Error in server loop: {e}", exc_info=True)
        finally:
            self.logger.info("Server loop ended")

