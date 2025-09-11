import argparse
import asyncio
import logging
import signal
import sys
import threading

import core.settings as settings
from core.network_utils import NetworkUtils
from core.server import Server

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("OpenArenaServerUtil")

server = Server()
async_loop = None
interface = "eno2"


def signal_handler(sig, frame):
    """Handle Ctrl-C interrupts cleanly."""
    logger.warning("Interrupt signal received. Starting cleanup...")

    # Clean up OBS connections
    if async_loop and async_loop.is_running():
        try:
            future = asyncio.run_coroutine_threadsafe(
                server.cleanup_obs_async(), async_loop
            )
            future.result(timeout=5)  # Wait up to 5 seconds for cleanup
        except Exception as e:
            logger.error(f"Error cleaning up OBS connections: {e}")

    # Clean up network rules
    try:
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


def parse_arguments():
    """Parse command line arguments for bot configuration."""
    parser = argparse.ArgumentParser(
        description="OpenArena Server Management System with OBS Integration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --bots 6 --difficulty 3 --bot-names "Sarge,Bones,Slash"
  python main.py --add-bots 2 --bot-difficulty 4
  python main.py --no-bots
        """,
    )

    # Bot configuration options
    bot_group = parser.add_argument_group("Bot Configuration")
    bot_group.add_argument(
        "--bots",
        type=int,
        help=f"Number of bots to add (default: {settings.bot_count})",
    )
    bot_group.add_argument(
        "--difficulty",
        "--bot-difficulty",
        type=int,
        choices=range(1, 6),
        help=f"Bot difficulty level 1-5 (default: {settings.bot_difficulty})",
    )
    bot_group.add_argument(
        "--bot-names",
        type=str,
        help=f"Comma-separated bot names (default: {','.join(settings.bot_names) if settings.bot_names[0] else 'Sarge,Bones,Slash,Grunt,Major'})",
    )
    bot_group.add_argument(
        "--add-bots", type=int, help="Add additional bots to default count"
    )
    bot_group.add_argument(
        "--no-bots", action="store_true", help="Disable bots completely"
    )

    # Server configuration
    server_group = parser.add_argument_group("Server Configuration")
    server_group.add_argument(
        "--interface",
        type=str,
        default="eno2",
        help="Network interface for latency control (default: eno2)",
    )

    return parser.parse_args()


def configure_bots_from_args(args):
    """Configure bot settings based on command line arguments."""
    bot_config = {
        "enable": not args.no_bots,  # Disable if --no-bots flag is set
        "count": settings.bot_count,
        "difficulty": settings.bot_difficulty,
        "names": settings.bot_names
        if settings.bot_names[0]
        else ["Sarge", "Bones", "Slash", "Grunt", "Major", "Ranger"],
    }

    if args.no_bots:
        bot_config["enable"] = False
        bot_config["count"] = 0
        return bot_config

    if args.bots is not None:
        bot_config["count"] = args.bots

    elif args.add_bots is not None:
        bot_config["count"] = settings.bot_count + args.add_bots

    if args.difficulty is not None:
        bot_config["difficulty"] = args.difficulty

    if args.bot_names:
        bot_config["names"] = [name.strip() for name in args.bot_names.split(",")]

    if bot_config["count"] > 0:
        bot_config["enable"] = True

    return bot_config


def main():
    """Main execution function."""
    global async_loop, interface

    args = parse_arguments()

    signal.signal(signal.SIGINT, signal_handler)

    bot_config = configure_bots_from_args(args)
    interface = args.interface  # Update global interface

    logger.info("Starting OpenArena Server Management System with OBS Integration")
    logger.info(f"Bot Configuration: {bot_config}")

    async_thread = threading.Thread(target=run_async_loop, daemon=True)
    async_thread.start()

    import time

    time.sleep(0.2)

    try:
        server.configure_bots(bot_config)
        server.configure_interface(interface)
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
                future = asyncio.run_coroutine_threadsafe(
                    server.cleanup_obs_async(), async_loop
                )
                future.result(timeout=5)
            except Exception as e:
                logger.error(f"Error cleaning up OBS connections: {e}")

        # Clean up network rules
        try:
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
