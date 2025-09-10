import logging
import signal
import sys

from core.server import Server

logger = logging.getLogger("OpenArenaServerUtil")

server = Server()


def signal_handler(sig, frame):
    """Handle Ctrl-C interrupts cleanly."""
    logger.warning("Interrupt signal received. Starting cleanup...")
    server.dispose()
    sys.exit(0)


def main():
    """Main execution function."""
    # Register the signal handler for Ctrl-C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        server.start_server()
        while True:
            msg = server.read_server()
            logger.info(f"{msg}")

    except Exception as e:
        logger.critical(f"An unhandled exception occurred: {e}", exc_info=True)
    finally:
        logger.info("Application is shutting down.")
        server.dispose()


if __name__ == "__main__":
    main()
