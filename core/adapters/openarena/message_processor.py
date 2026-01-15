"""OpenArena-specific message parsing."""

import logging
import re
from typing import Callable, Dict, List, Optional

from core.adapters.base import BaseMessageProcessor, MessageType, ParsedMessage


class OAMessageProcessor(BaseMessageProcessor):
    """
    OpenArena-specific message parsing.

    Parses server console output using regex patterns specific to
    OpenArena/Quake III Arena.
    """

    def __init__(self, send_command_callback: Optional[Callable[[str], None]] = None):
        super().__init__(send_command_callback)
        self.logger = logging.getLogger(__name__)

        # OpenArena-specific regex patterns
        self.patterns = {
            MessageType.CLIENT_CONNECT: re.compile(
                r"^Client ([0-9]+) connecting with ([0-9]+) challenge ping$"
            ),
            MessageType.CLIENT_DISCONNECT: re.compile(r"^ClientDisconnect: ([0-9]+)$"),
            MessageType.GAME_INITIALIZATION: re.compile(
                r"^------- Game Initialization -------$"
            ),
            MessageType.GAME_END: re.compile(r"^Exit: (Fraglimit|Timelimit) hit\.$"),
            MessageType.WARMUP_START: re.compile(r"^Warmup:\s*(.*)$"),
            MessageType.SERVER_SHUTDOWN: re.compile(r"^ShutdownGame:\s*(.*)$"),
        }

        # Status parsing state
        self._parsing_status = False
        self._status_lines: List[str] = []
        self._status_line_count = 0
        self._status_header_detected = False
        self._status_client_count = 0
        self._seen_separator = False

        # Event tracking for shutdown type detection
        self._recent_fraglimit_hit = False
        self._recent_game_initialization = False

    def get_supported_message_types(self) -> List[MessageType]:
        """Return list of message types this processor can detect."""
        return [
            MessageType.CLIENT_CONNECT,
            MessageType.CLIENT_DISCONNECT,
            MessageType.GAME_INITIALIZATION,
            MessageType.GAME_END,
            MessageType.WARMUP_START,
            MessageType.SERVER_SHUTDOWN,
            MessageType.STATUS_UPDATE,
        ]

    def process_message(self, raw_message: str) -> ParsedMessage:
        """Process a server message and return parsed result."""
        raw_message = raw_message.strip()

        if not raw_message:
            return ParsedMessage(MessageType.UNKNOWN, raw_message)

        # Check client connecting
        match = self.patterns[MessageType.CLIENT_CONNECT].match(raw_message)
        if match:
            return self._handle_client_connecting(raw_message, match)

        # Check client disconnect
        match = self.patterns[MessageType.CLIENT_DISCONNECT].match(raw_message)
        if match:
            return self._handle_client_disconnect(raw_message, match)

        # Check game initialization
        match = self.patterns[MessageType.GAME_INITIALIZATION].match(raw_message)
        if match:
            return self._handle_game_initialization(raw_message)

        # Check fraglimit/timelimit hit
        match = self.patterns[MessageType.GAME_END].match(raw_message)
        if match:
            return self._handle_match_end(raw_message, match)

        # Check warmup state
        match = self.patterns[MessageType.WARMUP_START].match(raw_message)
        if match:
            return self._handle_warmup_state(raw_message, match)

        # Check shutdown game
        match = self.patterns[MessageType.SERVER_SHUTDOWN].match(raw_message)
        if match:
            return self._handle_shutdown_game(raw_message, match)

        # Check for status header
        if "num score ping name" in raw_message and "address" in raw_message:
            self.logger.debug("Detected status header, starting status parsing")
            self._parsing_status = True
            self._status_lines = []
            self._status_line_count = 0
            self._status_header_detected = True
            self._status_client_count = 0
            self._seen_separator = False
            return self._handle_status_line(raw_message)

        # Continue status parsing if in progress
        if self._parsing_status:
            return self._handle_status_line(raw_message)

        return ParsedMessage(MessageType.UNKNOWN, raw_message)

    def _handle_client_connecting(
        self, raw_message: str, match: re.Match
    ) -> ParsedMessage:
        """Handle client connecting message."""
        client_id = int(match.group(1))
        challenge_ping = int(match.group(2))

        self.logger.info(
            f"Client {client_id} connecting with {challenge_ping} challenge ping"
        )

        # Request status to get client IP information
        if self.send_command:
            self.logger.debug("Sending 'status' command to get client IP information")
            self.send_command("status")

        return ParsedMessage(
            MessageType.CLIENT_CONNECT,
            raw_message,
            {
                "client_id": client_id,
                "challenge_ping": challenge_ping,
                "needs_status_parse": True,
            },
        )

    def _handle_client_disconnect(
        self, raw_message: str, match: re.Match
    ) -> ParsedMessage:
        """Handle client disconnect message."""
        client_id = int(match.group(1))
        self.logger.info(f"Client {client_id} disconnected")

        return ParsedMessage(
            MessageType.CLIENT_DISCONNECT, raw_message, {"client_id": client_id}
        )

    def _handle_game_initialization(self, raw_message: str) -> ParsedMessage:
        """Handle game initialization message."""
        self.logger.info(
            "Game initialization detected - waiting to determine if warmup or match"
        )
        self._recent_game_initialization = True

        return ParsedMessage(
            MessageType.GAME_INITIALIZATION,
            raw_message,
            {"event": "game_initialization", "awaiting_type_determination": True},
        )

    def _handle_match_end(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle fraglimit/timelimit hit message."""
        reason = match.group(1).lower()
        self.logger.info(f"{reason.capitalize()} hit detected - match ended")
        self._recent_fraglimit_hit = True

        return ParsedMessage(
            MessageType.GAME_END,
            raw_message,
            {"event": "match_ended", "reason": reason},
        )

    def _handle_warmup_state(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle warmup state message."""
        warmup_info = match.group(1).strip() if match.group(1) else ""

        initialization_type = (
            "warmup_initialization"
            if self._recent_game_initialization
            else "warmup_only"
        )

        self.logger.info(
            f"Warmup state detected: '{warmup_info}' (type: {initialization_type})"
        )

        self._recent_fraglimit_hit = False
        self._recent_game_initialization = False

        return ParsedMessage(
            MessageType.WARMUP_START,
            raw_message,
            {
                "event": "warmup_started",
                "warmup_info": warmup_info,
                "is_active": True,
                "initialization_type": initialization_type,
                "follows_game_initialization": initialization_type
                == "warmup_initialization",
            },
        )

    def _handle_shutdown_game(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle shutdown game message."""
        shutdown_info = match.group(1).strip() if match.group(1) else ""

        is_match_end = self._recent_fraglimit_hit
        if self._recent_fraglimit_hit:
            event_type = "match_end"
            self.logger.info("ShutdownGame after fraglimit hit - match ended")
            self._recent_fraglimit_hit = False
        else:
            event_type = "warmup_end"
            self.logger.info("ShutdownGame without fraglimit - warmup ended")

        return ParsedMessage(
            MessageType.SERVER_SHUTDOWN,
            raw_message,
            {
                "event": event_type,
                "shutdown_info": shutdown_info,
                "is_match_end": is_match_end,
            },
        )

    def _handle_status_line(self, raw_message: str) -> ParsedMessage:
        """Handle server status output lines."""
        self._status_line_count += 1

        self.logger.debug(f"[STATUS] Line {self._status_line_count}: '{raw_message}'")

        # Empty line ends status parsing
        if len(raw_message) == 0:
            self.logger.info("Empty line detected, ending status parsing")
            return self._complete_status_parsing()

        self._status_lines.append(raw_message)

        # Separator line
        if raw_message.startswith("---"):
            self.logger.debug("Found separator line, client data starts next")
            self._seen_separator = True
            return ParsedMessage(MessageType.STATUS_UPDATE, raw_message)

        # Map line
        if raw_message.startswith("map:"):
            self.logger.debug(f"Found map line: {raw_message}")
            return ParsedMessage(MessageType.STATUS_UPDATE, raw_message)

        # Header line
        if raw_message.startswith("num score ping"):
            return ParsedMessage(MessageType.STATUS_UPDATE, raw_message)

        # Client data lines
        if self._seen_separator:
            if re.match(r"^\s*\d+\s+", raw_message):
                client_data = self._extract_client_from_status_line(raw_message)
                if client_data:
                    self._status_client_count += 1
                    self.logger.info(
                        f"[STATUS] Extracted client: ID={client_data.get('client_id')}, "
                        f"Name={client_data.get('name')}, IP={client_data.get('ip')}"
                    )
                    return ParsedMessage(
                        MessageType.STATUS_UPDATE,
                        raw_message,
                        {
                            "client_data": client_data,
                            "line_number": self._status_line_count,
                        },
                    )
            else:
                self.logger.info(
                    f"Non-client line detected, ending status parsing: '{raw_message}'"
                )
                return self._complete_status_parsing_and_reprocess(raw_message)

        return ParsedMessage(MessageType.STATUS_UPDATE, raw_message)

    def _extract_client_from_status_line(self, line: str) -> Optional[Dict]:
        """Extract client data from a server status line."""
        try:
            parts = line.split()
            self.logger.debug(f"[STATUS] Line parts: {parts}")

            if len(parts) < 6:
                self.logger.debug(f"Line has insufficient parts: {len(parts)}")
                return None

            # Status line format:
            # num score ping name lastmsg address qport rate
            #  0    1   2    3      4    5        6    7
            try:
                client_id = int(parts[0])
                score = int(parts[1])
                ping = int(parts[2])
                name = parts[3]
                lastmsg = int(parts[4])
                address = parts[5]
                qport = int(parts[6]) if parts[6] != "0" else 0
                rate = int(parts[7])
            except (ValueError, IndexError) as e:
                self.logger.debug(f"Error parsing line parts: {e}")
                return None

            if address == "bot":
                client_type = "BOT"
                ip_address = "bot"
            else:
                client_type = "HUMAN"
                ip_address = address.split(":")[0] if ":" in address else address
                if not self._is_valid_ip(ip_address):
                    self.logger.warning(f"Invalid IP format: {ip_address}")
                    return None

            return {
                "client_id": client_id,
                "score": score,
                "ping": ping,
                "name": name,
                "lastmsg": lastmsg,
                "ip": ip_address,
                "qport": qport,
                "rate": rate,
                "type": client_type,
            }

        except Exception as e:
            self.logger.error(f"Error extracting client from line '{line}': {e}")
            return None

    def _extract_client_data_from_status(self) -> List[Dict]:
        """Extract all client data from collected status lines."""
        client_data_list = []

        self.logger.info(f"Processing {len(self._status_lines)} status lines")

        for i, line in enumerate(self._status_lines, 1):
            if i <= 3:  # Skip map, headers, and separator lines
                continue

            client_data = self._extract_client_from_status_line(line)
            if client_data:
                existing = next(
                    (
                        c
                        for c in client_data_list
                        if c["client_id"] == client_data["client_id"]
                    ),
                    None,
                )
                if not existing:
                    client_data_list.append(client_data)

        human_clients = [c for c in client_data_list if c["type"] == "HUMAN"]
        bot_clients = [c for c in client_data_list if c["type"] == "BOT"]

        self.logger.info(
            f"Extracted {len(client_data_list)} total clients: "
            f"{len(human_clients)} humans, {len(bot_clients)} bots"
        )

        return client_data_list

    def _complete_status_parsing(self) -> ParsedMessage:
        """Complete status parsing and return status complete message."""
        self.logger.info(
            f"Status parsing complete. Processed {self._status_client_count} clients"
        )
        self._parsing_status = False
        client_data = self._extract_client_data_from_status()

        return ParsedMessage(
            MessageType.STATUS_UPDATE,
            "STATUS_COMPLETE",
            {"client_data": client_data, "status_complete": True},
        )

    def _complete_status_parsing_and_reprocess(
        self, raw_message: str
    ) -> ParsedMessage:
        """Complete status parsing and return the non-status message."""
        self.logger.info(
            f"Status parsing complete. Processed {self._status_client_count} clients"
        )
        self._parsing_status = False
        client_data = self._extract_client_data_from_status()

        if client_data:
            return ParsedMessage(
                MessageType.STATUS_UPDATE,
                "STATUS_COMPLETE",
                {"client_data": client_data, "status_complete": True},
            )
        else:
            return ParsedMessage(MessageType.UNKNOWN, raw_message)

    def _is_valid_ip(self, ip: str) -> bool:
        """Basic IP address validation."""
        try:
            parts = ip.split(".")
            return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts)
        except (ValueError, AttributeError):
            return False
