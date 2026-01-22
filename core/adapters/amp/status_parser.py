from __future__ import annotations

import logging
from typing import Dict, Optional

from core.adapters.status_parser import StatusParser


class AMPStatusParser(StatusParser):
    """
    Status parser for custom Quake-like server output.

    Example:
        id     time ping loss      state   rate adr name
        3    00:05   12    0   spawning  80000 127.190.6.117:52271 'quangminh2479'
    """

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def is_status_header(self, line: str) -> bool:
        """Detect status header line."""
        return (
            "id" in line
            and "ping" in line
            and "adr" in line
            and "name" in line
        )

    def is_separator(self, line: str) -> bool:
        """No separator line in this format."""
        return False

    def parse_client_line(self, line: str) -> Optional[Dict]:
        """
        Parse client line.

        Example:
        3    00:05   12    0   spawning  80000 127.190.6.117:52271 'quangminh2479'
        """
        try:
            parts = line.split()

            if len(parts) < 8:
                return None

            client_id = int(parts[0])
            time_connected = parts[1]
            ping = int(parts[2])
            loss = int(parts[3])
            state = parts[4]
            rate = int(parts[5])
            address = parts[6]

            # Name may contain spaces → join the rest
            name = " ".join(parts[7:]).strip("'\"")

            ip = address.split(":")[0] if ":" in address else address

            if not self._is_valid_ip(ip):
                return None

            return {
                "client_id": client_id,
                "time": time_connected,
                "ping": ping,
                "loss": loss,
                "state": state,
                "rate": rate,
                "ip": ip,
                "address": address,
                "name": name,
                "type": "HUMAN",
            }

        except Exception as e:
            self.logger.debug(f"Failed to parse status line '{line}': {e}")
            return None

    def _is_valid_ip(self, ip: str) -> bool:
        try:
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            return all(0 <= int(p) <= 255 for p in parts)
        except Exception:
            return False
