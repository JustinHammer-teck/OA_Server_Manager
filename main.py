import asyncio
import logging
import signal
import sys
import threading

from core.network_utils import NetworkUtils
from core.server import Server

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("OpenArenaServerUtil")

server = Server()
async_loop = None


def signal_handler(sig, frame):
    """Handle Ctrl-C interrupts cleanly."""
    logger.warning("Interrupt signal received. Starting cleanup...")

    # Clean up OBS connections
    if async_loop and async_loop.is_running():
        try:
            future = asyncio.run_coroutine_threadsafe(server.cleanup_obs_async(), async_loop)
            future.result(timeout=5)  # Wait up to 5 seconds for cleanup
        except Exception as e:
            logger.error(f"Error cleaning up OBS connections: {e}")

    # Clean up network rules
    try:
        interface = "enp1s0"  # Default interface
        NetworkUtils.dispose(interface)
        logger.info("Network rules cleaned up")
    except Exception as e:
        logger.error(f"Error cleaning up network rules: {e}")

    server.dispose()
    
    # Stop async loop
    if async_loop and async_loop.is_running():
        async_loop.call_soon_threadsafe(async_loop.stop)
    
    sys.exit(0)


def run_async_loop():
    """Run the async event loop in a separate thread."""
    global async_loop
    async_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(async_loop)
    
    # Set the loop in the server
    server.set_async_loop(async_loop)
    
    try:
        async_loop.run_forever()
    except Exception as e:
        logger.error(f"Async loop error: {e}")
    finally:
        async_loop.close()


def main():
    """Main execution function."""
    global async_loop
    
    signal.signal(signal.SIGINT, signal_handler)

    logger.info("Starting OpenArena Server Management System with OBS Integration")

    # Start async event loop in a separate thread
    async_thread = threading.Thread(target=run_async_loop, daemon=True)
    async_thread.start()
    
    # Wait a moment for async loop to start
    import time
    time.sleep(0.5)

    try:
        server.start_server()
        logger.info("Server process started successfully")
        logger.info("OBS WebSocket support enabled")

        server.run_server_loop()

    except Exception as e:
        logger.critical(f"An unhandled exception occurred: {e}", exc_info=True)
    finally:
        logger.info("Application is shutting down.")

        # Clean up OBS connections
        if async_loop and async_loop.is_running():
            try:
                future = asyncio.run_coroutine_threadsafe(server.cleanup_obs_async(), async_loop)
                future.result(timeout=5)
            except Exception as e:
                logger.error(f"Error cleaning up OBS connections: {e}")

        # Clean up network rules
        try:
            interface = "enp1s0"
            NetworkUtils.dispose(interface)
            logger.info("Network rules cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up network rules: {e}")

        server.dispose()
        
        # Stop async loop
        if async_loop and async_loop.is_running():
            async_loop.call_soon_threadsafe(async_loop.stop)
            async_thread.join(timeout=2)


if __name__ == "__main__":
    main()
