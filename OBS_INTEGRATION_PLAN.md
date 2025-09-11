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

### Data Flow (Updated with Immediate Connection)

1. **Client Connection** → Server detects human player → **Immediate OBS connection attempt**
2. **OBS Connection Result** → Display status table → Update client manager
3. **Threshold Reached** → GameStateManager transitions to WARMUP
4. **Warmup Phase** → Check already connected → Connect remaining clients only
5. **Connection Results** → Kick failed clients OR proceed to recording
6. **Match Start** → Start all recordings → Begin match
7. **Match End** → Stop all recordings → Rotate to next match

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

## 3. Immediate OBS Connection Feature

### 3.1 Feature Overview

**Key Enhancement:** OBS connections are now established immediately when each client connects to the server, rather than waiting for the warmup phase.

### 3.2 Implementation Details

**New Connection Flow:**
```python
def _process_discovered_clients(self, client_ips):
    newly_added_humans = []
    
    for ip in client_ips:
        if ip not in self.client_manager.ip_latency_map:
            # Add new human client
            self.client_manager.add_client(client_id, ip, latency)
            newly_added_humans.append(ip)
    
    # Immediately attempt OBS connections for new clients
    if newly_added_humans and self._async_loop:
        for ip in newly_added_humans:
            self._async_loop.create_task(
                self._connect_single_client_obs_async(ip)
            )
```

**Per-Client Connection Method:**
```python
async def _connect_single_client_obs_async(self, client_ip: str):
    # Attempt connection to this specific client
    connected = await self.obs_manager.connect_client_obs(client_ip)
    
    # Update client manager with OBS status
    self.client_manager.set_obs_status(client_ip, connected)
    
    # Display immediate feedback
    if connected:
        print(f"\n[OBS CONNECTION SUCCESS] {client_ip}")
        self.display_utils.display_client_table(self.client_manager)
    else:
        print(f"\n[OBS CONNECTION FAILED] {client_ip}")
```

### 3.3 Benefits

✅ **Immediate Feedback** - Users know instantly if OBS connection works  
✅ **No Waiting** - OBS connects as soon as user joins  
✅ **Efficient Warmup** - Skips already connected clients  
✅ **Better UX** - Real-time status updates and notifications  
✅ **Early Detection** - Problems identified before warmup phase

### 3.4 Modified Warmup Behavior

The warmup phase now:
1. **Checks existing connections** - Identifies already connected vs. failed clients
2. **Only connects remaining** - Attempts connection for clients not yet connected
3. **Shows comprehensive status** - Displays table of all client states
4. **Handles mixed scenarios** - Some connected, some failed, some new

---

## 4. Workflow Implementation

### 4.1 Updated Warmup Phase Workflow

```python
# Updated pseudo-code for warmup phase (with immediate connections)
async def handle_warmup_phase():
    # 1. Check player threshold (3 humans)
    if human_count >= 3:
        # 2. Get human client IPs
        human_ips = client_manager.get_human_clients()
        
        # 3. Check which clients are already connected (NEW BEHAVIOR)
        already_connected = []
        need_connection = []
        
        for ip in human_ips:
            if obs_manager.is_client_connected(ip):
                already_connected.append(ip)
            else:
                need_connection.append(ip)
        
        print(f"OBS Status - Already connected: {len(already_connected)}")
        print(f"Need connection: {len(need_connection)}")
        
        # 4. Only attempt connections for remaining clients (OPTIMIZED)
        connection_results = {}
        if need_connection:
            print(f"Connecting to {len(need_connection)} remaining OBS instances...")
            connection_results = await obs_manager.connect_all_clients(
                need_connection, timeout=30
            )
        
        # Add already connected clients to results
        for ip in already_connected:
            connection_results[ip] = True
        
        # 5. Display comprehensive client table
        display_client_table(client_manager.get_client_info_table())
        
        # 6. Handle failed connections
        failed_clients = [ip for ip, connected in connection_results.items() if not connected]
        for ip in failed_clients:
            client_id = client_manager.get_client_id_by_ip(ip)
            server.send_command(f"kick {client_id}")
            logger.info(f"Kicked client {ip}: OBS connection failed")
        
        # 7. Start recordings for all connected clients
        successful_connections = [ip for ip, connected in connection_results.items() if connected]
        if successful_connections:
            recording_results = await obs_manager.start_all_recordings()
            display_recording_status(recording_results)
            
        # 8. Proceed to match
        game_state_manager.transition_to_running()
```

### 4.2 Match Recording Workflow

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

## 5. Display Formatting

### 5.1 Immediate Connection Feedback (NEW)

**When a client connects and OBS connection succeeds:**
```
[OBS CONNECTION SUCCESS] 192.168.1.100

===============================================================================
                             UPDATED CLIENT STATUS
===============================================================================
┌────────────┬───────────────┬────────┬─────────┬─────────────┬──────────┐
│ Client ID  │ IP Address    │ Type   │ Latency │ OBS Status  │ Name     │
├────────────┼───────────────┼────────┼─────────┼─────────────┼──────────┤
│ 101        │ 192.168.1.100 │ HUMAN  │ 200ms   │ Connected   │ Player1  │
└────────────┴───────────────┴────────┴─────────┴─────────────┴──────────┘
```

**When a client connects and OBS connection fails:**
```
[OBS CONNECTION FAILED] 192.168.1.101

===============================================================================
                      CLIENT STATUS - OBS CONNECTION FAILED
===============================================================================
┌────────────┬───────────────┬────────┬─────────┬─────────────┬──────────┐
│ Client ID  │ IP Address    │ Type   │ Latency │ OBS Status  │ Name     │
├────────────┼───────────────┼────────┼─────────┼─────────────┼──────────┤
│ 101        │ 192.168.1.100 │ HUMAN  │ 200ms   │ Connected   │ Player1  │
│ 102        │ 192.168.1.101 │ HUMAN  │ 300ms   │ Not Connected│ Player2 │
└────────────┴───────────────┴────────┴─────────┴─────────────┴──────────┘
```

### 5.2 Client Information Table (Warmup)

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

### 5.3 OBS Connection Results

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

## 6. Configuration Management

### 6.1 Environment Variables (.env)

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

### 6.2 Dependencies Update (pyproject.toml)

```toml
dependencies = [
    "dotenv>=0.9.9",
    "websockets>=12.0",
    "tabulate>=0.9.0",  # New
    "asyncio",          # Built-in
]
```

---

## 7. Error Handling Strategy

### 7.1 Connection Failures

**Timeout Handling:**
- 30-second timeout per client
- Log timeout as WARNING
- Kick client after timeout
- Continue with remaining clients

**Authentication Failures:**
- Log detailed error message
- Attempt retry (configurable)
- Mark client as failed after retries

### 7.2 Recording Failures

**Start Recording Failure:**
- Log error with client IP
- Continue match without that client's recording
- Send notification to server console

**Stop Recording Failure:**
- Log error but don't block match progression
- Attempt graceful cleanup

### 7.3 Async Operation Management

**Task Cancellation:**
- Proper cleanup on SIGINT
- Cancel all pending OBS operations
- Disconnect all WebSocket connections

**Exception Propagation:**
- Catch and log exceptions in async tasks
- Prevent single failure from crashing server

---

## 8. Logging Strategy

### 8.1 Log Levels

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

### 8.2 Log Output Format

```
2025-01-14 10:30:45 [INFO] Starting warmup phase with 3 humans, 2 bots
2025-01-14 10:30:46 [INFO] Connecting to OBS for 192.168.1.100...
2025-01-14 10:30:47 [INFO] OBS connected: 192.168.1.100
2025-01-14 10:30:48 [INFO] Starting recording for all clients
2025-01-14 10:32:00 [INFO] Match 1/6 started
2025-01-14 10:34:00 [INFO] Match 1/6 completed, stopping recordings
```

---

## 9. Testing Strategy

### 9.1 Unit Tests

- OBSManager connection/disconnection
- ClientManager type differentiation
- GameStateManager OBS phase transitions
- Async operation timeouts

### 9.2 Integration Tests

- Full warmup phase with OBS connections
- Recording start/stop during matches
- Client kick on connection failure
- Graceful degradation scenarios
- Immediate connection testing
- Mixed connection state scenarios

### 9.3 Manual Testing Checklist

- [ ] Connect with 3 human clients
- [ ] Verify immediate OBS connection attempts per client
- [ ] Check client table displays after each connection
- [ ] Verify warmup skips already connected clients
- [ ] Test recording start/stop
- [ ] Test client kick on OBS failure
- [ ] Verify match progression
- [ ] Test client disconnection cleanup
- [ ] Test server shutdown cleanup

---

## 10. Implementation Timeline

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
