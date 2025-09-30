# Release v1.1.0 - Timelimit Match End Support

**Release Date:** January 17, 2025

## ✨ New Features

### Match End Detection Enhancement
- **Timelimit support**: Added detection and handling for "Exit: Timelimit hit." messages
- **Unified match end processing**: Both fraglimit and timelimit now trigger the same OBS recording stop and match end actions
- **Enhanced logging**: Match end logs now display the specific reason (fraglimit vs timelimit)

### Client Discovery Improvements
- **Individual client processing**: Refactored client discovery to process each player individually instead of batch processing
- **Bot detection fix**: Improved bot detection using address field ("bot") instead of name matching
- **Duplicate prevention**: Added checks to prevent duplicate client registrations

## 🔧 Technical Improvements

### Message Processing
- Added `MATCH_END_TIMELIMIT` message type to MessageType enum
- New pattern matching for "Exit: Timelimit hit." messages
- Unified `_handle_timelimit_hit()` method with same behavior as fraglimit
- Both fraglimit and timelimit properly set flags for shutdown game handling

### Server Processing
- Updated `_on_match_end()` to handle both fraglimit and timelimit reasons
- Simplified `_process_discovered_client()` to handle individual clients
- Enhanced client discovery with proper IP validation and bot detection

## 🎯 Behavior Changes

### Match End Flow
- **Before**: Only fraglimit hits triggered OBS recording stops and match end actions
- **After**: Both fraglimit AND timelimit hits trigger the same complete match end sequence:
  - Stop OBS recordings immediately
  - Display reason-specific messages to players
  - Execute state management actions (latency rotation, match restart)
  - Proper experiment completion tracking

### Client Discovery Flow
- **Before**: Batch processing of discovered clients from status output
- **After**: Individual processing with immediate OBS connection for human players

## 📝 Files Changed
- `core/messaging/message_processor.py` - Added timelimit pattern and handler
- `core/server/server.py` - Updated match end handler and client discovery processing

## 🎮 Impact on Gameplay
- **Time-based matches**: Games ending by timelimit now properly stop recordings and manage state
- **Experiment continuity**: Both fraglimit and timelimit preserve experiment sequence
- **Player experience**: Clear messaging for both match end conditions

## 🔄 Migration Guide
- No configuration changes required
- Existing functionality preserved
- All match end conditions (fraglimit/timelimit) now handled consistently

---

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>