# oa_output_reader.py
from __future__ import annotations
import threading
import sys

def read_stdout(process, callback):
    """Đọc stdout liên tục từ process và gửi về callback"""
    for line in iter(process.stdout.readline, b''):
        try:
            decoded = line.decode('utf-8', errors='replace').rstrip()
            callback(decoded)
        except Exception as e:
            print(f"Error reading stdout: {e}", file=sys.stderr)

def read_stderr(process, callback):
    """Đọc stderr liên tục từ process và gửi về callback"""
    for line in iter(process.stderr.readline, b''):
        try:
            decoded = line.decode('utf-8', errors='replace').rstrip()
            callback(decoded)
        except Exception as e:
            print(f"Error reading stderr: {e}", file=sys.stderr)

def start_reader_threads(process, stdout_callback, stderr_callback):
    """Khởi chạy 2 thread đọc stdout và stderr"""
    threading.Thread(
        target=read_stdout, 
        args=(process, stdout_callback),
        daemon=True
    ).start()

    threading.Thread(
        target=read_stderr, 
        args=(process, stderr_callback),
        daemon=True
    ).start()
