# Release v1.2.1 - TUI Bug Fixes & Enhancements

**Release Date:** October 1, 2025

## 🐛 Bug Fixes

### Fixed Duplicate Round Count Increment
- **Issue**: `handle_match_shutdown_detected` was incrementing `round_count` after `handle_match_end_detected` already did, causing double increment
- **Fix**: Simplified `handle_match_shutdown_detected` to only acknowledge shutdown without counting
- **Impact**: Round counter now displays correctly throughout match progression
- **File**: `core/game/state_manager.py`

### Fixed Sudo Password Prompt on Exit
- **Issue**: Exiting TUI prompted for sudo password even when network rules weren't applied
- **Fix**: Added conditional check for `enable_latency_control` setting before calling `NetworkUtils.dispose()`
- **Impact**: Clean exit without unnecessary password prompts
- **File**: `tui_main.py`

### Fixed User Table Layout
- **Issue**: User table was too small and positioned incorrectly, couldn't display all columns
- **Fix**:
  - Changed CSS units from `100vh/100vw` to `100%` (Textual-compatible)
  - Set button container height to fixed `3` lines instead of `auto`
  - Added proper `#left-panel` and `#server-control-buttons` containers
  - Table now uses `height: 1fr` to expand and fill available space
- **Impact**: User table properly displays all columns (ID, Name, OBS, Action) with full visibility
- **Files**: `tui_main.py`, `tui_main.tcss`

## ✨ Enhancements

### Textual Worker Implementation
- **Change**: Refactored server thread management to use Textual's `@work(thread=True)` decorator
- **Benefits**:
  - Better lifecycle management
  - Cleaner code without manual thread handling
  - Non-blocking server startup from UI
  - Automatic cleanup by Textual framework
- **File**: `tui_main.py`

### Server Start/Stop Controls
- **Added**: "Start Server" and "Kill Server" buttons
- **Features**:
  - Start Server button disabled when server is running
  - Thread-safe `server.is_running()` method for status checks
  - Non-blocking server startup using Worker
- **Files**: `tui_main.py`, `core/server/server.py`

### File Logging
- **Added**: Rotating file handler for TUI logs
- **Configuration**:
  - Log file: `tui_app.log`
  - Max size: 5MB per file
  - Keeps 3 backup files
  - Format includes timestamp, logger name, level, and message
- **File**: `tui_main.py`

## 🔧 Technical Changes

### State Manager (`core/game/state_manager.py`)
- Simplified `handle_match_shutdown_detected()` - removed duplicate round counting logic
- Removed redundant experiment finished checks
- Removed duplicate latency rotation actions

### Server (`core/server/server.py`)
- Added `is_running()` method for thread-safe process status check
- Renamed `MatchEndStrategy` to `MatchShutdownStrategy`
- Renamed `WarmupEndStrategy` to `WarmupShutdownStrategy`

### TUI (`tui_main.py`)
- Removed manual thread management (`server_thread`, `run_server_thread`, `start_server_process`)
- Added `@work(thread=True)` decorator for `run_server_worker()`
- Updated cleanup to conditionally dispose network rules
- Added rotating file handler in `main()`

### TUI CSS (`tui_main.tcss`)
- Fixed container height/width units (`100%` instead of `100vh/100vw`)
- Added `#left-panel` styles (40% width, 100% height)
- Added `#server-control-buttons` styles (height: 3, margin-bottom: 1)
- Updated `#user-table` to use `height: 1fr` for expansion
- Updated `#right-panel` to 60% width (complement to left-panel)

## 📝 Files Changed
- `core/game/state_manager.py` - Bug fix + cleanup
- `core/server/server.py` - Added `is_running()` method
- `core/server/shutdown_strategies.py` - Renamed strategies
- `tui_main.py` - Major refactoring + bug fixes
- `tui_main.tcss` - Layout fixes

## 🎯 Testing Notes
- Verified round counting is correct across match progression
- Verified clean exit without sudo prompts when latency control not enabled
- Verified user table displays all columns with proper sizing
- Verified server start/stop buttons work correctly
- Verified Worker-based server startup is non-blocking

---

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>