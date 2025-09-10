# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is an OpenArena (OA) game server management system designed for network latency experiments and performance monitoring. The project is undergoing refactoring from a procedural script (`server_script.py`) to a modern OOP architecture for better modularity, extensibility, and integration with external systems.

## Project Structure

```
.
├── CLAUDE.md
├── README.md
├── core
│   ├── __init__.py
│   ├── network_utils.py
│   ├── server.py
│   └── settings.py
├── flake.lock
├── flake.nix
├── main.py
├── package.json
├── pnpm-lock.yaml
├── pyproject.toml
├── server_script.py
└── uv.lock
```

## Refactoring Goals

### Current State
- **`server_script.py`**: **REFERENCE ONLY** - Legacy monolithic procedural script (438 lines) - DO NOT MODIFY, use as source for refactoring
- **`core/`**: Partially refactored modular components (Server, NetworkUtils, settings)
- **`main.py`**: New OOP entry point using the Server class

### Target Architecture
1. **Complete OOP Refactoring**: Convert all procedural logic to object-oriented design
2. **Client Management System**: Track and manage individual client connections with IP mapping
3. **Latency Configuration**: Dynamic per-client latency management for experimental sequences
4. **OBS Integration**: WebSocket-based recording synchronization with client OBS instances
5. **Experiment Orchestration**: Automated management of 6-10 match experimental sequences

## Planned Features

### 1. Client Management System
- **ClientManager Class**: Track connected clients with IP addresses, connection states, and metadata
- **Client Dictionary**: Maintain persistent mapping of client IPs to OBS instances and experiment data
- **Connection Monitoring**: Real-time tracking of client join/disconnect events

### 2. OBS WebSocket Integration
- **OBS Controller**: WebSocket communication with client OBS instances for synchronized recording
- **Recording Coordination**: Automatic start/stop recording based on match state transitions
- **Multi-Client Sync**: Simultaneous control of multiple client recording sessions

### 3. Advanced Latency Configuration
- **Match-Based Profiles**: Configure different latency settings for each match in experimental sequence
- **Per-Client Latency**: Individual latency assignment to each connected client
- **Rotation Strategies**: Support multiple latency distribution algorithms (round-robin, random, fixed patterns)
- **Configuration Templates**: Pre-defined latency profiles for common experimental scenarios

### 4. Experiment Management
- **Sequence Configuration**: Define 6-10 match experimental sequences with varying network conditions
- **Data Collection Sync**: Coordinate data collection between server metrics and client recordings
- **Match State Machine**: Enhanced state management (WAITING → WARMUP → RUNNING → RECORDING → ANALYSIS)
- **Automated Progression**: Handle match transitions and experiment sequencing

## Current Architecture

### Core Components
- **`main.py`**: Refactored entry point using modular Server class
- **`core/server.py`**: Server class with state management, bot control, and process handling
- **`core/settings.py`**: Environment-based configuration using dotenv
- **`core/network_utils.py`**: Network latency simulation using tc/nftables

### Key Architecture Patterns
1. **State Machine**: Server operates in phases (WAITING, WARMUP, RUNNING) for experiment control
2. **Environment Configuration**: All settings externalized to `.env` file
3. **Process Management**: Uses subprocess.Popen for `oa_ded` dedicated server control
4. **Network Simulation**: Linux traffic control for per-client latency application

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

### Server Dependencies
- OpenArena dedicated server (`oa_ded`) installed and in PATH
- Linux system with `tc` (traffic control) and `nftables`
- Root/sudo access for network rule management
- Server configuration files (e.g., `andrew_server.cfg`, `t_server.cfg`)

### Future Dependencies
- WebSocket libraries for OBS communication (`obs-websocket-py`)
- Async frameworks for concurrent client management (`asyncio`)
- JSON configuration files for experiment templates

## Key Implementation Details

### Current Server Management
- **Process Control**: Server class manages `oa_ded` lifecycle with stdin command sending
- **Output Monitoring**: Real-time parsing of server stderr for game state detection
- **Network Latency**: `NetworkUtils.apply_latency_rules()` uses tc/HTB queuing with nftables

### Planned Client Management
- **IP Tracking**: Parse server status output to maintain client IP registry
- **OBS Mapping**: Associate each client IP with corresponding OBS WebSocket endpoint
- **State Synchronization**: Coordinate match state changes with recording control

### Experiment Sequencing
- **Match Progression**: Automatic transition through experimental match sequence
- **Latency Rotation**: Apply different network conditions for each match
- **Data Collection**: Synchronized start/stop of server logging and client recording

### WebSocket Architecture
- **Async Communication**: Non-blocking WebSocket connections to multiple OBS instances
- **Command Queue**: Buffered command system for reliable recording control
- **Error Handling**: Robust connection management with reconnection strategies

## Current Refactoring Progress

### ✅ **Completed Components** (133 lines total):
1. **`core/server.py`**: Basic Server class with:
   - Server process management (`start_server`, `dispose`)
   - Command sending (`send_command`)
   - Bot management (`add_bots`)
   - Basic state tracking (`ServerState` enum)

2. **`core/settings.py`**: Configuration management with environment variables

3. **`core/network_utils.py`**: Network latency utilities (`NetworkUtils` class)

4. **`main.py`**: Simple OOP entry point (38 lines)

### ❌ **Missing Key Components** (from 437-line `server_script.py`):

1. **Client Management System**:
   - IP address tracking and parsing from server status
   - Client connection/disconnection handling
   - Player list management

2. **Game State Machine Logic**:
   - Complex match state transitions (WAITING → WARMUP → RUNNING)
   - Round progression and experiment sequencing
   - Match timing and progression logic

3. **Server Message Processing**:
   - Real-time parsing of server stderr output
   - Pattern matching for client connections, disconnections, map changes
   - Game event detection (e.g., "AAS initialized", "ClientDisconnect")

4. **Experiment Management**:
   - Latency rotation between matches
   - Match counting and sequence control
   - Automated progression through experimental phases

5. **Signal Handling & Cleanup**:
   - Proper SIGINT handling for graceful shutdown
   - Network rule cleanup on exit

6. **Missing Properties/Methods** in Server class:
   - `nplayers_threshold` property (referenced at server.py:68,71 but not defined)
   - `server_process` property (referenced at server.py:82 but not defined) 
   - Message processing loop (main game loop)

### 🚧 **Current Bugs to Fix**:
- `server.py:68,71`: References undefined `self.nplayers_threshold`
- `server.py:82`: References undefined `self.server_process` 
- `server.py:130`: Incorrect encoding in `send_command`

## Implementation Roadmap

### **Phase 1: Fix Current Issues** (Priority: High)
1. **Fix Server class bugs**:
   - Add missing `nplayers_threshold` property
   - Fix `server_process` property reference
   - Fix encoding issue in `send_command`

2. **Complete basic Server functionality**:
   - Add server message processing loop
   - Implement proper state management integration

### **Phase 2: Core Refactoring** (Priority: High)
1. **Create ClientManager class** (`core/client_manager.py`):
   - IP tracking and client registry
   - Connection/disconnection event handling
   - Integration with server status parsing

2. **Create GameStateManager class** (`core/game_state_manager.py`):
   - State machine logic (WAITING → WARMUP → RUNNING)
   - Match progression and timing
   - Event-driven state transitions

3. **Create MessageProcessor class** (`core/message_processor.py`):
   - Server output parsing with regex patterns
   - Game event detection and dispatching
   - Client status extraction

### **Phase 3: Advanced Features** (Priority: Medium)
1. **Enhanced LatencyManager** (`core/latency_manager.py`):
   - Per-client latency configuration
   - Match-based latency rotation
   - Configuration templates for experiments

2. **ExperimentController** (`core/experiment_controller.py`):
   - Multi-match sequence management
   - Automated experiment progression
   - Data collection coordination

### **Phase 4: OBS Integration** (Priority: Low - Future)
1. **OBSController class** (`core/obs_controller.py`)
2. **WebSocket communication layer**
3. **Recording synchronization**

## Key Refactoring Patterns

### From Procedural to OOP
- **Original**: Single 437-line script with global variables and functions
- **Target**: Modular classes with clear responsibilities and dependency injection
- **Benefits**: Better testability, maintainability, and extensibility

### State Management
- **Original**: Global `STATE` variable with enum
- **Target**: Encapsulated state machine in `GameStateManager` class
- **Events**: Client connections, map changes, timeouts trigger state transitions

### Message Processing
- **Original**: Inline regex matching in main loop
- **Target**: Dedicated `MessageProcessor` with event handlers
- **Pattern**: Observer pattern for game event notifications
