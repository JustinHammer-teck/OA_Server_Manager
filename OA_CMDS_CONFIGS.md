
### Commands 

```
/cl_noprint <0 or 1> - If enabled, it does not write text to console (and to upper left console notification area). This hides system messages, chat messages, etc. Default value is 0.


```


### Settings

```
cg_draw2d 	boolean 	Enables the graphics of the HUD. 

```


# OpenArena Console Commands & Configuration Variables Reference

## 1. Console Commands

###  Player Movement & Actions (Commands starting with `+` / `-`)
These are input bindings typically used in console or in `bind` scripts (e.g., `bind w "+forward"`):
- `+forward` / `-forward`: Start / stop moving forward  
- `+back` / `-back`: Move backwards  
- `+moveleft` / `-moveleft`: Strafe left  
- `+moveright` / `-moveright`: Strafe right  
- `+left` / `-left`: Turn left  
- `+right` / `-right`: Turn right  
- `+lookup` / `-lookup`: Look up  
- `+lookdown` / `-lookdown`: Look down  
- `+mlook` / `-mlook`: Mouse look (mouselook toggle)  
- `+zoom`: Zoom in (to `cg_zoomfov`)  
- `+attack` / `-attack`: Start / stop firing weapon  
- `+speed`: Toggle run/walk  
(*Additional Team Arena / Mods-specific `+buttonX` signals also exist*)  
:contentReference[oaicite:0]{index=0}

###  Gameplay & Utility Commands
- `bind <key> "<command>"`: Bind command to key  
- `bindlist`: List current key bindings  
- `exec <filename>`: Execute commands from config file (e.g., `autoexec.cfg`)  
- `record <filename>` / `stoprecord`: Record demo playback  
- `clientinfo`: Show client info (name, model, etc.)  
- `addbot <...>`: Add a bot with parameters (bot name, skill, team)  
- `kick <player>` / `clientkick <ID>`: Remove player (admin commands)  
- `banClient` / `banUser`: Ban players (slot/IP/CD-Key) in server context  
- `map` / `map_restart`: Load a map or restart current one  
- `callvote <command>`: Start a vote (map change, kick, etc.)  
- `vote yes` / `vote no`: Cast vote  
- `scores`: Display current scores  
- `clear`: Clear console text  
- `condump <file>`: Dump console output to file  
- `cmdlist`: List all available console commands  
- `cmd <...>`: Send remote console commands  
- `cinematic`: Play the intro cinematic (`RoQ`)  
- `centerview`: Reset view to center  
- `clientkick`: Similar to `kick` by ID  
- `addbot`: See above  
- `callteamvote`: Specific team vote commands  
:contentReference[oaicite:1]{index=1}

###  Developer, Debug & Logging
- `condump`, `logfile 0/1/2`: Console logging  
- `clear`: Clears console  
- `cmdlist`: List all commands  
:contentReference[oaicite:2]{index=2}

## 2. Configuration Variables (Cvars)

###  Basic Cvar Operations
- `/set <cvar> <value>`: Set a cvar (temporary)  
- `/seta <cvar> <value>`: Set and archive (saved to config)  
- `/sets <cvar> <value>`: Set and mark as serverinfo (visible in server listing)  
- `<cvar>`: Type alone to display current and default values  
- `+set <cvar> <value>`: On command line (launch OA with custom settings)  
- `unset <cvar>` / `reset <cvar>`: Remove or reset cvar to default  
:contentReference[oaicite:3]{index=3}

###  Common Gameplay Cvars (Fandom-based)
- `bot_nochat`: (0/1/2) Disable bot chat / team chat  
- `com_blood`: (0/1) Enable blood & gibs  
- `sv_allowDownload`: (0/1) Allow clients to download missing files  
- `con_notifytime`: Message on-screen time  
- `cg_draw2d`: Show HUD  
- `sv_hostname`: Set server name  
- Audio Cvars: `s_useOpenAL`, `s_alSources`, `cl_aviFrameRate` (video capture FPS)  
:contentReference[oaicite:4]{index=4}

###  Server & Dedicated Config Cvars (Debian manpage)
These can be set via `+set` when launching `openarena-server` or in server config:
- `capturelimit`, `fraglimit`, `timelimit`, `g_gametype`, `g_friendlyFire`, `g_gravity`, `g_quadfactor`, `g_weaponrespawn`, `nextmap`, `sv_hostname`, `sv_maxclients`, `sv_fps`, `sv_privateClients`, `sv_privatePassword`, `g_motd`, `sv_allowDownload`, `g_needpass`, etc.  
:contentReference[oaicite:5]{index=5}

###  Advanced Server Variables (OpenArena wiki)
- `dmflags`: Bitmask for no fall damage, default FOV, no footsteps, etc.  
- Elimination mode cvars: `elimination_activewarmup`, `elimination_selfdamage`, etc.  
- Various `sv_` cvars: `sv_floodProtect`, `sv_pure`, `sv_voip`, `sv_timeout`, `sv_zombietime`, and more.  

### Where weapon numbers correspond as follows:

1. Gauntlet
2. Machinegun
3. Shotgun
4. Grenade Launcher
5. Rocket Launcher
6. Lightning Gun
7. Railgun
8. Plasma Gun
9. BFG10K
