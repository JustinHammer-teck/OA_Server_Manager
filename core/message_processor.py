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
        
        # Message patterns
        self.patterns = {
            MessageType.CLIENT_CONNECTING: re.compile(r"^Client ([0-9]+) connecting with ([0-9]+) challenge ping$"),
            MessageType.CLIENT_DISCONNECT: re.compile(r"^ClientDisconnect: ([0-9]+)$"),
            MessageType.GAME_INITIALIZATION: re.compile(r"^------- Game Initialization -------$"),
            MessageType.MATCH_END_FRAGLIMIT: re.compile(r"^Exit: Fraglimit hit\.$"),
            MessageType.WARMUP_STATE: re.compile(r"^Warmup:\s*(.*)$"),
            MessageType.SHUTDOWN_GAME: re.compile(r"^ShutdownGame:\s*(.*)$")
        }
        
        # Track status parsing state
        self._parsing_status = False
        self._status_lines = []
        self._status_line_count = 0
        
        # Track recent game events for context
        self._recent_fraglimit_hit = False
        self._recent_game_initialization = False
    
    def process_message(self, raw_message: str) -> ParsedMessage:
        """Process a server message and return parsed result."""
        raw_message = raw_message.strip()
        
        if not raw_message:
            return ParsedMessage(MessageType.UNKNOWN, raw_message)
        
        # Check for client connecting
        match = self.patterns[MessageType.CLIENT_CONNECTING].match(raw_message)
        if match:
            return self._handle_client_connecting(raw_message, match)
        
        # Check for client disconnect
        match = self.patterns[MessageType.CLIENT_DISCONNECT].match(raw_message)
        if match:
            return self._handle_client_disconnect(raw_message, match)
        
        # Check for game initialization
        match = self.patterns[MessageType.GAME_INITIALIZATION].match(raw_message)
        if match:
            return self._handle_game_initialization(raw_message, match)
        
        # Check for fraglimit hit
        match = self.patterns[MessageType.MATCH_END_FRAGLIMIT].match(raw_message)
        if match:
            return self._handle_fraglimit_hit(raw_message, match)
        
        # Check for warmup state
        match = self.patterns[MessageType.WARMUP_STATE].match(raw_message)
        if match:
            return self._handle_warmup_state(raw_message, match)
        
        # Check for shutdown game
        match = self.patterns[MessageType.SHUTDOWN_GAME].match(raw_message)
        if match:
            return self._handle_shutdown_game(raw_message, match)
        
        # Check if this is part of status output
        if self._parsing_status:
            return self._handle_status_line(raw_message)
        
        return ParsedMessage(MessageType.UNKNOWN, raw_message)
    
    def _handle_client_connecting(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle client connecting message."""
        client_id = int(match.group(1))
        challenge_ping = int(match.group(2))
        
        self.logger.info(f"Client {client_id} connecting with {challenge_ping} challenge ping")
        
        # Request status to get client IP information
        self.send_command("status")
        self._parsing_status = True
        self._status_lines = []
        self._status_line_count = 0
        
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
        
        # Set flag to track that we just saw a game initialization
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
        
        # Set flag for upcoming ShutdownGame message
        self._recent_fraglimit_hit = True
        
        return ParsedMessage(
            MessageType.MATCH_END_FRAGLIMIT,
            raw_message,
            {"event": "match_ended", "reason": "fraglimit"}
        )
    
    def _handle_warmup_state(self, raw_message: str, match: re.Match) -> ParsedMessage:
        """Handle warmup state message."""
        warmup_info = match.group(1).strip() if match.group(1) else ""
        
        # Check if this follows a recent game initialization
        initialization_type = "warmup_initialization" if self._recent_game_initialization else "warmup_only"
        
        self.logger.info(f"Warmup state detected: '{warmup_info}' (type: {initialization_type})")
        
        # Clear fraglimit flag when warmup starts
        self._recent_fraglimit_hit = False
        # Clear game initialization flag after determination
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
        
        # Determine if this is end of match or end of warmup based on recent events
        is_match_end = self._recent_fraglimit_hit
        if self._recent_fraglimit_hit:
            event_type = "match_end"
            self.logger.info("ShutdownGame after fraglimit hit - match ended")
            # Reset flag after processing
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
        """Handle server status output lines."""
        self._status_line_count += 1
        
        # Empty line signals end of status output
        if len(raw_message) == 0:
            self._parsing_status = False
            client_ips = self._extract_client_ips_from_status()
            
            return ParsedMessage(
                MessageType.STATUS_LINE,
                "STATUS_COMPLETE",
                {
                    "client_ips": client_ips,
                    "status_complete": True
                }
            )
        
        # Store status line for parsing
        self._status_lines.append(raw_message)
        
        # Parse client IP from status line (skip header lines)
        if self._status_line_count > 4:
            client_ip = self._extract_ip_from_status_line(raw_message)
            if client_ip:
                return ParsedMessage(
                    MessageType.STATUS_LINE,
                    raw_message,
                    {
                        "client_ip": client_ip,
                        "line_number": self._status_line_count
                    }
                )
        
        return ParsedMessage(MessageType.STATUS_LINE, raw_message)
    
    def _extract_ip_from_status_line(self, line: str) -> Optional[str]:
        """Extract IP address from a server status line."""
        try:
            parts = line.split()
            if len(parts) > 4:
                ip_part = parts[4]
                # Handle format like "192.168.1.100^7:27960"
                if "^7" in ip_part:
                    ip = ip_part.split("^7")[1].split(":")[0]
                    self.logger.debug(f"Extracted IP: {ip}")
                    return ip
                else:
                    # Handle other IP formats
                    ip = ip_part.split(":")[0]
                    if self._is_valid_ip(ip):
                        return ip
        except (IndexError, ValueError) as e:
            self.logger.debug(f"Could not extract IP from line: {line} - {e}")
        
        return None
    
    def _extract_client_ips_from_status(self) -> List[str]:
        """Extract all client IPs from collected status lines."""
        client_ips = []
        for line in self._status_lines:
            ip = self._extract_ip_from_status_line(line)
            if ip and ip not in client_ips:
                client_ips.append(ip)
        
        self.logger.info(f"Extracted {len(client_ips)} client IPs from status: {client_ips}")
        return client_ips
    
    def _is_valid_ip(self, ip: str) -> bool:
        """Basic IP address validation."""
        try:
            parts = ip.split('.')
            return (len(parts) == 4 and 
                   all(0 <= int(part) <= 255 for part in parts))
        except (ValueError, AttributeError):
            return False
    
    def reset_status_parsing(self) -> None:
        """Reset status parsing state."""
        self._parsing_status = False
        self._status_lines.clear()
        self._status_line_count = 0
    
    def is_parsing_status(self) -> bool:
        """Check if currently parsing status output."""
        return self._parsing_status
    
    def get_pattern_info(self) -> Dict[str, str]:
        """Get information about message patterns for debugging."""
        return {
            msg_type.name: pattern.pattern 
            for msg_type, pattern in self.patterns.items()
        }