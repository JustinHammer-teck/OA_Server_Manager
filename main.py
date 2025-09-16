import os
import asyncio
import logging
import signal
import sys
import threading
import time



import core.utils.settings as settings
from core.network.network_utils import NetworkUtils
from core.server.server import Server

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("OpenArenaServerUtil")

server = Server()
async_loop = None
interface = settings.interface


def signal_handler(sig, frame):
    """Handle exit signals (SIGINT, SIGTERM) cleanly."""
    signal_name = "SIGTERM" if sig == signal.SIGTERM else "SIGINT"
    logger.warning(f"{signal_name} received. Starting graceful shutdown...")

    def force_exit():
        time.sleep(10)  # 10 second timeout
        logger.error("Forced shutdown after timeout")
        os._exit(1)

    timeout_thread = threading.Thread(target=force_exit, daemon=True)
    timeout_thread.start()

    try:
        if async_loop and async_loop.is_running():
            try:
                future = asyncio.run_coroutine_threadsafe(
                    server.cleanup_obs_async(), async_loop
                )
                future.result(timeout=5)
            except Exception as e:
                logger.error(f"Error cleaning up OBS connections: {e}")

        try:
            NetworkUtils.dispose(interface)
            logger.info("Network rules cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up network rules: {e}")

        server.dispose()

        if async_loop and async_loop.is_running():
            async_loop.call_soon_threadsafe(async_loop.stop)

        logger.info("Graceful shutdown completed")
        sys.exit(0)

    except Exception as e:
        logger.error(f"Error during shutdown: {e}")
        sys.exit(1)


def run_async_loop():
    """Run the async event loop in a separate thread."""
    global async_loop
    async_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(async_loop)

    server.set_async_loop(async_loop)

    def exception_handler(loop, context):
        """Handle unhandled exceptions in the async loop."""
        exception = context.get('exception')
        if exception:
            logger.error(f"Unhandled exception in async loop: {exception}", exc_info=True)
        else:
            logger.error(f"Async loop error: {context['message']}")

    async_loop.set_exception_handler(exception_handler)

    try:
        logger.info("Starting async event loop")
        async_loop.run_forever()
    except Exception as e:
        logger.error(f"Fatal async loop error: {e}", exc_info=True)
    finally:
        logger.info("Async event loop closing")
        async_loop.close()

def main():
    """Main execution function."""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("Starting OpenArena Server Management System with OBS Integration")

    async_thread = threading.Thread(target=run_async_loop, daemon=True)
    async_thread.start()

    import time

    time.sleep(0.2)

    try:
        server.start_server()
        logger.info("Server process started successfully")
        server.run_server_loop()

    except Exception as e:
        logger.critical(f"An unhandled exception occurred: {e}", exc_info=True)
    finally:
        logger.info("Application is shutting down.")

        if async_loop and async_loop.is_running():
            try:
                future = asyncio.run_coroutine_threadsafe(
                    server.cleanup_obs_async(), async_loop
                )
                future.result(timeout=5)
            except Exception as e:
                logger.error(f"Error cleaning up OBS connections: {e}")

        try:
            NetworkUtils.dispose(interface)
            logger.info("Network rules cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up network rules: {e}")

        server.dispose()

        if async_loop and async_loop.is_running():
            async_loop.call_soon_threadsafe(async_loop.stop)
            async_thread.join(timeout=2)


if __name__ == "__main__":
    main()
