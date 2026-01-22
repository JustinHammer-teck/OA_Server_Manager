# oa_reader.py
from __future__ import annotations
import threading
import re
from subprocess import Popen

class OAReader:
    """
    Reads stdout/stderr from a running OpenArena dedicated server (oa_ded.exe),
    detects client connect/disconnect events, and calls callbacks.
    """

    def __init__(self, server_process: Popen, 
                 stdout_callback=None, 
                 stderr_callback=None,
                 client_connect_callback=None,
                 client_disconnect_callback=None):
        """
        Args:
            server_process: Popen object of oa_ded.exe
            stdout_callback: called for every stdout line
            stderr_callback: called for every stderr line
            client_connect_callback: called with client_id, ping when client connects
            client_disconnect_callback: called with client_id when client disconnects
        """
        self.server_process = server_process
        self.stdout_callback = stdout_callback
        self.stderr_callback = stderr_callback
        self.client_connect_callback = client_connect_callback
        self.client_disconnect_callback = client_disconnect_callback
        self.running = False

    def start(self):
        """Start reading stdout/stderr in background threads."""
        self.running = True
        threading.Thread(target=self._read_stdout, daemon=True).start()
        threading.Thread(target=self._read_stderr, daemon=True).start()

    def stop(self):
        self.running = False

    def _read_stdout(self):
        for line in iter(self.server_process.stdout.readline, b''):
            if not self.running:
                break
            try:
                decoded_line = line.decode('utf-8', errors='replace').rstrip()
            except Exception:
                decoded_line = str(line)
            if self.stdout_callback:
                self.stdout_callback(decoded_line)
            self._parse_line(decoded_line)

    def _read_stderr(self):
        for line in iter(self.server_process.stderr.readline, b''):
            if not self.running:
                break
            try:
                decoded_line = line.decode('utf-8', errors='replace').rstrip()
            except Exception:
                decoded_line = str(line)
            if self.stderr_callback:
                self.stderr_callback(decoded_line)
            self._parse_line(decoded_line)

    def _parse_line(self, line: str):
        """Detect client connect/disconnect from line text."""
        # Example: "Client 3 connecting with 50 challenge ping"
        m = re.match(r"^Client (\d+) connecting with (\d+) challenge ping", line)
        if m:
            client_id = int(m.group(1))
            ping = int(m.group(2))
            if self.client_connect_callback:
                self.client_connect_callback(client_id, ping)
            return

        # Example: "ClientDisconnect: 3"
        m = re.match(r"^ClientDisconnect: (\d+)", line)
        if m:
            client_id = int(m.group(1))
            if self.client_disconnect_callback:
                self.client_disconnect_callback(client_id)
            return
