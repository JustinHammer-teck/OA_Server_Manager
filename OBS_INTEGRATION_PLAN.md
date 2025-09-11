# OBS WebSocket Integration Plan for OpenArena Server

## Document Information
- **Type:** Technical Implementation Plan
- **Date:** 2025-01-14
- **Version:** 1.0
- **Status:** Planning Phase

---

## Executive Summary

This document outlines the integration plan for adding OBS (Open Broadcaster Software) WebSocket control to the OpenArena server management system. The integration will enable synchronized recording management across multiple client OBS instances, with automatic recording control during experimental matches.

### Key Objectives
- Asynchronous OBS WebSocket management for non-blocking operations
- Automatic recording synchronization for human clients
- Client differentiation (Human vs Bot)
- Graceful handling of connection failures
- Per-match recording lifecycle management

---

## 1. Architecture Overview

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    OpenArena Server (oa_ded)                │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   Server Class    │
                    │  (Orchestrator)    │
                    └─────────┬─────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼────────┐  ┌────────▼────────┐  ┌────────▼────────┐
│ ClientManager  │  │ GameStateManager │  │   OBSManager    │
│                │  │                  │  │     (NEW)       │
│ • Track Humans │  │ • WAITING        │  │ • Async Ops     │
│ • Track Bots   │  │ • WARMUP + OBS   │  │ • Multi-Client  │
│ • OBS Status   │  │ • RUNNING        │  │ • Recording     │
└────────────────┘  └──────────────────┘  └─────────────────┘
                                                    │
                                          ┌─────────▼─────────┐
                                          │  OBS WebSocket    │
                                          │   Connections     │
                                          │  (Per Client)     │
                                          └───────────────────┘
```

### Data Flow

1. **Client Connection** → Server detects human player → ClientManager tracks
2. **Threshold Reached** → GameStateManager transitions to WARMUP
3. **Warmup Phase** → OBSManager attempts connections → Display status
4. **Connection Results** → Kick failed clients OR proceed to recording
5. **Match Start** → Start all recordings → Begin match
6. **Match End** → Stop all recordings → Rotate to next match

### References Docs

@OA_CMDS_CONFIGS.md
@OBS_WEBSOCKET.md

---

## 2. Implementation Components

### 2.1 OBSManager Class (`core/obs_manager.py`)

**Purpose:** Centralized management of multiple OBS WebSocket connections

**Key Features:**
- Asynchronous connection management
- Batch recording operations
- Connection timeout handling
- Status monitoring

**Core Methods:**
```python
class OBSManager:
    async def connect_client_obs(self, client_ip: str, obs_port: int = 4455, 
                                  password: Optional[str] = None) -> bool
    async def connect_all_clients(self, client_ips: List[str], 
                                   timeout: int = 30) -> Dict[str, bool]
    async def start_all_recordings(self) -> Dict[str, bool]
    async def stop_all_recordings(self) -> Dict[str, bool]
    async def get_all_recording_status(self) -> Dict[str, Dict]
    async def disconnect_client(self, client_ip: str) -> None
    async def disconnect_all(self) -> None
```

**Connection Strategy:**
- Parallel connection attempts using `asyncio.gather()`
- Individual timeout per client (default 30 seconds)
- Retry logic for transient failures
- Clean disconnection on failure

---

### 2.2 Enhanced ClientManager (`core/client_manager.py`)

**NOTE:**
- Bot has these name in it
```
bot_names = [
    "Angelyss",
    "Arachna",
    "Major",
    "Sarge",
    "Skelebot",
    "Merman",
    "Beret",
    "Kyonshi",
]
```

**New Features:**
- Client type differentiation (Human vs Bot)
- OBS connection status tracking
- Tabulate-ready data formatting

**New/Modified Methods:**
```python
class ClientManager:
    def add_client(self, client_id: int, ip: str, latency: Optional[int] = None, 
                   is_bot: bool = False) -> None
    def get_human_clients(self) -> List[str]
    def get_bot_clients(self) -> List[str]
    def set_obs_status(self, ip: str, connected: bool) -> None
    def get_obs_status(self, ip: str) -> Optional[bool]
    def get_client_info_table(self) -> List[List[Any]]
    def is_bot(self, client_id: int) -> bool
```

**Data Structure Enhancement:**
```python
# Current
self.client_ip_map: Dict[int, str] = {}
self.ip_latency_map: Dict[str, int] = {}

# New additions
self.client_type_map: Dict[int, str] = {}  # "HUMAN" or "BOT"
self.obs_status_map: Dict[str, bool] = {}  # IP -> OBS connected
```

---

### 2.3 Modified GameStateManager (`core/game_state_manager.py`)

**Enhanced State Machine:**

```
WAITING (current: wait for players)
   ↓ (3 human players detected)
WARMUP (enhanced: add bots + OBS connection)
   ├─ Add 2 easy bots
   ├─ Connect to OBS instances (async)
   ├─ Display connection status
   ├─ Kick failed connections
   └─ Start recordings
   ↓ (OBS ready + 1 minute elapsed)
RUNNING (enhanced: per-match recording)
   ├─ Start recording (match begin)
   ├─ Run match
   └─ Stop recording (match end)
```

**New Methods:**
```python
class GameStateManager:
    def should_add_warmup_bots(self) -> bool
    def set_obs_connection_status(self, all_connected: bool) -> None
    def is_ready_for_match(self) -> bool
    async def handle_warmup_obs_phase(self, obs_manager, human_ips) -> bool
```

---

## 3. Workflow Implementation

### 3.1 Warmup Phase Workflow

```python
# Pseudo-code for warmup phase
async def handle_warmup_phase():
    # 1. Check player threshold (3 humans)
    if human_count >= 3:
        # 2. Add 2 easy bots
        server.add_bots(num_bots=2, difficulty=1, names=["Bot1", "Bot2"])
        
        # 3. Get human client IPs
        human_ips = client_manager.get_human_clients()
        
        # 4. Attempt OBS connections (async)
        print("Connecting to OBS instances...")
        connection_results = await obs_manager.connect_all_clients(
            human_ips, timeout=30
        )
        
        # 5. Update client manager with OBS status
        for ip, connected in connection_results.items():
            client_manager.set_obs_status(ip, connected)
        
        # 6. Display client table
        display_client_table(client_manager.get_client_info_table())
        
        # 7. Handle failed connections
        for ip, connected in connection_results.items():
            if not connected:
                client_id = client_manager.get_client_id_by_ip(ip)
                server.send_command(f"kick {client_id}")
                logger.debug(f"Kicked client {ip}: OBS connection failed")
        
        # 8. Start recordings for connected clients
        if any(connection_results.values()):
            recording_results = await obs_manager.start_all_recordings()
            display_recording_status(recording_results)
            
        # 9. Proceed to match
        game_state_manager.transition_to_running()
```

### 3.2 Match Recording Workflow

```python
# Per-match recording control
async def handle_match_lifecycle():
    # Match start
    logger.info(f"Starting match {current_round}/{max_rounds}")
    await obs_manager.start_all_recordings()
    
    # Match running...
    
    # Match end
    logger.info(f"Match {current_round} completed")
    await obs_manager.stop_all_recordings()
    
    # Rotate latencies for next match
    if current_round < max_rounds:
        rotate_latencies()
```

---

## 4. Display Formatting

### 4.1 Client Information Table (Warmup)

```
╔════════════╦═══════════════╦════════╦═════════╦═══════════╗
║ Client ID  ║ IP Address    ║ Type   ║ Latency ║ OBS Status║
╠════════════╬═══════════════╬════════╬═════════╬═══════════╣
║ 101        ║ 192.168.1.100 ║ HUMAN  ║ 200ms   ║ Connected ║
║ 102        ║ 192.168.1.101 ║ HUMAN  ║ 300ms   ║ Connected ║
║ 103        ║ 192.168.1.102 ║ HUMAN  ║ 150ms   ║ Failed    ║
║ 501        ║ N/A           ║ BOT    ║ N/A     ║ N/A       ║
║ 502        ║ N/A           ║ BOT    ║ N/A     ║ N/A       ║
╚════════════╩═══════════════╩════════╩═════════╩═══════════╝
```

### 4.2 OBS Connection Results

```
╔═══════════════╦════════════════╦══════════════════════╗
║ Client IP     ║ OBS Connection ║ Recording Status     ║
╠═══════════════╬════════════════╬══════════════════════╣
║ 192.168.1.100 ║ ✓ Connected    ║ Recording Started    ║
║ 192.168.1.101 ║ ✓ Connected    ║ Recording Started    ║
║ 192.168.1.102 ║ ✗ Failed       ║ Client Kicked        ║
╚═══════════════╩════════════════╩══════════════════════╝
```

---

## 5. Configuration Management

### 5.1 Environment Variables (.env)

```bash
# Existing configurations
NPLAYERS_THRESHOLD=3
WARMUP_TIMELIMIT=1
BOT_ENABLE=true
BOT_COUNT=2

# New OBS configurations
OBS_PORT=4455
OBS_PASSWORD=yourpassword
OBS_CONNECTION_TIMEOUT=30
OBS_RETRY_ATTEMPTS=2
BOT_DIFFICULTY_WARMUP=1

# Display settings
DISPLAY_CLIENT_TABLE=true
DISPLAY_OBS_STATUS=true
```

### 5.2 Dependencies Update (pyproject.toml)

```toml
dependencies = [
    "dotenv>=0.9.9",
    "websockets>=12.0",
    "tabulate>=0.9.0",  # New
    "asyncio",          # Built-in
]
```

---

## 6. Error Handling Strategy

### 6.1 Connection Failures

**Timeout Handling:**
- 30-second timeout per client
- Log timeout as WARNING
- Kick client after timeout
- Continue with remaining clients

**Authentication Failures:**
- Log detailed error message
- Attempt retry (configurable)
- Mark client as failed after retries

### 6.2 Recording Failures

**Start Recording Failure:**
- Log error with client IP
- Continue match without that client's recording
- Send notification to server console

**Stop Recording Failure:**
- Log error but don't block match progression
- Attempt graceful cleanup

### 6.3 Async Operation Management

**Task Cancellation:**
- Proper cleanup on SIGINT
- Cancel all pending OBS operations
- Disconnect all WebSocket connections

**Exception Propagation:**
- Catch and log exceptions in async tasks
- Prevent single failure from crashing server

---

## 7. Logging Strategy

### 7.1 Log Levels

```python
# INFO level
logger.info("Starting OBS connection phase")
logger.info(f"Connected to OBS for client {ip}")
logger.info(f"Recording started for {count} clients")

# WARNING level
logger.warning(f"OBS connection timeout for {ip}")
logger.warning(f"Failed to stop recording for {ip}")

# DEBUG level  
logger.debug(f"OBS WebSocket message: {message}")
logger.debug(f"Kicking client {id}: OBS connection failed")

# ERROR level
logger.error(f"Critical OBS manager failure: {error}")
```

### 7.2 Log Output Format

```
2025-01-14 10:30:45 [INFO] Starting warmup phase with 3 humans, 2 bots
2025-01-14 10:30:46 [INFO] Connecting to OBS for 192.168.1.100...
2025-01-14 10:30:47 [INFO] OBS connected: 192.168.1.100
2025-01-14 10:30:48 [INFO] Starting recording for all clients
2025-01-14 10:32:00 [INFO] Match 1/6 started
2025-01-14 10:34:00 [INFO] Match 1/6 completed, stopping recordings
```

---

## 8. Testing Strategy

### 8.1 Unit Tests

- OBSManager connection/disconnection
- ClientManager type differentiation
- GameStateManager OBS phase transitions
- Async operation timeouts

### 8.2 Integration Tests

- Full warmup phase with OBS connections
- Recording start/stop during matches
- Client kick on connection failure
- Graceful degradation scenarios

### 8.3 Manual Testing Checklist

- [ ] Connect with 3 human clients
- [ ] Verify bot addition (2 easy bots)
- [ ] Check OBS connection attempts
- [ ] Verify client table display
- [ ] Test recording start/stop
- [ ] Test client kick on OBS failure
- [ ] Verify match progression
- [ ] Test server shutdown cleanup

---

## 9. Implementation Timeline

### Phase 1: Core Components (Day 1)
- Create OBSManager class
- Enhance ClientManager
- Add tabulate dependency

### Phase 2: Integration (Day 2)
- Modify GameStateManager
- Update Server class
- Add async support to main.py

### Phase 3: Testing & Refinement (Day 3)
- End-to-end testing
- Error handling improvements
- Performance optimization

### Phase 4: Documentation (Day 4)
- Update README
- Add usage examples
- Create troubleshooting guide

---

## 10. Future Enhancements

### Potential Improvements

1. **Dynamic OBS Discovery:**
   - Auto-detect OBS instances on network
   - mDNS/Bonjour service discovery

2. **Recording Management:**
   - Configurable recording profiles
   - Automatic file naming with metadata
   - Post-match file organization

3. **Advanced Monitoring:**
   - Real-time recording statistics
   - Network bandwidth monitoring
   - OBS performance metrics

4. **Fault Tolerance:**
   - Automatic reconnection attempts
   - Recording resume on connection restore
   - Backup recording triggers

5. **Web Dashboard:**
   - Real-time client status display
   - Manual recording controls
   - Historical session data

---

## Appendix A: Code Examples

### A.1 OBSManager Connection Example

```python
async def connect_to_client_obs(self, client_ip: str) -> bool:
    """Connect to a single client's OBS instance."""
    try:
        obs_client = OBSWebSocketClient(
            host=client_ip,
            port=self.obs_port,
            password=self.obs_password
        )
        
        # Attempt connection with timeout
        connected = await asyncio.wait_for(
            obs_client.connect(),
            timeout=self.connection_timeout
        )
        
        if connected:
            self.obs_clients[client_ip] = obs_client
            self.logger.info(f"OBS connected: {client_ip}")
            return True
            
    except asyncio.TimeoutError:
        self.logger.warning(f"OBS connection timeout: {client_ip}")
    except Exception as e:
        self.logger.error(f"OBS connection error for {client_ip}: {e}")
    
    return False
```

### A.2 Tabulate Display Example

```python
from tabulate import tabulate

def display_client_table(client_manager):
    """Display formatted client information table."""
    headers = ["Client ID", "IP Address", "Type", "Latency", "OBS Status"]
    table_data = client_manager.get_client_info_table()
    
    print("\n" + "="*60)
    print("CLIENT INFORMATION")
    print("="*60)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print("="*60 + "\n")
```

---

## Appendix B: Configuration File Examples

### B.1 Sample .env Configuration

```bash
# OpenArena Server Settings
NPLAYERS_THRESHOLD=3
TIMELIMIT=2
WARMUP_TIMELIMIT=1
REPEATS=2

# Bot Configuration
BOT_ENABLE=true
BOT_COUNT=2
BOT_DIFFICULTY=3
BOT_DIFFICULTY_WARMUP=1
BOT_NAMES=Sarge,Grunt

# Network Latency Settings
LATENCIES=100,200,300
INTERFACE=enp1s0

# OBS WebSocket Settings
OBS_PORT=4455
OBS_PASSWORD=SecurePassword123
OBS_CONNECTION_TIMEOUT=30
OBS_RETRY_ATTEMPTS=2

# Display Settings
DISPLAY_CLIENT_TABLE=true
DISPLAY_OBS_STATUS=true
LOG_LEVEL=INFO
```

---

## Document Revision History

| Version | Date       | Author | Changes                    |
|---------|------------|--------|----------------------------|
| 1.0     | 2025-01-14 | System | Initial plan creation      |

---

**END OF DOCUMENT**
