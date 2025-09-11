# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

## Refactoring Goals

### Current State ✅ **REFACTORING COMPLETE**
- **`server_script.py`**: **REFERENCE ONLY** - Legacy monolithic procedural script (438 lines) - DO NOT MODIFY, use as source for refactoring
- **`core/`**: **FULLY REFACTORED** modular architecture with specialized managers (1200+ lines total)
- **`main.py`**: Enhanced OOP entry point with proper logging and cleanup
- **`tests/`**: Test scripts for OBS WebSocket validation and functionality

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

### Future Dependencies (OBS Integration)
- WebSocket libraries for OBS communication (`obs-websocket-py`)
- Async frameworks for concurrent client management (`asyncio`)
- JSON configuration files for experiment templates

## Key Implementation Details

### Current Server Management
- **Process Control**: Server class manages `oa_ded` lifecycle with stdin command sending
- **Output Monitoring**: Real-time parsing of server stderr for game state detection
- **Network Latency**: `NetworkUtils.apply_latency_rules()` uses tc/HTB queuing with nftables
- **OBS Integration**: Immediate WebSocket connection to client OBS instances upon joining

### Implemented Client Management
- **IP Tracking**: Parse server status output to maintain client IP registry
- **OBS Mapping**: Associate each client IP with corresponding OBS WebSocket endpoint
- **Immediate Connection**: Connect to OBS as soon as client joins (no waiting)
- **State Synchronization**: Coordinate match state changes with recording control
- **Real-time Feedback**: Display connection status with formatted tables

### Experiment Sequencing
- **Match Progression**: Automatic transition through experimental match sequence
- **Latency Rotation**: Apply different network conditions for each match
- **Data Collection**: Synchronized start/stop of server logging and client recording

### WebSocket Architecture
- **Async Communication**: Non-blocking WebSocket connections to multiple OBS instances
- **Command Queue**: Buffered command system for reliable recording control
- **Error Handling**: Robust connection management with reconnection strategies

## Current Refactoring Progress

### ✅ **Completed Components** (400+ lines total):
1. **`core/server.py`**: **FULLY INTEGRATED** Server class (270 lines) with:
   - Server process management (`start_server`, `dispose`)
   - Command sending (`send_command`)
   - Bot management (`add_bots`)
   - **Complete message processing loop** (`run_server_loop`)
   - **Event handlers** for all game events
   - **Integrated client, state, and latency management**

2. **`core/client_manager.py`**: **NEW** ClientManager class (70 lines) with:
   - Client connection tracking with IP addresses
   - Latency assignment and rotation
   - Connection/disconnection handling

3. **`core/game_state_manager.py`**: **NEW** GameStateManager class (110 lines) with:
   - State machine (WAITING → WARMUP → RUNNING)
   - Match progression and experiment sequencing  
   - Server command integration

4. **`core/message_processor.py`**: **NEW** MessageProcessor class (140 lines) with:
   - Server message parsing with regex patterns
   - Event detection and structured data extraction
   - Status output parsing for client IP discovery

5. **`core/settings.py`**: Configuration management with environment variables

6. **`core/network_utils.py`**: Network latency utilities (`NetworkUtils` class)

7. **`main.py`**: **ENHANCED** integrated entry point (68 lines) with proper logging and cleanup

### ✅ **OBS WEBSOCKET INTEGRATION** - Immediate Connection Feature:

6. **`core/obs_manager.py`**: **NEW** OBSManager class (180+ lines) with:
   - Asynchronous WebSocket connection management
   - Per-client connection handling with timeout
   - Batch recording operations (start/stop all)
   - Individual client status tracking and cleanup

7. **`core/obs_controller.py`**: **NEW** OBSWebSocketClient class (200+ lines) with:
   - OBS WebSocket 5.x protocol implementation
   - Authentication handling (challenge/salt)
   - Recording control (start/stop/status)
   - Scene management and connection lifecycle

8. **`core/display_utils.py`**: **NEW** DisplayUtils class (150+ lines) with:
   - Formatted tabulate output for client information
   - Real-time OBS connection status display
   - Match start/end notifications
   - Connection result summaries

### ✅ **ENHANCED COMPONENTS** - Immediate Connection Integration:

- **`core/server.py`**: **ENHANCED** with immediate OBS connection (580+ lines):
  - `_connect_single_client_obs_async()` - Immediate per-client connection
  - `_handle_obs_connections_async()` - Skip already connected during warmup
  - `_disconnect_client_obs_async()` - Clean disconnection handling
  - Async task management and lifecycle control

- **`core/client_manager.py`**: **ENHANCED** with OBS status tracking (210+ lines):
  - Human vs Bot client differentiation
  - Per-IP OBS connection status tracking
  - Tabulate-ready data formatting
  - Bot name recognition and type detection

### ✅ **REFACTORING COMPLETE** - All Core Components Implemented:

1. **✅ Client Management System**: **COMPLETE**
   - ✅ IP address tracking and parsing from server status
   - ✅ Client connection/disconnection handling  
   - ✅ Player list management with latency assignments

2. **✅ Game State Machine Logic**: **COMPLETE**
   - ✅ State transitions (WAITING → WARMUP → RUNNING)
   - ✅ Round progression and experiment sequencing
   - ✅ Match timing and progression logic

3. **✅ Server Message Processing**: **COMPLETE**
   - ✅ Real-time parsing of server stderr output
   - ✅ Pattern matching for client connections, disconnections, map changes
   - ✅ Game event detection ("AAS initialized", "ClientDisconnect", etc.)

4. **✅ Experiment Management**: **COMPLETE**
   - ✅ Latency rotation between matches
   - ✅ Match counting and sequence control
   - ✅ Automated progression through experimental phases

5. **✅ Signal Handling & Cleanup**: **COMPLETE**
   - ✅ Proper SIGINT handling for graceful shutdown
   - ✅ Network rule cleanup on exit

6. **✅ All Server Properties/Methods**: **COMPLETE**
   - ✅ All properties properly defined and integrated
   - ✅ Complete message processing loop implemented
   - ✅ Full integration of all manager components

### 🎉 **All Phase 1 & 2 Bugs Fixed**:
- ✅ All undefined property references resolved
- ✅ All encoding issues fixed
- ✅ Complete integration achieved

## Implementation Roadmap

### **✅ Phase 1: Fix Current Issues** (Priority: High) - **COMPLETED**
1. **✅ Fix Server class bugs**:
   - ✅ Added missing `nplayers_threshold` property
   - ✅ Fixed `server_process` property reference
   - ✅ Fixed encoding issue in `send_command`

2. **✅ Complete basic Server functionality**:
   - ✅ Added server message processing loop
   - ✅ Implemented proper state management integration

### **✅ Phase 2: Core Refactoring** (Priority: High) - **COMPLETED**
1. **✅ Created ClientManager class** (`core/client_manager.py`):
   - ✅ IP tracking and client registry
   - ✅ Connection/disconnection event handling
   - ✅ Integration with server status parsing

2. **✅ Created GameStateManager class** (`core/game_state_manager.py`):
   - ✅ State machine logic (WAITING → WARMUP → RUNNING)
   - ✅ Match progression and timing
   - ✅ Event-driven state transitions

3. **✅ Created MessageProcessor class** (`core/message_processor.py`):
   - ✅ Server output parsing with regex patterns
   - ✅ Game event detection and dispatching
   - ✅ Client status extraction

### **✅ Phase 2.5: Integration** (Priority: High) - **COMPLETED**
1. **✅ Complete System Integration**:
   - ✅ Integrated all three core classes into Server
   - ✅ Added main message processing loop (`run_server_loop`)
   - ✅ Connected client management with game state transitions
   - ✅ Automated latency application and rotation
   - ✅ Enhanced main.py with proper logging and cleanup

### **✅ Phase 3: Investigation & Documentation** (Priority: High) - **COMPLETED**
1. **✅ Complete Latency System Investigation**:
   - ✅ Analyzed Linux Traffic Control (tc) and nftables integration
   - ✅ Traced IP discovery and client mapping workflow
   - ✅ Documented packet processing flow and network architecture
   - ✅ Verified system scalability and performance characteristics

2. **✅ Comprehensive Technical Documentation**:
   - ✅ Created detailed investigation report (`LATENCY_INVESTIGATION.md`)
   - ✅ Documented troubleshooting and verification procedures
   - ✅ Added performance metrics and scalability data
   - ✅ Included security considerations and research applications

## **🎯 Current Status: COMPLETE ARCHITECTURE REFACTORING**
The system has been successfully refactored from a monolithic design to a clean, modular architecture with full OBS WebSocket integration and specialized component separation.

### **✅ Complete Refactoring Features:**
- **Modular Architecture**: Separated concerns into specialized managers
- **Clean Server Core**: Focused only on process management and coordination
- **OBS Connection Management**: Dedicated component for WebSocket operations
- **Bot Management**: Isolated bot configuration and server integration
- **Game Configuration**: Centralized OpenArena settings management
- **Latency Management**: Specialized network simulation and rotation
- **Immediate OBS Connection**: OBS connects when each client joins
- **Automatic Client Kicks**: Failed OBS connections result in client removal
- **Match-based Recording**: Automatic recording start/stop with fraglimit detection

### **📊 Refactored Architecture Statistics:**
- **Original Monolithic**: 734-line server.py
- **New Modular Design**: 1200+ lines across 12 specialized components
- **Server Core Reduction**: 734 → 410 lines (44% smaller)
- **New Specialized Managers**: 4 dedicated components (800+ lines)
- **Enhanced Modularity**: Each component has single responsibility
- **Improved Testability**: Individual managers can be tested independently

## **🏗️ Refactored Architecture Components**

### **Core Specialized Managers** (NEW)

1. **`obs_connection_manager.py`** (240 lines)
   - **Purpose**: Manages all OBS WebSocket connection operations
   - **Features**: Immediate client connections, warmup batch connections, recording control
   - **Integration**: Handles client kicks on OBS failure, async task management

2. **`bot_manager.py`** (190 lines) 
   - **Purpose**: Bot configuration and server integration management
   - **Features**: Bot addition/removal, difficulty settings, state tracking
   - **Integration**: Command-line argument processing, server setting initialization

3. **`game_config_manager.py`** (180 lines)
   - **Purpose**: OpenArena game settings and configuration management  
   - **Features**: Capturelimit, warmup, timelimit, map control, startup configuration
   - **Integration**: Runtime setting changes, startup argument generation

4. **`latency_manager.py`** (210 lines)
   - **Purpose**: Network latency simulation and rotation management
   - **Features**: Latency rule application, rotation strategies, per-client assignments
   - **Integration**: Linux traffic control integration, interface validation

### **Enhanced Core Components**

1. **`server.py`** (REFACTORED - 410 lines, 44% reduction)
   - **Purpose**: Core server process management and component coordination
   - **Focus**: Process lifecycle, command sending, message processing coordination
   - **Integration**: Orchestrates all specialized managers, maintains clean separation

### **Phase 4: Future Advanced Features** (Priority: Medium)
1. **Enhanced Experiment Templates**:
   - Pre-defined latency sequences for common research scenarios
   - Multi-match experiment configuration profiles
   - Automated data collection coordination

2. **Advanced OBS Integration**:
   - Scene switching based on match state
   - Custom recording formats and settings
   - Multi-stream coordination for different perspectives

### **Phase 5: Server Manager Latency Control** (Priority: High)
1. **Server-side Latency Management Interface**:
   - Real-time latency control and monitoring
   - Dynamic latency adjustment during matches
   - Per-client latency configuration interface
   - Latency profile management (save/load configurations)

2. **Administrative Control Features**:
   - Live latency modification without restart
   - Client-specific latency targeting
   - Experiment template creation and management
   - Real-time latency verification and monitoring

### **Phase 6: OBS Integration** (Priority: Low - Future)
1. **OBSController class** (`core/obs_controller.py`)
2. **WebSocket communication layer**
3. **Recording synchronization**

## **🔧 Key Improvements and Bug Fixes**

### **Critical Bug Fixes**
1. **Player Threshold Issue**: Fixed default from 7 to 2 players for warmup transition
2. **OBS WebSocket Protocol**: Fixed subprotocol compatibility issues  
3. **Connection Timeouts**: Added proper timeout handling for OBS connections
4. **Client Kick Implementation**: Added automatic kick for failed OBS connections
5. **Match End Detection**: Added fraglimit hit detection for OBS recording control

### **Configuration Enhancements**  
1. **OpenArena Game Settings**: Added capturelimit, warmup time, and warmup enable controls
2. **Bot Management**: Fixed bot count logic (--bots vs --add-bots confusion)
3. **Environment Configuration**: Enhanced .env file with OBS and game settings
4. **Command Line Arguments**: Clarified help text and examples for bot configuration

### **Architectural Improvements**
1. **Separation of Concerns**: Extracted 4 specialized managers from monolithic server
2. **Clean Component Integration**: Each manager has single responsibility 
3. **Async Task Management**: Proper OBS connection handling in separate thread
4. **Error Handling**: Comprehensive exception handling and logging throughout
5. **Resource Cleanup**: Proper disposal of network rules and OBS connections

### **From Monolithic to Modular Architecture**
- **Original**: Single 734-line server.py handling all responsibilities
- **Current**: Clean 410-line server.py coordinating 4 specialized managers
- **Benefits**: Better testability, maintainability, and independent feature development

### **Enhanced State Management**
- **Game State Machine**: Clean transitions (WAITING → WARMUP → RUNNING)
- **Match Progression**: Automated sequencing with latency rotation
- **OBS Integration**: Recording synchronized with match start/end events

### **Improved Message Processing**
- **Event-Driven Architecture**: Dedicated handlers for each message type
- **Pattern Matching**: Robust regex patterns for server output parsing
- **Real-time Feedback**: Immediate client status updates and OBS connection results
