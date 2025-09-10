import logging
import signal
import sys

from core.server import Server
from core.network_utils import NetworkUtils

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("OpenArenaServerUtil")

server = Server()


def signal_handler(sig, frame):
    """Handle Ctrl-C interrupts cleanly."""
    logger.warning("Interrupt signal received. Starting cleanup...")
    
    # Clean up network rules
    try:
        interface = "enp1s0"  # Default interface
        NetworkUtils.dispose(interface)
        logger.info("Network rules cleaned up")
    except Exception as e:
        logger.error(f"Error cleaning up network rules: {e}")
    
    server.dispose()
    sys.exit(0)


def main():
    """Main execution function."""
    # Register the signal handler for Ctrl-C
    signal.signal(signal.SIGINT, signal_handler)
    
    logger.info("Starting OpenArena Server Management System")
    logger.info("========================================")

    try:
        # Start the OpenArena dedicated server
        server.start_server()
        logger.info("Server process started successfully")
        
        # Run the integrated message processing loop
        server.run_server_loop()
        
    except Exception as e:
        logger.critical(f"An unhandled exception occurred: {e}", exc_info=True)
    finally:
        logger.info("Application is shutting down.")
        
        # Clean up network rules
        try:
            interface = "enp1s0"
            NetworkUtils.dispose(interface)
            logger.info("Network rules cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up network rules: {e}")
        
        server.dispose()


if __name__ == "__main__":
    main()
