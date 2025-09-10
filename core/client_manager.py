import logging
from typing import Dict, List, Optional


class ClientManager:
    """Manages client connections and their network configurations."""
    
    def __init__(self):
        self.ip_latency_map: Dict[str, int] = {}
        self.client_ip_map: Dict[int, str] = {}
        self.player_count: int = 0
        self.logger = logging.getLogger(__name__)
    
    def add_client(self, client_id: int, ip: str, latency: Optional[int] = None) -> None:
        """Add a new client with IP address and optional latency assignment."""
        if ip not in self.ip_latency_map:
            self.client_ip_map[client_id] = ip
            self.ip_latency_map[ip] = latency if latency is not None else 0
            self.player_count = len(self.ip_latency_map)
            self.logger.info(f"Added client {client_id} with IP {ip}, latency {latency}ms")
        else:
            self.logger.debug(f"Client IP {ip} already exists, updating client_id mapping")
            self.client_ip_map[client_id] = ip
    
    def remove_client(self, client_id: int) -> None:
        """Remove client and clean up mappings."""
        if client_id in self.client_ip_map:
            ip = self.client_ip_map[client_id]
            del self.client_ip_map[client_id]
            
            # Only remove IP if no other clients are using it
            if ip not in self.client_ip_map.values():
                del self.ip_latency_map[ip]
                self.logger.info(f"Removed client {client_id} with IP {ip}")
            else:
                self.logger.debug(f"Client {client_id} removed but IP {ip} still in use")
                
            self.player_count = len(self.ip_latency_map)
        else:
            self.logger.warning(f"Attempted to remove unknown client {client_id}")
    
    def get_client_count(self) -> int:
        """Return current number of connected clients."""
        return self.player_count
    
    def assign_latencies(self, latencies: List[int]) -> None:
        """Distribute latencies across connected clients using round-robin."""
        if not self.ip_latency_map or not latencies:
            return
            
        ips = list(self.ip_latency_map.keys())
        for i, ip in enumerate(ips):
            self.ip_latency_map[ip] = latencies[i % len(latencies)]
        
        self.logger.info(f"Assigned latencies to {len(ips)} clients: {dict(zip(ips, [latencies[i % len(latencies)] for i in range(len(ips))]))}")
    
    def get_latency_map(self) -> Dict[str, int]:
        """Return current IP to latency mapping."""
        return self.ip_latency_map.copy()
    
    def get_client_ip(self, client_id: int) -> Optional[str]:
        """Get IP address for a specific client ID."""
        return self.client_ip_map.get(client_id)
    
    def set_client_latency(self, ip: str, latency: int) -> None:
        """Set latency for a specific client IP."""
        if ip in self.ip_latency_map:
            self.ip_latency_map[ip] = latency
            self.logger.debug(f"Set latency for {ip} to {latency}ms")
        else:
            self.logger.warning(f"Attempted to set latency for unknown IP {ip}")
    
    def clear_all_clients(self) -> None:
        """Clear all client data."""
        self.ip_latency_map.clear()
        self.client_ip_map.clear()
        self.player_count = 0
        self.logger.info("Cleared all client data")
    
    def get_client_list(self) -> List[str]:
        """Return list of connected client IPs."""
        return list(self.ip_latency_map.keys())