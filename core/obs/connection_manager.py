"""
OBS Connection Manager - Handles all OBS WebSocket operations.

Extracted from server.py to separate concerns and reduce complexity.
"""
import asyncio
import logging
from typing import Dict, List, Optional, Callable

from core.obs.manager import OBSManager
from core.utils.display_utils import DisplayUtils


class OBSConnectionManager:
    """
    Manages OBS WebSocket connections and recording operations.
    
    Handles both immediate connections when clients join and batch 
    connections during warmup phase.
    """
    
    def __init__(self, obs_port: int = 4455, obs_password: Optional[str] = None, 
                 obs_timeout: int = 30, send_command_callback: Optional[Callable[[str], None]] = None):
        """
        Initialize OBS Connection Manager.
        
        Args:
            obs_port: OBS WebSocket port
            obs_password: OBS WebSocket password
            obs_timeout: Connection timeout in seconds
            send_command_callback: Function to send commands to game server
        """
        self.obs_manager = OBSManager(
            obs_port=obs_port, 
            obs_password=obs_password, 
            connection_timeout=obs_timeout
        )
        self.display_utils = DisplayUtils()
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)
        
        # Track ongoing connection tasks
        self._connection_tasks: Dict[str, asyncio.Task] = {}
    
    async def connect_single_client_immediately(self, client_ip: str, client_manager) -> bool:
        """
        Connect to a single client's OBS instance immediately upon joining.
        
        Args:
            client_ip: Client IP address
            client_manager: ClientManager instance to update OBS status
            
        Returns:
            True if connection successful, False otherwise
        """
        try:
            self.logger.info(f"Attempting immediate OBS connection for {client_ip}")
            
            # Cancel any existing connection task for this IP
            if client_ip in self._connection_tasks:
                self._connection_tasks[client_ip].cancel()
            
            # Attempt connection to this specific client
            connected = await self.obs_manager.connect_client_obs(client_ip)
            
            # Update client manager with OBS status
            client_manager.set_obs_status(client_ip, connected)
            
            if connected:
                self.logger.info(f"✓ OBS connected for client {client_ip}")
                if self.send_command:
                    self.send_command(f"say OBS connected for {client_ip}")
                
                # Display updated client table
                print(f"\n[OBS CONNECTION SUCCESS] {client_ip}")
                self.display_utils.display_client_table(
                    client_manager, "UPDATED CLIENT STATUS"
                )
            else:
                self.logger.warning(f"✗ OBS connection failed for client {client_ip}")
                if self.send_command:
                    self.send_command(f"say OBS connection failed for {client_ip} - will be kicked")
                
                print(f"\n[OBS CONNECTION FAILED] {client_ip}")
                self.display_utils.display_client_table(
                    client_manager, "CLIENT STATUS - OBS CONNECTION FAILED"
                )
                
                # Request client kick for failed OBS connection
                return await self._handle_connection_failure(client_ip, client_manager)
            
            return connected
            
        except Exception as e:
            self.logger.error(f"Error connecting to OBS for {client_ip}: {e}", exc_info=True)
            return False
    
    async def _handle_connection_failure(self, client_ip: str, client_manager) -> bool:
        """Handle failed OBS connection by kicking the client."""
        client_id = client_manager.get_client_id_by_ip(client_ip)
        if client_id and self.send_command:
            self.send_command(f"kick {client_id}")
            self.send_command(f"say Client {client_id} kicked - OBS not available")
            self.logger.info(f"Kicked client {client_id} ({client_ip}) - OBS connection failed")
        else:
            self.logger.warning(f"Could not find client ID for IP {client_ip} to kick")
        
        return False
    
    async def handle_warmup_connections(self, client_manager, nplayers_threshold: int) -> Dict[str, bool]:
        """
        Handle OBS connections during warmup phase.
        
        Args:
            client_manager: ClientManager instance
            nplayers_threshold: Minimum number of players needed
            
        Returns:
            Dictionary mapping IP to connection success status
        """
        try:
            human_ips = client_manager.get_human_clients()
            
            if not human_ips:
                self.logger.info("No human clients for warmup OBS check")
                return {}
            
            already_connected = []
            need_connection = []
            
            for ip in human_ips:
                if self.obs_manager.is_client_connected(ip):
                    already_connected.append(ip)
                else:
                    obs_status = client_manager.get_obs_status(ip)
                    if obs_status is None or obs_status is False:
                        need_connection.append(ip)
            
            self.logger.info(
                f"OBS Status - Already connected: {len(already_connected)}, Need connection: {len(need_connection)}"
            )
            
            self.display_utils.display_warmup_status(
                client_manager.get_human_count(),
                nplayers_threshold,
                obs_connecting=(len(need_connection) > 0),
            )
            
            connection_results = {}
            
            if need_connection:
                self.logger.info(f"Attempting OBS connections for {len(need_connection)} remaining clients")
                connection_results = await self.obs_manager.connect_all_clients(need_connection)
                
                for ip, connected in connection_results.items():
                    client_manager.set_obs_status(ip, connected)
            
            for ip in already_connected:
                connection_results[ip] = True
            
            if need_connection:
                self.display_utils.display_obs_connection_results(connection_results)
            
            self.display_utils.display_client_table(
                client_manager, "WARMUP PHASE - CLIENT STATUS"
            )
            
            await self._handle_warmup_failures(connection_results, client_manager)
            
            return connection_results
            
        except Exception as e:
            self.logger.error(f"Error handling OBS connections during warmup: {e}", exc_info=True)
            return {}
    
    async def _handle_warmup_failures(self, connection_results: Dict[str, bool], client_manager):
        """Handle failed OBS connections during warmup by kicking clients."""
        failed_clients = [ip for ip, connected in connection_results.items() if not connected]
        
        for ip in failed_clients:
            client_id = client_manager.get_client_id_by_ip(ip)
            if client_id and self.send_command:
                self.send_command(f"kick {client_id}")
                self.logger.info(f"Kicked client {client_id} (IP: {ip}) - OBS connection failed")
                client_manager.remove_client(client_id)
    
    async def start_match_recording(self, game_state_manager) -> Dict[str, bool]:
        """Start recording for all connected OBS clients at match start."""
        try:
            if not self.obs_manager.get_connected_clients():
                self.logger.warning("No OBS clients connected for recording")
                return {}
            
            round_info = game_state_manager.get_round_info()
            self.display_utils.display_match_start(
                round_info["current_round"], round_info["max_rounds"]
            )
            
            self.logger.info(f"Starting recording for match {round_info['current_round']}")
            recording_results = await self.obs_manager.start_all_recordings()
            
            # Log results
            for ip, success in recording_results.items():
                if success:
                    self.logger.info(f"Recording started for {ip}")
                else:
                    self.logger.warning(f"Failed to start recording for {ip}")
            
            return recording_results
            
        except Exception as e:
            self.logger.error(f"Error starting match recording: {e}", exc_info=True)
            return {}
    
    async def stop_match_recording(self, game_state_manager) -> Dict[str, bool]:
        """Stop recording for all connected OBS clients at match end."""
        try:
            if not self.obs_manager.get_connected_clients():
                return {}
            
            round_info = game_state_manager.get_round_info()
            self.display_utils.display_match_end(
                round_info["current_round"], round_info["max_rounds"]
            )

            await asyncio.sleep(4)

            self.logger.info(f"Stopping recording for match {round_info['current_round']}")
            recording_results = await self.obs_manager.stop_all_recordings()
            
            # Log results
            for ip, success in recording_results.items():
                if success:
                    self.logger.info(f"Recording stopped for {ip}")
                else:
                    self.logger.warning(f"Failed to stop recording for {ip}")
            
            return recording_results
            
        except Exception as e:
            self.logger.error(f"Error stopping match recording: {e}", exc_info=True)
            return {}
    
    async def disconnect_client(self, client_ip: str):
        """Disconnect a single client's OBS connection."""
        try:
            if client_ip in self._connection_tasks:
                self._connection_tasks[client_ip].cancel()
                del self._connection_tasks[client_ip]
            
            await self.obs_manager.disconnect_client(client_ip)
            self.logger.info(f"OBS connection closed for disconnected client {client_ip}")
        except Exception as e:
            self.logger.error(f"Error disconnecting OBS for {client_ip}: {e}")
    
    async def cleanup_all(self):
        """Clean up all OBS connections and tasks."""
        try:
            for task in self._connection_tasks.values():
                task.cancel()
            self._connection_tasks.clear()
            
            await self.obs_manager.disconnect_all()
            self.logger.info("All OBS connections cleaned up")
        except Exception as e:
            self.logger.error(f"Error cleaning up OBS connections: {e}")

    def is_client_connected(self, client_ip: str) -> bool:
        """Check if a client is connected."""
        return self.obs_manager.is_client_connected(client_ip)