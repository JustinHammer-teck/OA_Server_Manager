"""Dota 2-specific message parsing."""

import logging
import re
from typing import Callable, Dict, List, Optional

from core.adapters.base import BaseMessageProcessor, MessageType, ParsedMessage


class Dota2MessageProcessor(BaseMessageProcessor):
    """
    Dota 2 server output parsing.

    Parses RCON responses and status poll output from Dota 2 servers.
    Unlike OpenArena which has continuous stderr output, Dota 2
    communication is primarily request/response via RCON.

    Game states in Dota 2:
    - DOTA_GAMERULES_STATE_INIT
    - DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD
    - DOTA_GAMERULES_STATE_HERO_SELECTION
    - DOTA_GAMERULES_STATE_STRATEGY_TIME
    - DOTA_GAMERULES_STATE_PRE_GAME
    - DOTA_GAMERULES_STATE_GAME_IN_PROGRESS
    - DOTA_GAMERULES_STATE_POST_GAME
    - DOTA_GAMERULES_STATE_DISCONNECT
    """

    def __init__(self, send_command_callback: Optional[Callable[[str], None]] = None):
        super().__init__(send_command_callback)
        self.logger = logging.getLogger(__name__)

        # Dota 2-specific patterns
        self.patterns = {
            # Status poll response parsing
            MessageType.STATUS_UPDATE: re.compile(
                r"^STATUS_POLL:(.*)$", re.DOTALL
            ),
            # Player connection
            MessageType.CLIENT_CONNECT: re.compile(
                r"^Client\s+'([^']+)'\s+connected\s+from\s+(\d+\.\d+\.\d+\.\d+)"
            ),
            # Player disconnection
            MessageType.CLIENT_DISCONNECT: re.compile(
                r"^Dropped\s+([^\s]+)\s+from\s+server"
            ),
            # Game state changes
            MessageType.GAME_START: re.compile(
                r"^Game\s+state\s+changed\s+to\s+DOTA_GAMERULES_STATE_GAME_IN_PROGRESS$"
            ),
            MessageType.GAME_END: re.compile(
                r"^Game\s+state\s+changed\s+to\s+DOTA_GAMERULES_STATE_POST_GAME$"
            ),
            MessageType.WARMUP_START: re.compile(
                r"^Game\s+state\s+changed\s+to\s+DOTA_GAMERULES_STATE_(HERO_SELECTION|STRATEGY_TIME|PRE_GAME)$"
            ),
            # Server shutdown
            MessageType.SERVER_SHUTDOWN: re.compile(
                r"^(Server\s+shutting\s+down|DOTA_GAMERULES_STATE_DISCONNECT)$"
            ),
        }

        # Track current game state
        self._current_game_state: Optional[str] = None
        self._last_player_count: int = 0

    def get_supported_message_types(self) -> List[MessageType]:
        """Return list of message types this processor can detect."""
        return [
            MessageType.CLIENT_CONNECT,
            MessageType.CLIENT_DISCONNECT,
            MessageType.GAME_START,
            MessageType.GAME_END,
            MessageType.WARMUP_START,
            MessageType.SERVER_SHUTDOWN,
            MessageType.STATUS_UPDATE,
        ]

    def process_message(self, raw_message: str) -> ParsedMessage:
        """Parse Dota 2 server output."""
        raw_message = raw_message.strip()

        if not raw_message:
            return ParsedMessage(MessageType.UNKNOWN, raw_message)

        # Handle status poll responses
        if raw_message.startswith("STATUS_POLL:"):
            return self._parse_status_poll(raw_message[12:])

        # Check other patterns
        for msg_type, pattern in self.patterns.items():
            if msg_type == MessageType.STATUS_UPDATE:
                continue  # Already handled above

            match = pattern.match(raw_message)
            if match:
                return self._create_parsed_message(msg_type, raw_message, match)

        return ParsedMessage(MessageType.UNKNOWN, raw_message)

    def _create_parsed_message(
        self, msg_type: MessageType, raw_message: str, match: re.Match
    ) -> ParsedMessage:
        """Create a ParsedMessage from a regex match."""
        data: Dict = {}

        if msg_type == MessageType.CLIENT_CONNECT:
            data = {
                "name": match.group(1),
                "ip": match.group(2),
            }
            self.logger.info(f"Client connected: {data['name']} from {data['ip']}")

        elif msg_type == MessageType.CLIENT_DISCONNECT:
            data = {"name": match.group(1)}
            self.logger.info(f"Client disconnected: {data['name']}")

        elif msg_type == MessageType.GAME_START:
            data = {"event": "game_started"}
            self._current_game_state = "GAME_IN_PROGRESS"
            self.logger.info("Dota 2 game started")

        elif msg_type == MessageType.GAME_END:
            data = {"event": "game_ended"}
            self._current_game_state = "POST_GAME"
            self.logger.info("Dota 2 game ended")

        elif msg_type == MessageType.WARMUP_START:
            phase = match.group(1)
            data = {
                "event": "warmup_started",
                "phase": phase,
            }
            self._current_game_state = phase
            self.logger.info(f"Dota 2 pre-game phase: {phase}")

        elif msg_type == MessageType.SERVER_SHUTDOWN:
            data = {"event": "server_shutdown"}
            self.logger.info("Dota 2 server shutting down")

        return ParsedMessage(msg_type, raw_message, data)

    def _parse_status_poll(self, status_output: str) -> ParsedMessage:
        """
        Parse Dota 2 status command output.

        Dota 2 status format typically includes:
        - hostname: Server name
        - version: Server version
        - map: Current map
        - players: X humans, Y bots (Z/MAX)
        - Player table with: userid name steamid connected ping loss state rate
        """
        data: Dict = {
            "raw_status": status_output,
            "players": [],
        }

        lines = status_output.strip().split("\n")
        in_player_section = False

        for line in lines:
            line = line.strip()

            # Parse server info lines
            if line.startswith("hostname:"):
                data["hostname"] = line.split(":", 1)[1].strip()
            elif line.startswith("map"):
                # Format: map     : mapname at: x y z
                parts = line.split(":")
                if len(parts) >= 2:
                    data["map"] = parts[1].strip().split()[0]
            elif line.startswith("players"):
                # Format: players : X humans, Y bots (Z/MAX)
                match = re.search(r"(\d+)\s+humans?,\s*(\d+)\s+bots?\s*\((\d+)/(\d+)\)", line)
                if match:
                    data["human_count"] = int(match.group(1))
                    data["bot_count"] = int(match.group(2))
                    data["player_count"] = int(match.group(3))
                    data["max_players"] = int(match.group(4))

            # Detect player table header
            elif "userid" in line and "name" in line:
                in_player_section = True
                continue

            # Parse player lines
            elif in_player_section and line and not line.startswith("#"):
                player = self._parse_player_line(line)
                if player:
                    data["players"].append(player)

        # Detect state changes based on player count
        current_count = len(data.get("players", []))
        if current_count != self._last_player_count:
            data["player_count_changed"] = True
            data["previous_count"] = self._last_player_count
            self._last_player_count = current_count

        return ParsedMessage(
            MessageType.STATUS_UPDATE,
            status_output,
            data,
        )

    def _parse_player_line(self, line: str) -> Optional[Dict]:
        """
        Parse a player line from status output.

        Expected format:
        # userid name steamid connected ping loss state rate
        """
        try:
            # Remove leading # if present
            if line.startswith("#"):
                line = line[1:].strip()

            parts = line.split()
            if len(parts) < 4:
                return None

            # Try to parse as player data
            player = {
                "userid": parts[0],
                "name": parts[1],
            }

            # Parse additional fields if present
            if len(parts) >= 3:
                player["steamid"] = parts[2]
            if len(parts) >= 4:
                player["connected"] = parts[3]
            if len(parts) >= 5:
                try:
                    player["ping"] = int(parts[4])
                except ValueError:
                    player["ping"] = 0
            if len(parts) >= 6:
                player["loss"] = parts[5]
            if len(parts) >= 7:
                player["state"] = parts[6]
            if len(parts) >= 8:
                try:
                    player["rate"] = int(parts[7])
                except ValueError:
                    player["rate"] = 0

            # Determine if bot
            steamid = player.get("steamid", "")
            player["is_bot"] = "BOT" in steamid.upper() or steamid == "0"

            return player

        except Exception as e:
            self.logger.debug(f"Failed to parse player line '{line}': {e}")
            return None

    def get_current_game_state(self) -> Optional[str]:
        """Get the current tracked game state."""
        return self._current_game_state
