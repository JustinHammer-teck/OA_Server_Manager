import logging
import os
import signal
import sys
from enum import Enum

from dotenv import load_dotenv


class ServerState(Enum):
    WAITING = 1
    WARMUP = 2
    RUNNING = 3


logger = logging.getLogger("OpenArenaServerUtil")

load_dotenv()

nplayers_threshold = int(os.getenv("NPLAYERS_THRESHOLD", 2))
timelimit = int(os.getenv("TIMELIMIT", 2))
warmup_timelimit = int(os.getenv("WARMUP_TIMELIMIT", 5))
repeats = int(os.getenv("REPEATS", 1))

bot_count = int(os.getenv("BOT_COUNT", 4))
bot_difficulty = int(os.getenv("BOT_DIFFICULTY", 1))
bot_names = os.getenv("BOT_NAMES", "").split(",")

latencies = [int(lat) for lat in os.getenv("LATENCIES", "200").split(",")]


def signal_handler(sig, frame):
    """Handle Ctrl-C interrupts cleanly."""
    logger.warning("Interrupt signal received. Starting cleanup...")
    manager.cleanup()
    sys.exit(0)


def main():
    """Main execution function."""
    # Register the signal handler for Ctrl-C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        manager.start_server()
        manager.run()
    except Exception as e:
        logger.critical(f"An unhandled exception occurred: {e}", exc_info=True)
    finally:
        logger.info("Application is shutting down.")
        manager.cleanup()


if __name__ == "__main__":
    main()
