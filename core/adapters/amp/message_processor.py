from __future__ import annotations

import logging
from typing import Callable, Dict, List, Optional

from core.adapters.base import BaseMessageProcessor, MessageType, ParsedMessage
from core.adapters.amp.status_parser import AMPStatusParser


class AMPMessageProcessor(BaseMessageProcessor):
    """
    Message processor for custom Quake-like server.
    """

    def __init__(self, send_command_callback: Optional[Callable[[str], None]] = None):
        super().__init__(send_command_callback)
        self.logger = logging.getLogger(__name__)

        self._status_parser = AMPStatusParser()
        self._status_client_count = 0

    def get_supported_message_types(self) -> List[MessageType]:
        return [
            MessageType.STATUS_UPDATE,
        ]

    def process_message(self, raw_message: str) -> ParsedMessage:
        raw_message = raw_message.strip()

        if not raw_message:
            if self._status_parser.is_parsing:
                return self._complete_status_parsing()
            return ParsedMessage(MessageType.UNKNOWN, raw_message)

        # Detect status header
        if self._status_parser.is_status_header(raw_message):
            self.logger.debug("Status header detected, starting parsing")
            self._status_parser.start_parsing()
            self._status_client_count = 0
            self._status_parser.add_line(raw_message)
            return ParsedMessage(MessageType.STATUS_UPDATE, raw_message)

        # Continue status parsing
        if self._status_parser.is_parsing:
            self._status_parser.add_line(raw_message)

            client = self._status_parser.parse_client_line(raw_message)
            if client:
                self._status_client_count += 1
                self.logger.info(
                    f"[STATUS] Client {client['client_id']} "
                    f"{client['name']} ({client['ip']})"
                )
                return ParsedMessage(
                    MessageType.STATUS_UPDATE,
                    raw_message,
                    {"client_data": client},
                )

            return ParsedMessage(MessageType.STATUS_UPDATE, raw_message)

        return ParsedMessage(MessageType.UNKNOWN, raw_message)

    def _complete_status_parsing(self) -> ParsedMessage:
        self.logger.info(
            f"Status parsing completed ({self._status_client_count} clients)"
        )

        clients: List[Dict] = []
        for line in self._status_parser.lines:
            client = self._status_parser.parse_client_line(line)
            if client:
                clients.append(client)

        self._status_parser.complete()

        return ParsedMessage(
            MessageType.STATUS_UPDATE,
            "STATUS_COMPLETE",
            {"clients": clients, "status_complete": True},
        )