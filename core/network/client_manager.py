import logging
from typing import Any, Dict, List, Optional


class ClientManager:
    """Manages client connections and their network configurations."""

    BOT_NAMES = [
        "Angelyss",
        "Arachna",
        "Major",
        "Sarge",
        "Skelebot",
        "Merman",
        "Beret",
        "Kyonshi",
    ]

    def __init__(self):
        self.ip_latency_map: Dict[str, int] = {}
        self.client_ip_map: Dict[int, str] = {}
        self.client_type_map: Dict[int, str] = {}  # "HUMAN" or "BOT"
        self.client_name_map: Dict[int, str] = {}  # Client names
        self.obs_status_map: Dict[str, bool] = {}  # IP -> OBS connected
        self.player_count: int = 0
        self.human_count: int = 0
        self.bot_count: int = 0
        self.logger = logging.getLogger(__name__)

    def add_client(
        self,
        client_id: int,
        ip: Optional[str] = None,
        latency: Optional[int] = None,
        name: Optional[str] = None,
        is_bot: bool = False,
    ) -> None:
        """Add a new client with IP address and optional latency assignment."""

        if name and name in self.BOT_NAMES:
            is_bot = True

        self.client_type_map[client_id] = "BOT" if is_bot else "HUMAN"

        if name:
            self.client_name_map[client_id] = name

        if not is_bot and ip:
            if ip not in self.ip_latency_map:
                self.client_ip_map[client_id] = ip
                self.ip_latency_map[ip] = latency if latency is not None else 0
                self.obs_status_map[ip] = False  # Default OBS not connected
                self.logger.info(
                    f"Added HUMAN client {client_id} with IP {ip}, latency {latency}ms"
                )
            else:
                self.logger.debug(
                    f"Client IP {ip} already exists, updating client_id mapping"
                )
                self.client_ip_map[client_id] = ip
            self.human_count = len(
                [cid for cid, ctype in self.client_type_map.items() if ctype == "HUMAN"]
            )
        elif is_bot:
            self.logger.info(f"Added BOT client {client_id} with name {name}")
            self.bot_count = len(
                [cid for cid, ctype in self.client_type_map.items() if ctype == "BOT"]
            )

        self.player_count = self.human_count + self.bot_count

    def remove_client(self, client_id: int) -> None:
        """Remove client and clean up mappings."""
        client_type = self.client_type_map.get(client_id, "UNKNOWN")

        if client_id in self.client_ip_map:
            ip = self.client_ip_map[client_id]
            del self.client_ip_map[client_id]

            if ip not in self.client_ip_map.values():
                if ip in self.ip_latency_map:
                    del self.ip_latency_map[ip]
                if ip in self.obs_status_map:
                    del self.obs_status_map[ip]
                self.logger.info(
                    f"Removed {client_type} client {client_id} with IP {ip}"
                )
            else:
                self.logger.debug(
                    f"Client {client_id} removed but IP {ip} still in use"
                )

        if client_id in self.client_type_map:
            del self.client_type_map[client_id]
        if client_id in self.client_name_map:
            del self.client_name_map[client_id]

        self.human_count = len(
            [cid for cid, ctype in self.client_type_map.items() if ctype == "HUMAN"]
        )
        self.bot_count = len(
            [cid for cid, ctype in self.client_type_map.items() if ctype == "BOT"]
        )
        self.player_count = self.human_count + self.bot_count

        if client_type == "UNKNOWN" and client_id not in self.client_type_map:
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

        self.logger.info(
            f"Assigned latencies to {len(ips)} clients: {dict(zip(ips, [latencies[i % len(latencies)] for i in range(len(ips))]))}"
        )

    def get_latency_map(self) -> Dict[str, int]:
        """Return current IP to latency mapping."""
        return self.ip_latency_map.copy()

    def get_client_ip(self, client_id: int) -> Optional[str]:
        """Get IP address for a specific client ID."""
        return self.client_ip_map.get(client_id)

    def get_human_clients(self) -> List[str]:
        """Return list of human client IPs."""
        human_ips = []
        for client_id, client_type in self.client_type_map.items():
            if client_type == "HUMAN" and client_id in self.client_ip_map:
                human_ips.append(self.client_ip_map[client_id])
        return human_ips

    def get_human_count(self) -> int:
        """Return current number of human players."""
        return self.human_count

    def get_bot_count(self) -> int:
        """Return current number of bot players."""
        return self.bot_count

    def set_obs_status(self, ip: str, connected: bool) -> None:
        """Set OBS connection status for a client IP."""
        if ip in self.ip_latency_map:
            self.obs_status_map[ip] = connected
            self.logger.debug(f"Set OBS status for {ip} to {connected}")
        else:
            self.logger.warning(f"Attempted to set OBS status for unknown IP {ip}")

    def get_obs_status(self, ip: str) -> Optional[bool]:
        """Get OBS connection status for a client IP."""
        return self.obs_status_map.get(ip)

    def get_client_id_by_ip(self, ip: str) -> Optional[int]:
        """Get client ID by IP address."""
        for client_id, client_ip in self.client_ip_map.items():
            if client_ip == ip:
                return client_id
        return None

    def get_client_info_table(self) -> List[List[Any]]:
        """Get client information formatted for tabulate display."""
        table_data = []

        for client_id, client_type in self.client_type_map.items():
            row = [client_id]

            if client_type == "HUMAN":
                ip = self.client_ip_map.get(client_id, "N/A")
                row.append(ip)
                row.append("HUMAN")
                row.append(
                    f"{self.ip_latency_map.get(ip, 0)}ms" if ip != "N/A" else "N/A"
                )

                # OBS status
                obs_status = self.obs_status_map.get(ip, False)
                row.append("Connected" if obs_status else "Not Connected")
            else:  # BOT
                row.append("N/A")  # No IP for bots
                row.append("BOT")
                row.append("N/A")  # No latency for bots
                row.append("N/A")  # No OBS for bots

            # Add name if available
            name = self.client_name_map.get(client_id, "Unknown")
            row.append(name)

            table_data.append(row)

        return table_data

