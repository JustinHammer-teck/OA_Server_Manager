# Release v1.2.0 - TUI Player Management

**Release Date:** September 30, 2025

## ✨ New Features

### TUI Enhancements
- **Connected Users Table**: Real-time display with Client ID, Name, OBS Status, and Actions
- **Game Status Panel**: Live game state and round counter display
- **Bot Controls**: Add Bot and Remove All Bots buttons

### Player Kick System
- **Slot-based kicking**: New `kick_client(client_id)` method using OpenArena's `clientkick` command
- **TUI Integration**: Click any row in the Connected Users table to kick player/bot
- **Reliable**: Works correctly with duplicate bot names

## 🔧 Technical Changes

### Server (`core/server/server.py`)
- Added `kick_client(client_id: int)` method with validation and logging

### NetworkManager (`core/network/network_manager.py`)
- Added `get_client_id_by_ip(ip: str)` helper method

### TUI (`tui_main.py`)
- Added "ID" column to user table showing slot numbers
- Updated row click handler to use `server.kick_client(client_id)`
- Auto-refresh every 2 seconds for status and user table

## 📝 Files Changed
- `core/server/server.py`
- `core/network/network_manager.py`
- `tui_main.py`

## 🚀 Usage
- **Kick player**: Click any row in the Connected Users table
- **Add bot**: Click "Add Bot" button
- **Remove bots**: Click "Remove All Bots" button

---

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>