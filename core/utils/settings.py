import os

from dotenv import load_dotenv

load_dotenv()


def get_bool_env(key, default=False):
    return os.getenv(key, str(default)).lower() in ("true", "1", "yes")


nplayers_threshold = int(os.getenv("NPLAYERS_THRESHOLD", 1))
timelimit = int(os.getenv("TIMELIMIT", 2))
warmup_timelimit = int(os.getenv("WARMUP_TIMELIMIT", 5))
repeats = int(os.getenv("REPEATS", 1))

bot_enable = get_bool_env("BOT_ENABLE")
bot_count = int(os.getenv("BOT_COUNT", 4))
bot_difficulty = int(os.getenv("BOT_DIFFICULTY", 1))
bot_names = os.getenv("BOT_NAMES", "").split(",")

latencies = [int(lat) for lat in os.getenv("LATENCIES", "200").split(",")]
enable_latency_control = get_bool_env("ENABLE_LATENCY_CONTROL", False)

# OpenArena Game Configuration
flaglimit = int(os.getenv("FLAGLIMIT", 8))
warmup_time = int(os.getenv("WARMUP_TIME", 20))
enable_warmup = get_bool_env("ENABLE_WARMUP", True)

# OBS WebSocket settings
obs_port = os.getenv("OBS_PORT", "4455")
obs_password = os.getenv("OBS_PASSWORD", None)
obs_connection_timeout = os.getenv("OBS_CONNECTION_TIMEOUT", "30")
