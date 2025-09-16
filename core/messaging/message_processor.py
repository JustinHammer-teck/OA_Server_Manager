import logging
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Callable
from enum import Enum


class MessageType(Enum):
    CLIENT_CONNECTING = "client_connecting"
    CLIENT_DISCONNECT = "client_disconnect"
    GAME_INITIALIZATION = "game_initialization"
    MATCH_END_FRAGLIMIT = "match_end_fraglimit"
    WARMUP_STATE = "warmup_state"
    SHUTDOWN_GAME = "shutdown_game"
    STATUS_LINE = "status_line"
    UNKNOWN = "unknown"


@dataclass
class ParsedMessage:
    """Represents a parsed server message."""
    message_type: MessageType
    raw_message: str
    data: Dict = None
    
    def __post_init__(self):
        if self.data is None:
            self.data = {}


class MessageProcessor:
    """Processes server messages and extracts game events."""
    
    def __init__(self, send_command_callback: Callable[[str], None]):
        self.send_command = send_command_callback
        self.logger = logging.getLogger(__name__)
        
        self.patterns = {
            MessageType.CLIENT_CONNECTING: re.compile(r"^Client ([0-9]+) connecting with ([0-9]+) challenge ping$"),
            MessageType.CLIENT_DISCONNECT: re.compile(r"^ClientDisconnect: ([0-9]+)$"),
            MessageType.GAME_INITIALIZATION: re.compile(r"^------- Game Initialization -------$"),
            MessageType.MATCH_END_FRAGLIMIT: re.compile(r"^Exit: Fraglimit hit\.$"),
            MessageType.WARMUP_STATE: re.compile(r"^Warmup:\s*(.*)$"),
            MessageType.SHUTDOWN_GAME: re.compile(r"^ShutdownGame:\s*(.*)$")
        }
        
        self._parsing_status = False
        self._status_lines = []
        self._status_line_count = 0
        self._status_header_detected = False
        self._status_client_count = 0
        self._seen_separator = False
        
        self._recent_fraglimit_hit = False
        self._recent_game_initialization = False
    
    def process_message(self, raw_message: str) -> ParsedMessage:
        """Process a server message and return parsed result."""
        raw_message = raw_message.strip()
        
        if not raw_message:
            return ParsedMessage(MessageType.UNKNOWN, raw_message)
        
        match = self.patterns[MessageType.CLIENT_CONNECTING].match(raw_message)
        if match:
            return self._handle_client_connecting(raw_message, match)
        
        match = self.patterns[MessageType.CLIENT_DISCONNECT].match(raw_message)
        if match:
            return self._handle_client_disconnect(raw_message, match)
        
        match = self.patterns[MessageType.GAME_INITIALIZATION].match(raw_message)
        if match:
            return self._handle_game_initialization(raw_message, match)
        
        match = self.patterns[MessageType.MATCH_END_FRAGLIMIT].match(raw_message)
        if match:
            return self._handle_fraglimit_hit(raw_message, match)
        
        match = self.patterns[MessageType.WARMUP_STATE].match(raw_message)
        if match:
            return self._handle_warmup_state(raw_message, match)
        
        match = self.patterns[MessageType.SHUTDOWN_GAME].match(raw_message)
        if match:
            return self._handle_shutdown_game(raw_message, match)
        
        if "num score ping name" in raw_message and "address" in raw_message:
            self.logger.debug(f"[STATUS] Detected status header, starting status parsing")
            self._parsing_status = True
            self._status_lines = []
            self._status_line_count = 0
            self._status_header_detected = True
            self._status_client_count = 0
            self._seen_separator = False
            return self._handle_status_line(raw_message)
        
        if self._parsing_status:
            return self._handle_status_line(raw_message)
        
        return ParsedMessage(MessageType.UNKNOWN, raw_message)
    
    def _handle_client_connecting(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle client connecting message."""
        client_id = int(match.group(1))
        challenge_ping = int(match.group(2))
        
        self.logger.info(f"Client {client_id} connecting with {challenge_ping} challenge ping")
        
        # Request status to get client IP information
        self.logger.debug(f"[STATUS] Sending 'status' command to get client IP information")
        self.send_command("status")
        
        return ParsedMessage(
            MessageType.CLIENT_CONNECTING,
            raw_message,
            {
                "client_id": client_id,
                "challenge_ping": challenge_ping,
                "needs_status_parse": True
            }
        )
    
    def _handle_client_disconnect(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle client disconnect message."""
        client_id = int(match.group(1))
        
        self.logger.info(f"Client {client_id} disconnected")
        
        return ParsedMessage(
            MessageType.CLIENT_DISCONNECT,
            raw_message,
            {"client_id": client_id}
        )
    
    def _handle_game_initialization(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle game initialization message."""
        self.logger.info("Game initialization detected - waiting to determine if warmup or match")
        
        self._recent_game_initialization = True
        
        return ParsedMessage(
            MessageType.GAME_INITIALIZATION,
            raw_message,
            {
                "event": "game_initialization",
                "awaiting_type_determination": True
            }
        )
    
    def _handle_fraglimit_hit(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle fraglimit hit message."""
        self.logger.info("Fraglimit hit detected - match ended")
        
        self._recent_fraglimit_hit = True
        
        return ParsedMessage(
            MessageType.MATCH_END_FRAGLIMIT,
            raw_message,
            {"event": "match_ended", "reason": "fraglimit"}
        )
    
    def _handle_warmup_state(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle warmup state message."""
        warmup_info = match.group(1).strip() if match.group(1) else ""
        
        initialization_type = "warmup_initialization" if self._recent_game_initialization else "warmup_only"
        
        self.logger.info(f"Warmup state detected: '{warmup_info}' (type: {initialization_type})")
        
        self._recent_fraglimit_hit = False
        self._recent_game_initialization = False
        
        return ParsedMessage(
            MessageType.WARMUP_STATE,
            raw_message,
            {
                "event": "warmup_started",
                "warmup_info": warmup_info,
                "is_active": True,
                "initialization_type": initialization_type,
                "follows_game_initialization": initialization_type == "warmup_initialization"
            }
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
            MessageType.SHUTDOWN_GAME,
            raw_message,
            {
                "event": event_type,
                "shutdown_info": shutdown_info,
                "is_match_end": is_match_end
            }
        )
    
    def _handle_status_line(self, raw_message: str) -> ParsedMessage:
        """Handle server status output lines with clean exit detection."""
        self._status_line_count += 1
        
        self.logger.debug(f"[STATUS] Line {self._status_line_count}: '{raw_message}'")
        
        if len(raw_message) == 0:
            self.logger.info(f"[STATUS] Empty line detected, ending status parsing")
            return self._complete_status_parsing()
        
        self._status_lines.append(raw_message)
        
        if raw_message.startswith("---"):
            self.logger.debug(f"[STATUS] Found separator line, client data starts next")
            self._seen_separator = True
            return ParsedMessage(MessageType.STATUS_LINE, raw_message)
        
        if raw_message.startswith("map:"):
            self.logger.debug(f"[STATUS] Found map line: {raw_message}")
            return ParsedMessage(MessageType.STATUS_LINE, raw_message)
        
        if raw_message.startswith("num score ping"):
            return ParsedMessage(MessageType.STATUS_LINE, raw_message)
        
        if self._seen_separator:
            if re.match(r'^\s*\d+\s+', raw_message):
                client_data = self._extract_client_from_status_line(raw_message)
                if client_data:
                    self._status_client_count += 1
                    self.logger.info(f"[STATUS] Extracted client: ID={client_data.get('client_id')}, Name={client_data.get('name')}, IP={client_data.get('ip')}, Type={client_data.get('type')}")
                    return ParsedMessage(
                        MessageType.STATUS_LINE,
                        raw_message,
                        {
                            "client_data": client_data,
                            "line_number": self._status_line_count
                        }
                    )
                else:
                    self.logger.debug(f"[STATUS] Could not parse client line: '{raw_message}'")
            else:
                self.logger.info(f"[STATUS] Non-client line detected, ending status parsing: '{raw_message}'")
                return self._complete_status_parsing_and_reprocess(raw_message)
        
        return ParsedMessage(MessageType.STATUS_LINE, raw_message)
    
    def _extract_client_from_status_line(self, line: str) -> Optional[dict]:
        """Extract client data from a server status line."""
        try:
            parts = line.split()
            self.logger.debug(f"[STATUS] Line parts: {parts}")
            
            if len(parts) < 6:
                self.logger.debug(f"[STATUS] Line has insufficient parts: {len(parts)}")
                return None
            
            # Status line format:
            # num score ping name lastmsg address qport rate
            #  0    1   2    3      4    5        6    7
            try:
                client_id = int(parts[0])
                score = int(parts[1])
                ping = int(parts[2])
                name = parts[3]  # May contain color codes
                lastmsg = int(parts[4])
                address = parts[5]  # IP address or "bot"
                qport = int(parts[6]) if parts[6] != '0' else 0
                rate = int(parts[7])
            except (ValueError, IndexError) as e:
                self.logger.debug(f"[STATUS] Error parsing line parts: {e}")
                return None
            
            if address == "bot":
                client_type = "BOT"
                ip_address = None
            else:
                client_type = "HUMAN"
                ip_address = address.split(":")[0] if ":" in address else address
                if not self._is_valid_ip(ip_address):
                    self.logger.warning(f"[STATUS] Invalid IP format: {ip_address}")
                    return None
            
            client_data = {
                "client_id": client_id,
                "score": score,
                "ping": ping,
                "name": name,
                "lastmsg": lastmsg,
                "ip": ip_address,
                "qport": qport,
                "rate": rate,
                "type": client_type
            }
            
            self.logger.debug(f"[STATUS] Extracted client data: {client_data}")
            return client_data
            
        except Exception as e:
            self.logger.error(f"[STATUS] Error extracting client from line '{line}': {e}")
            return None
    
    def _extract_client_data_from_status(self) -> List[dict]:
        """Extract all client data from collected status lines."""
        client_data_list = []
        
        self.logger.info(f"[STATUS] Processing {len(self._status_lines)} status lines")
        
        for i, line in enumerate(self._status_lines, 1):
            if i <= 3:  # Skip map, headers, and separator lines
                self.logger.debug(f"[STATUS] Skipping header line {i}: '{line}'")
                continue
                
            client_data = self._extract_client_from_status_line(line)
            if client_data:
                existing = next((c for c in client_data_list if c["client_id"] == client_data["client_id"]), None)
                if not existing:
                    client_data_list.append(client_data)
                else:
                    self.logger.debug(f"[STATUS] Duplicate client_id {client_data['client_id']}, skipping")
        
        human_clients = [c for c in client_data_list if c["type"] == "HUMAN"]
        bot_clients = [c for c in client_data_list if c["type"] == "BOT"]
        
        self.logger.info(f"[STATUS] Extracted {len(client_data_list)} total clients: {len(human_clients)} humans, {len(bot_clients)} bots")
        if human_clients:
            human_ips = [c["ip"] for c in human_clients]
            self.logger.info(f"[STATUS] Human client IPs: {human_ips}")
            
        return client_data_list
    
    def _complete_status_parsing(self) -> ParsedMessage:
        """Complete status parsing and return status complete message."""
        self.logger.info(f"[STATUS] Status parsing complete. Processed {self._status_client_count} clients")
        self._parsing_status = False
        client_data = self._extract_client_data_from_status()
        
        return ParsedMessage(
            MessageType.STATUS_LINE,
            "STATUS_COMPLETE",
            {
                "client_data": client_data,
                "status_complete": True
            }
        )
    
    def _complete_status_parsing_and_reprocess(self, raw_message: str) -> ParsedMessage:
        """Complete status parsing and return the non-status message for reprocessing."""
        self.logger.info(f"[STATUS] Status parsing complete. Processed {self._status_client_count} clients")
        self._parsing_status = False
        client_data = self._extract_client_data_from_status()
        
        if client_data:
            self.logger.debug(f"[STATUS] Sending status complete with {len(client_data)} clients")
            return ParsedMessage(
                MessageType.STATUS_LINE,
                "STATUS_COMPLETE",
                {
                    "client_data": client_data,
                    "status_complete": True
                }
            )
        else:
            return ParsedMessage(MessageType.UNKNOWN, raw_message)
    
    def _is_valid_ip(self, ip: str) -> bool:
        """Basic IP address validation."""
        try:
            parts = ip.split('.')
            return (len(parts) == 4 and 
                   all(0 <= int(part) <= 255 for part in parts))
        except (ValueError, AttributeError):
            return False