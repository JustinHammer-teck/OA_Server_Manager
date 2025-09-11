# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

- Do not comment for the obvious method that do that think. Use comment when it has to be there. Don't use too much comment in the code.

## Project Overview
This is an OpenArena (OA) game server management system designed for network latency experiments and performance monitoring. The project is undergoing refactoring from a procedural script (`server_script.py`) to a modern OOP architecture for better modularity, extensibility, and integration with external systems.

## Project Structure

```
.
├── CLAUDE.md
├── LATENCY_INVESTIGATION.md
├── OA_CMDS_CONFIGS.md
├── OBS_INTEGRATION_PLAN.md
├── OBS_WEBSOCKET.md
├── README.md
├── core
│   ├── __init__.py
│   ├── bot_manager.py
│   ├── client_manager.py
│   ├── display_utils.py
│   ├── game_config_manager.py
│   ├── game_state_manager.py
│   ├── latency_manager.py
│   ├── message_processor.py
│   ├── network_utils.py
│   ├── obs_connection_manager.py
│   ├── obs_controller.py
│   ├── obs_manager.py
│   ├── server.py
│   ├── server.py.bak
│   └── settings.py
├── tests
│   ├── README.md
│   ├── __init__.py
│   ├── obs_test.py
│   └── test_obs_connection.py
├── flake.lock
├── flake.nix
├── main.py
├── package.json
├── pnpm-lock.yaml
├── pyproject.toml
├── server_script.py
└── uv.lock
```
## Commands

### Development and Testing
```bash
# Install dependencies
uv sync  # or pip install -e .

# Run the refactored OOP server
python main.py

# Run the legacy procedural server (for reference)
python server_script.py --interface enp1s0 --bots 4 --difficulty 3

# Install Node.js dependencies (Claude Code integration)
pnpm install
```

### Configuration Management

Server behavior controlled via `.env` file:

**Core Settings:**
- `NPLAYERS_THRESHOLD`: Minimum human players before starting experiments
- `TIMELIMIT`: Duration of gameplay rounds in minutes  
- `WARMUP_TIMELIMIT`: Warmup phase duration
- `REPEATS`: Number of experimental sequence repetitions

**Bot Configuration:**
- `BOT_ENABLE`: Enable/disable bot management
- `BOT_COUNT`: Number of bots to add
- `BOT_DIFFICULTY`: Bot difficulty level (1-5)
- `BOT_NAMES`: Comma-separated list of bot names

**Network Configuration:**
- `LATENCIES`: Comma-separated latency values in milliseconds
- `INTERFACE`: Network interface for traffic control (default: enp1s0)

**Planned OBS Integration Settings:**
- `OBS_WEBSOCKET_PORT`: Default OBS WebSocket port
- `OBS_PASSWORD`: Authentication for OBS WebSocket connections
- `RECORDING_FORMAT`: Output format for synchronized recordings
- `SYNC_BUFFER_TIME`: Buffer time for recording synchronization

## Implementation Requirements

### Linux System Dependencies
**Core Network Tools** (Required for latency simulation):
- **`iproute2`** - Provides `tc` (traffic control) command for network shaping
  ```bash
  sudo apt-get install iproute2    # Debian/Ubuntu
  sudo dnf install iproute-tc      # Fedora/RHEL
  ```

- **`nftables`** - Modern Linux firewall for packet marking and filtering
  ```bash
  sudo apt-get install nftables    # Debian/Ubuntu  
  sudo dnf install nftables        # Fedora/RHEL
  ```

**System Privileges**:
- **`sudo`** access required for network operations:
  - `/usr/bin/sudo /sbin/tc` - Traffic control commands
  - `/usr/bin/sudo nft` - Netfilter table operations
  - Network interface manipulation

**Game Server**:
- **OpenArena dedicated server** (`oa_ded`) installed and available in PATH
  ```bash
  # Install OpenArena (varies by distribution)
  sudo apt-get install openarena-server    # Debian/Ubuntu
  sudo dnf install openarena               # Fedora
  ```

**Configuration Files**:
- Server configuration files (e.g., `andrew_server.cfg`, `t_server.cfg`)
- Map rotation and game settings files

### Python Dependencies
**Runtime Requirements**:
- **Python 3.13+** (specified in pyproject.toml)
- **`python-dotenv`** - Environment variable management

**Installation**:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install python-dotenv
```

### Network Interface Requirements
**Network Configuration**:
- Physical or virtual network interface (default: `enp1s0`)
- Interface must be configurable with `tc` rules
- Root privileges for network manipulation

**Verification Commands**:
```bash
# Check if tc is available
which tc
# Check if nft is available  
which nft
# Check network interfaces
ip link show
# Test sudo access
sudo -v
```
- Only Implement a small feature at time do not thinking too far and make it over broad.