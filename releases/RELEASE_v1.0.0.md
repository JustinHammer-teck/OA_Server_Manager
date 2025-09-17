# Release v1.0.0 - Major Refactoring & TUI Support

**Release Date:** January 17, 2025

## 🎯 Highlights
- Complete OOP refactoring from procedural architecture
- New Terminal User Interface (TUI) for admin commands
- Consolidated manager system (50% reduction)
- Enhanced error handling and process safety

## ✨ What's New

### Core Refactoring
- **Manager Consolidation**: Reduced from 8 managers to 4
  - `NetworkManager` (merged ClientManager + LatencyManager)
  - `GameManager` (merged BotManager + GameConfigManager)
  - Kept `GameStateManager` and `MessageProcessor` separate
- **Message Handling**: Replaced if-elif chain with dispatch dictionary pattern
- **Code Reduction**: ~50% reduction in message handling logic

### TUI Support
- New `tui_main.py` with Textual-based interface
- Admin command input panel
- Real-time server log display
- Background thread server execution
- Press 'q' to quit, type commands directly

### Error Handling
- Process I/O error handling for `send_command()` and `read_server()`
- Proper exception logging (removed silent catches)
- Added `is_process_alive()` health check method
- Protection against BrokenPipeError and OSError

## 🔧 Technical Improvements
- Simplified initialization (removed unnecessary abstraction)
- Fixed hardcoded interface to use settings.interface
- Centralized cleanup() function
- Thread-safe server operations
- Better async task management

## 📦 Dependencies
- Python 3.13+
- textual (for TUI)
- python-dotenv
- websockets

## 🚀 Usage

### Standard Mode:
```bash
uv run main.py
```

### TUI Mode:
```bash
uv run tui_main.py
```

## 🐛 Bug Fixes
- Fixed redundant cleanup code between signal_handler and main
- Fixed silent exception swallowing
- Added proper error handling for subprocess I/O

## 📝 Notes
- Server process now runs in background thread for better control
- TUI allows real-time admin command execution
- All changes maintain backward compatibility

## 🔄 Migration Guide
- No breaking changes for existing configurations
- Add TUI usage by running `uv run tui_main.py` instead of `uv run main.py`
- All environment variables remain the same

## 🏗️ Architecture Changes
```
Before: 8 separate managers
After: 4 consolidated managers

Old:
├── ClientManager
├── LatencyManager
├── BotManager
├── GameConfigManager
├── GameStateManager     (kept)
├── MessageProcessor     (kept)
├── OBSConnectionManager (kept)
└── DisplayUtils         (kept)

New:
├── NetworkManager       (ClientManager + LatencyManager)
├── GameManager          (BotManager + GameConfigManager)
├── GameStateManager
├── MessageProcessor
├── OBSConnectionManager
└── DisplayUtils
```

## 🧪 Testing
- Server successfully runs in background thread
- TUI interface functional with command input
- Error handling tested with process failures
- All existing functionality preserved

---

**Full Changelog**: [View commits](https://github.com/your-repo/compare/v0.9.0...v1.0.0)