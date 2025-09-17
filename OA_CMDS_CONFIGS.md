# Quake III Console Commands (from Joz3D Archive)

| Command | Description                                                                                                                                                                                                                                                                                                                  |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| +attack | start attacking (shooting, punching)                                                                                                                                                                                                                                                                                         |
| +back | start moving backwards                                                                                                                                                                                                                                                                                                       |
| +button0 | start firing same as mouse button 1 (fires weapon)                                                                                                                                                                                                                                                                           |
| +button1 | start displaying chat bubble                                                                                                                                                                                                                                                                                                 |
| +button2 | start using items (same as enter)                                                                                                                                                                                                                                                                                            |
| +button3 | start player taunt animation                                                                                                                                                                                                                                                                                                 |
| +button4 | fixed +button4 not causing footsteps "John Carmack"                                                                                                                                                                                                                                                                          |
| +button5 | used for MODS also used by Team Arena Mission Pack                                                                                                                                                                                                                                                                           |
| +button6 | used for MODS also used by Team Arena Mission Pack                                                                                                                                                                                                                                                                           |
| +button7 | start hand signal, player model looks like it's motioning to team "move forward" (Team Arena Models Only)                                                                                                                                                                                                                    |
| +button8 | start hand signal, player model looks like it's motioning to team "come here" (Team Arena Models Only)                                                                                                                                                                                                                       |
| +button9 | stop hand signal, player model looks like it's motioning to team "come to my left side" (Team Arena Models Only)                                                                                                                                                                                                             |
| +button10 | start hand signal, player model looks like it's motioning to team "come to my right side" (Team Arena Models Only)                                                                                                                                                                                                           |
| +button11 | —                                                                                                                                                                                                                                                                                                                            |
| +button12 | —                                                                                                                                                                                                                                                                                                                            |
| +button13 | —                                                                                                                                                                                                                                                                                                                            |
| +button14 | —                                                                                                                                                                                                                                                                                                                            |
| +forward | start moving forward                                                                                                                                                                                                                                                                                                         |
| +info | start displaying server information (sv_hostname, map, rules, g_gametype, fraglimit)                                                                                                                                                                                                                                         |
| +left | start turning left                                                                                                                                                                                                                                                                                                           |
| +lookdown | start looking down                                                                                                                                                                                                                                                                                                           |
| +lookup | start looking up                                                                                                                                                                                                                                                                                                             |
| +mlook | start using mouse movements to control head movement                                                                                                                                                                                                                                                                         |
| +movedown | start moving down (crouch, climb down, swim down)                                                                                                                                                                                                                                                                            |
| +moveleft | start strafing to the left                                                                                                                                                                                                                                                                                                   |
| +moveright | start strafing to the right                                                                                                                                                                                                                                                                                                  |
| +moveup | start moving up (jump, climb up, swim up)                                                                                                                                                                                                                                                                                    |
| +right | start turning right                                                                                                                                                                                                                                                                                                          |
| +scores | start displaying current scores                                                                                                                                                                                                                                                                                              |
| +speed | speed toggle bound to shift key by default toggles run/walk                                                                                                                                                                                                                                                                  |
| +strafe | start changing directional movement into strafing movement                                                                                                                                                                                                                                                                   |
| +zoom | zoom in to fov specified by the zoomfov variable                                                                                                                                                                                                                                                                             |
| addbot | add one bot <botlib> name of the bot library <name> name of the bot <skin> skin of the bot <charfile> file with the bot character <charname> name of the character - "Mr. Elusive" bots can be given a fractional skill when adding them from the console. for instance use "/addbot grunt 4.6 blue" to add a 4.5 skill Grunt to team blue. |
| arena | load arena and bots "name" from arena.txt (arena <name>)                                                                                                                                                                                                                                                                     |
| -attack | stop attacking (shooting, punching)                                                                                                                                                                                                                                                                                          |
| -back | stop moving backwards                                                                                                                                                                                                                                                                                                        |
| banClient | ban a client by slot number used in conjunction with serverstatus you can ban players by their slot number regardless of player name (from server console only) part of the client banning system which depends on a master banned list on the master server at id software                                                  |
| banUser | ban a client by their player name. once the name is entered the players name, IP, and CD-Key are sent to the master server where the player will be banned for a length of time determined by id software.                                                                                                                   |
| bind | assign a key to command(s). `(bind <key> "<command>")`                                                                                                                                                                                                                                                                       |
| bindlist | list all currently bound keys and what command they are bound to                                                                                                                                                                                                                                                             |
| -button0 | stop firing same as mouse button 1 (fires weapon)                                                                                                                                                                                                                                                                            |
| -button1 | stop displaying chat bubble                                                                                                                                                                                                                                                                                                  |
| -button2 | stop using items (same as releasing enter)                                                                                                                                                                                                                                                                                   |
| -button3 | stop player taunt animation                                                                                                                                                                                                                                                                                                  |
| -button4 | fixed +button4 not causing footsteps "John Carmack"                                                                                                                                                                                                                                                                          |
| -button5 | used for MODS also used by Team Arena Mission Pack                                                                                                                                                                                                                                                                           |
| -button6 | used for MODS also used by Team Arena Mission Pack                                                                                                                                                                                                                                                                           |
| -button7 | stop hand signal, player model looks like it's motioning to team "move forward" (Team Arena Models Only)                                                                                                                                                                                                                     |
| -button8 | stop hand signal, player model looks like it's motioning to team "come here" (Team Arena Models Only)                                                                                                                                                                                                                        |
| -button9 | stop hand signal, player model looks like it's motioning to team "come to my left side" (Team Arena Models Only)                                                                                                                                                                                                             |
| -button10 | stop hand signal, player model looks like it's motioning to team "come to my right side" (Team Arena Models Only)                                                                                                                                                                                                            |
| -button11 | —                                                                                                                                                                                                                                                                                                                            |
| -button12 | —                                                                                                                                                                                                                                                                                                                            |
| -button13 | —                                                                                                                                                                                                                                                                                                                            |
| -button14 | —                                                                                                                                                                                                                                                                                                                            |
| callteamvote | allows a team to vote for a captain or team leader                                                                                                                                                                                                                                                                           |
| callvote | `callvote <command> vote <y/n>` — Caller automatically votes yes; vote has a 30 second timeout; each client can only call 3 votes a level. Vote commands are: map_restart, nextmap, map, g_gametype and kick.                                                                                                                |
| centerview | quickly move current view to the center of screen                                                                                                                                                                                                                                                                            |
| changeVectors | change to vector defined by FIND_NEW_CHANGE_VECTORS as in vector graphics                                                                                                                                                                                                                                                    |
| cinematic | play the q3a movie RoQ files (cinematic intro.RoQ)                                                                                                                                                                                                                                                                           |
| clear | clear all text from console                                                                                                                                                                                                                                                                                                  |
| clientinfo | display name, rate, number of snaps, player model, rail color, and handicap (state number?)                                                                                                                                                                                                                                  |
| clientkick | kick a client by slot number used in conjunction with serverstatus you can kick players by their slot number regardless of player name (from server console only)                                                                                                                                                            |
| cmd | send a command to server remote console                                                                                                                                                                                                                                                                                      |
| cmdlist | list all available console commands                                                                                                                                                                                                                                                                                          |
| condump | `condump "x"` write the console text to a file where `"x"` is the name of that file                                                                                                                                                                                                                                          |
| configstrings | list the current config strings in effect                                                                                                                                                                                                                                                                                    |
| connect | connect to server (connect 204.52.135.50) or (connect serverURL.com)                                                                                                                                                                                                                                                         |
| crash | causes Q3TEST.EXE to perform an illegal operation in Windows                                                                                                                                                                                                                                                                 |
| cvar_restart | reset all variables back to factory defaults (could be handy)                                                                                                                                                                                                                                                                |
| cvarlist | list all available console variables and their values                                                                                                                                                                                                                                                                        |
| demo | play demo (`demo q3demo001.dm3`)                                                                                                                                                                                                                                                                                             |
| devmap | load maps in development mode? (loads map with cheats enabled)                                                                                                                                                                                                                                                               |
| dir | display directory if syntax is correct ex. `(dir \)` or `(dir ..\)` or `(dir ..\baseq3)`                                                                                                                                                                                                                                     |
| disconnect | disconnects you from server (local included)                                                                                                                                                                                                                                                                                 |
| dumpuser | display user info (handicap, model/color, rail color, more…)(dumpuser "<name>")                                                                                                                                                                                                                                              |
| echo | echo a string to the message display to your console only                                                                                                                                                                                                                                                                    |
| error | execute an error routine to protect the server                                                                                                                                                                                                                                                                               |
| exec | execute a config file or script                                                                                                                                                                                                                                                                                              |
| fdir | search directory for file filters, e.g. `fdir *q3dm?.bsp`                                                                                                                                                                                                                                                                    |
| follow | switch to follow mode (`follow "<name>"`) or follow1/2 etc.                                                                                                                                                                                                                                                                  |
| gfxinfo | returns extensive information about video settings                                                                                                                                                                                                                                                                           |
| fs_openedList | display the file name of open pak files (pk3)                                                                                                                                                                                                                                                                                |
| Fs_pureList | displays contents of the `sv_referencedPaks` variable                                                                                                                                                                                                                                                                        |
| Fs_referencedList | display the contents of `sv_referencedPakNames` variable                                                                                                                                                                                                                                                                     |
| give | (cheat) give player item (give railgun)                                                                                                                                                                                                                                                                                      |
| globalservers | list public servers on the internet                                                                                                                                                                                                                                                                                          |
| god | cheat – give player invulnerability                                                                                                                                                                                                                                                                                          |
| heartbeat | send a manual heartbeat to the master servers                                                                                                                                                                                                                                                                                |
| hunk_stats | returns value of some registers: how many bits high/low and total (memory stats)                                                                                                                                                                                                                                             |
| imagelist | list currently open images/textures used by the current map; also shows the amount of texture memory the map is using                                                                                                                                                                                                        |
| in_restart | restarts all the input drivers, joystick, etc                                                                                                                                                                                                                                                                                |
| -info | stop displaying server information (sv_hostname, map, rules, g_gametype, fraglimit)                                                                                                                                                                                                                                          |
| joy_advancedupdate | removed — joy support still broken                                                                                                                                                                                                                                                                                           |
| kick | kick the player with the given name off the server                                                                                                                                                                                                                                                                           |
| kill | kills your player (suicide)                                                                                                                                                                                                                                                                                                  |
| killserver | stops server from running and broadcasting heartbeat                                                                                                                                                                                                                                                                         |
| -left | stop turning left                                                                                                                                                                                                                                                                                                            |
| levelshot | display the image used at the end of a level                                                                                                                                                                                                                                                                                 |
| loaddefered | load models and skins that have not yet been loaded                                                                                                                                                                                                                                                                          |
| loaddeferred | load models and skins that have not yet been loaded (corrected spelling)                                                                                                                                                                                                                                                     |
| localservers | list servers on LAN or local subnet only                                                                                                                                                                                                                                                                                     |
| -lookdown | stop looking down                                                                                                                                                                                                                                                                                                            |
| -lookup | stop looking up                                                                                                                                                                                                                                                                                                              |
| map | loads specified map (e.g. `map q3dm7`)                                                                                                                                                                                                                                                                                       |
| map_restart | resets the game on the same map (also plays fight! sound file and displays FIGHT!) A \map_restart allows to apply the change without waiting for natural match end                                                                                                                                                           |
| meminfo | meminfo command replaces `hunk_stats` and `z_stats`                                                                                                                                                                                                                                                                          |
| messagemode | send a message to everyone on the server                                                                                                                                                                                                                                                                                     |
| messagemode2 | send a message to teammates                                                                                                                                                                                                                                                                                                  |
| messagemode3 | send a message to tourney opponents?                                                                                                                                                                                                                                                                                         |
| messagemode4 | send a message to attacker? (does not work)                                                                                                                                                                                                                                                                                  |
| midiinfo | display information about MIDI music system                                                                                                                                                                                                                                                                                  |
| -mlook | stop using mouse look                                                                                                                                                                                                                                                                                                        |
| model | display the name of current player model if no parameters are given (see also model variable)                                                                                                                                                                                                                                |
| modelist | list of accessible screen resolutions                                                                                                                                                                                                                                                                                        |
| modellist | list of currently open player models                                                                                                                                                                                                                                                                                         |
| -movedown | stop moving down (crouch, climb down, swim down)                                                                                                                                                                                                                                                                             |
| -moveleft | stop strafing to the left                                                                                                                                                                                                                                                                                                    |
| -moveright | stop strafing to the right                                                                                                                                                                                                                                                                                                   |
| -moveup | stop moving up (jump, climb up, swim up)                                                                                                                                                                                                                                                                                     |
| music | plays specified music file (e.g. `music music.wav`)                                                                                                                                                                                                                                                                          |
| net_restart | reset all the network related variables like rate etc.                                                                                                                                                                                                                                                                       |
| nextframe | change the animation frame of testmodel etc. (bound to keys in default config)                                                                                                                                                                                                                                               |
| nextskin | change to next skin of testmodel etc.                                                                                                                                                                                                                                                                                        |
| noclip | no clipping mode — objects/walls are not solid                                                                                                                                                                                                                                                                               |
| notarget | bots will not fight/see you (good for screenshots)                                                                                                                                                                                                                                                                           |
| path | display all current game paths                                                                                                                                                                                                                                                                                               |
| ping | manually ping a server (by hostname or IP)                                                                                                                                                                                                                                                                                   |
| play | play a sound file (e.g. `play sound.wav`)                                                                                                                                                                                                                                                                                    |
| prevframe | previous frame (testmodel)                                                                                                                                                                                                                                                                                                   |
| prevskin | previous skin (testmodel)                                                                                                                                                                                                                                                                                                    |
| quit | quit arena and return to OS                                                                                                                                                                                                                                                                                                  |
| rcon | start a remote console to a server                                                                                                                                                                                                                                                                                           |
| reconnect | reconnect to last server you were connected to                                                                                                                                                                                                                                                                               |
| record | records a demo (e.g. `record mydemo.dm3`)                                                                                                                                                                                                                                                                                    |
| reset | reset specified variable (e.g. `reset model`) — single variable reset                                                                                                                                                                                                                                                        |
| restart | restart game on current map (server only)                                                                                                                                                                                                                                                                                    |
| -right | stop turning right                                                                                                                                                                                                                                                                                                           |
| s_info | display information about sound system                                                                                                                                                                                                                                                                                       |
| s_list | display filenames of sound files as they play                                                                                                                                                                                                                                                                                |
| s_stop | stop sound playing currently                                                                                                                                                                                                                                                                                                 |
| s_disable_a3d | disable A3D sound system support                                                                                                                                                                                                                                                                                             |
| s_enable_a3d | enable A3D sound support                                                                                                                                                                                                                                                                                                     |
| say | say message to everyone on server                                                                                                                                                                                                                                                                                            |
| say_team | say message only to your team                                                                                                                                                                                                                                                                                                |
| scanservers | scan LAN for servers                                                                                                                                                                                                                                                                                                         |
| -scores | stop displaying current scores                                                                                                                                                                                                                                                                                               |
| screenshot | save current view as TARGA image                                                                                                                                                                                                                                                                                             |
| screenshotJPEG | save current view as JPEG image                                                                                                                                                                                                                                                                                              |
| sectorlist | list sectors and number of entities in each on the current map                                                                                                                                                                                                                                                               |
| serverinfo | give server information from server console                                                                                                                                                                                                                                                                                  |
| serverstatus | display status of connected server + client slots                                                                                                                                                                                                                                                                            |
| serverrecord | record a server-side demo                                                                                                                                                                                                                                                                                                    |
| serverstop | stop server-side demo recording                                                                                                                                                                                                                                                                                              |
| set | set a cvar (non-archived)                                                                                                                                                                                                                                                                                                    |
| seta | set a cvar with archive flag (saved to config)                                                                                                                                                                                                                                                                               |
| sets | set a cvar with serverinfo flag (visible to clients)                                                                                                                                                                                                                                                                         |
| setu | set a cvar with userinfo flag                                                                                                                                                                                                                                                                                                |
| setenv | set environment variable                                                                                                                                                                                                                                                                                                     |
| setviewpos | sets the player’s view coordinates on the map                                                                                                                                                                                                                                                                                |
| shaderlist | list currently loaded shaders                                                                                                                                                                                                                                                                                                |
| showip | display your current IP address                                                                                                                                                                                                                                                                                              |
| sizedown | make viewport one size smaller                                                                                                                                                                                                                                                                                               |
| sizeup | make viewport one size larger                                                                                                                                                                                                                                                                                                |
| skinlist | list currently loaded skins                                                                                                                                                                                                                                                                                                  |
| snd_restart | reinitialize sound system                                                                                                                                                                                                                                                                                                    |
| soundinfo | info about sound system                                                                                                                                                                                                                                                                                                      |
| soundlist | list sound files in use                                                                                                                                                                                                                                                                                                      |
| spdevmap | load a devmap with bots spawned (cheats enabled)                                                                                                                                                                                                                                                                             |
| -speed | stop speed toggle (reverse of +speed)                                                                                                                                                                                                                                                                                        |
| spmap | load a map with bots spawned in standard (no cheats)                                                                                                                                                                                                                                                                         |
| startOrbit | start 3rd person display orbiting your player model                                                                                                                                                                                                                                                                          |
| stats | —                                                                                                                                                                                                                                                                                                                            |
| status | status of currently connected server                                                                                                                                                                                                                                                                                         |
| stoprecord | stop recording demo                                                                                                                                                                                                                                                                                                          |
| stopdemo | stop demo recording                                                                                                                                                                                                                                                                                                          |
| stopsound | stop currently playing sound                                                                                                                                                                                                                                                                                                 |
| -strafe | stop strafing movement                                                                                                                                                                                                                                                                                                       |
| systeminfo | returns values for: `g_syncronousClients, sv_serverid, timescale`                                                                                                                                                                                                                                                            |
| tcmd | display current target command or code address                                                                                                                                                                                                                                                                               |
| team | set player status / team / spectator etc.                                                                                                                                                                                                                                                                                    |
| teamtask | display/assign current team task (offense / defense / etc.)                                                                                                                                                                                                                                                                  |
| teamvote | allows casting a vote on a called team-vote                                                                                                                                                                                                                                                                                  |
| tell | send private message to individual player                                                                                                                                                                                                                                                                                    |
| tell_attacker | private message to your last known attacker?                                                                                                                                                                                                                                                                                 |
| tell_target | private message to last target?                                                                                                                                                                                                                                                                                              |
| testfog | (removed / dev) for fog emulation                                                                                                                                                                                                                                                                                            |
| testgun | hide weapon model + model test frames/skins                                                                                                                                                                                                                                                                                  |
| testmodel | spawn a model in front of you for viewing/testing skins/frames                                                                                                                                                                                                                                                               |
| testshader | apply a shader to map or model for testing                                                                                                                                                                                                                                                                                   |
| toggle | toggle a cvar between two values (e.g. `toggle cg_autoswitch`)                                                                                                                                                                                                                                                               |
| toggleconsole | open/close the console                                                                                                                                                                                                                                                                                                       |
| touchFile | make a zero-byte file (dev/test)                                                                                                                                                                                                                                                                                             |
| unbind | remove a key binding                                                                                                                                                                                                                                                                                                         |
| unbindall | remove all key bindings                                                                                                                                                                                                                                                                                                      |
| userinfo | list user info like via clientinfo                                                                                                                                                                                                                                                                                           |
| vid_restart | restart video / reinitialize graphics driver / resolution etc.                                                                                                                                                                                                                                                               |
| viewpos | returns player coordinates x y z on map                                                                                                                                                                                                                                                                                      |
| vminfo | display virtual machine interpreter info                                                                                                                                                                                                                                                                                     |
| vosay | use a predefined voice message to all                                                                                                                                                                                                                                                                                        |
| vosay_team | voice message to team only                                                                                                                                                                                                                                                                                                   |
| vote | cast vote (yes/no) on a previously called vote                                                                                                                                                                                                                                                                               |
| vsay | use predefined voice message to all                                                                                                                                                                                                                                                                                          |
| vsay_team | voice message to team only                                                                                                                                                                                                                                                                                                   |
| vstr | execute variable’s content as console command string                                                                                                                                                                                                                                                                         |
| vtaunt | voice taunt to all                                                                                                                                                                                                                                                                                                           |
| vtell | voice taunt to a specific player                                                                                                                                                                                                                                                                                             |
| vtell_attacker | voice taunt to your attacker                                                                                                                                                                                                                                                                                                 |
| vtell_target | voice taunt to your target                                                                                                                                                                                                                                                                                                   |
| wait | insert one game tick delay in script or command chain                                                                                                                                                                                                                                                                        |
| weapnext | switch to next weapon                                                                                                                                                                                                                                                                                                        |
| weapon | select a weapon by number (e.g. `weapon "5"`)                                                                                                                                                                                                                                                                                |
| weapprev | switch to previous weapon                                                                                                                                                                                                                                                                                                    |
| writeconfig | save current configuration to file                                                                                                                                                                                                                                                                                           |
| z_stats | display memory stats for Z-buffer etc                                                                                                                                                                                                                                                                                        |


C - cheat C - cheat
U - user (player)
A - archive
S - server
R - read only 

| Variable | Description | Class ID |
|---|---|---|
| class ID | activeaction "" | |
| arch "win98" | architecture/operating system | |
| bot_aasoptimize "0" | optimize the .aas file when one is written - MrElusive | |
| bot_challenge "0" | make the bot a bit more challenging - MrElusive | |
| bot_debug "0" | toggle debugging tool for bot code | |
| bot_developer "0" | toggle developer mode for bots | |
| bot_enable "0" | enable and disable adding of bots to the map/game | |
| bot_fastchat "0" | toggle between frequent and less frequent bot chat strings 1 = more often | |
| bot_forceclustering "0" | force recalculating the aas clusters - MrElusive | |
| bot_forcereachability "0" | force recalculating the aas reachabilities - MrElusive | |
| bot_forcewrite "0" | force writing out a new .aas file - MrElusive | |
| bot_grapple "0" | toggle determines weather the bots will use the grappling hook | |
| bot_groundonly "1" | this is a debug cvar to show areas which does not work in the retail version special thanks to - MrElusive | |
| bot_interbreedbots "10" | number of bots used for goal fuzzy logic interbreeding - MrElusive | |
| bot_interbreedchar "" | bot character to be used with goal fuzzy logic interbreeding - MrElusive | C |
| bot_interbreedcycle "20" | number of matches between interbreeding - MrElusive | C |
| bot_interbreedwrite "" | file to write interbreeded goal fuzzy logic to - MrElusive | C |
| bot_maxdebugpolys "128" | max number of polygons available for visualizing things when debugging MrElusive | |
| bot_memorydump "0" | possibly displays memory allocation/use for bots used for debugging? | C |
| bot_minplayers "0" | this is used to ensure a minimum numbers of players are playing on a server bots are added/removed to get the specified number of players in the game special thanks to - MrElusive | S |
| bot_nochat "0" | toggle determines weather bots will chat or not 0 = bots will chat | |
| bot_pause "0" | debug command to pause the bots - MrElusive | C |
| bot_predictobstacles "1" | possibly tells bot's to predict an obstacle and turn before running into it | |
| bot_reachability "0" | this is a debug cvar which does not work in the retail version - MrElusive | |
| bot_reloadcharacters "0" | this cvar if set to 1 disabled bot character file caching. used when creating bot characters while keeping Q3A running. kicking and re-adding a bot will reload the bot character files - MrElusive | |
| bot_report "0" | debug command to have the bots report what they are doing in CTF MrElusive | C |
| bot_rocketjump "1" | toggle determines weather the bots will use the rocket jump technique | |
| bot_saveroutingcache "0" | possibly allows the BOT AI to save routes for custom maps in memory. | C |
| bot_testclusters "0" | possibly a debug variable for testing BOT's on new terrain maps | C |
| bot_testichat "0" | used to test the initial bot chats. set this to 1 and add a bot. the bot will spit out all initial chats. - MrElusive | |
| bot_testrchat "0" | used to test the reply chats. set this to 1 and add one bot. the bot will always reply and dump all possible replies - MrElusive | |
| bot_testsolid "0" | test for "solid areas" in the .aas file (read the q3r manual) - MrElusive | C |
| bot_thinktime "100" | this is the time in milliseconds between two AI frames. - MrElusiveset the amount of time a bot thinks about a move before making it AI...(c: | |
| bot_usehook "0" | toggle determines weather the bots will use the grappling hook | |
| bot_visualizejumppads "0" | visualizes the default arch of a jumppad (read the q3r manual) - MrElusive | C |
| capturelimit "8" | set # of times a team must grab the others flag before the win is declared | S A |
| cg_animspeed "1" | toggle linear interpolation between successive frames in a player animation. 0 = no interpolation 1 = it does interpolate - Coriolis + WhatEver | C |
| cg_autoswitch "1" | auto-switch weapons (on pick-up) | A |
| cg_bobpitch "0.002" | set amount player view bobs forward/back while moving | A |
| cg_bobroll "0.002" | set amount player view rolls side to side while moving | A |
| cg_bobup "0.005" | set amount player view bobs up/down while moving | A |
| cg_brassTime "1250" | set amount of time a shell casing gets displayed if set to 0 the game engine will skip all shell eject code | A |
| cg_cameraOrbit "0" | change the step or increment units of the orbit rotation from one angle how much of a step to next angle | C |
| cg_cameraOrbitDelay "50" | change the rate at wich the camara moves to the next orbit position the higher the number the slower | A |
| cg_centertime "3" | set display time for center screen messages (0 off) | C |
| cg_crosshairHealth "1" | show health by the cross hairs (only works with #10 now?) - LOKi | A |
| cg_crosshairSize "24" | crosshair size...incase you have crosshair envy (c: | A |
| cg_crosshairX "0" | set X coordinates of the crosshair if cg_crosshairSize not 0 | A |
| cg_crosshairY "0" | set Y coordinates of the crosshair if cg_crosshairSize not 0 | A |
| cg_debuganim "0" | toggle model animation debug mode | C |
| cg_debugevents "0" | toggle event debug mode | C |
| cg_debugposition "0" | toggle player position debug mode | C |
| cg_deferPlayers "1" | the loading of player models will not take place until the next map, or when you die, or toggle the scoreboard (tab) this prevents the "hitch" effect when a player using a new model or skin joins the game after you. if you join the game after them the models and skins will download as you join? | A |
| cg_demoLook "0" | possibly to change the look of a recorded demo? | |
| cg_draw2D "1" | toggle the drawing of 2D items or text on the status display | A |
| cg_draw3dIcons "1" | toggle the drawing of 3D icons on the HUD off and on draw 2D icon for ammo if cg_draw3dicons 0 "John Carmack" | A |
| cg_drawAmmoWarning "1" | toggle low-ammo warning display | A |
| cg_drawAttacker "1" | toggle the display of last know assailant | A |
| cg_drawCrosshair "1" | select crosshair (change to zero if you have really good aim ha! ha!) 10 crosshairs to select from (cg_drawCrosshair 1 - 10) "John Carmack" | A |
| cg_drawCrosshairNames "1" | toggle displaying of the name of the player you're aiming at | A |
| cg_drawFPS "0" | toggle Frames Per Second display (when set to one "0" is default) | A |
| cg_drawFriend "1" | toggle the display of triangle shaped icon over the heads of your team mates | A |
| cg_drawGun "1" | toggle determines if the weapon you're holding is visible or not | A |
| cg_drawIcons "1" | toggle the drawing of any icons on the HUD and scoreboard | A |
| cg_drawRewards "1" | toggle display of award icons above the "you fragged..." message - LOKi | A |
| cg_drawKiller "1" | toggle display of player's name and picture that fragged you last | A |
| cg_drawSnapshot "0" | toggle the display of snapshots counter (# of snaps since game start) | A |
| cg_drawStatus "1" | draw the HUD. (toggle weather or not health and score are displayed) | A |
| cg_drawTeamOverlay "0" | set the drawing location of the team status overlay 1=top right 2=bottom right 3=bottom left of the screen it shows team player names, location, ammo (and what type weapon), and frag count for each player - LOKi | |
| cg_drawTimer "1" | show timer on HUD. shows time since map start counts up - LOKi | A |
| cg_errordecay "100" | helps to smooth animation during player prediction while experiencing packet loss or snapshot errors. "detect prediction errors and allow them to be decayed off over several frames to ease the jerk." from the source code comments cg_predict.c | |
| cg_extrapolate "1" | toggle blending of animations from one to the next (like a segue) - Andre | |
| cg_footsteps "1" | toggle the footstep sounds of all players (cheat protected) - LOKi | C |
| cg_forceModel "0" | force model selection, also forces player sounds "John Carmack" | A |
| cg_fov "90" | field of view/vision "90" is default higher numbers give peripheral vision. | A |
| cg_gibs "1" | toggle the display of animated gibs (explosions flying body parts!) | A |
| cg_gun "1" | toggle determines if the weapon your holding is visible or not | A |
| cg_gunX "0" | set X coordinates of viewable weapon if cg_drawGun is set to 1 | C |
| cg_gunY "0" | set Y coordinates of viewable weapon if cg_drawGun is set to 1 | C |
| cg_gunZ "0" | set Z coordinates of viewable weapon if cg_drawGun is set to 1 moves the gun model forward or backward in relation to the player models hold | C |
| cg_ignore "0" | used for debugging possibly like the notarget command | |
| cg_lagometer "1" | toggle the display of Lag-O-Meter on the HUD 1=netgraph 0=frag counter which changes color to reflect what place your in as well Section 6 of the Q3Test_Instructions_Readme.txt has a more detailed description of this tool. Simply put the top graph (blue/yellow): A vertical line is painted for every rendered frame. if the line is blue and going down from the baseline that indicates a steady transition of frames from one to the next. A yellow line going up from the baseline means the frames are not being fully rendered in time. The bottom graph (green/yellow/red): A vertical line is painted for every received snapshot. If the line is green it indicates properly received snapshots, with the height of the bar proportional to the ping. If the bar is yellow it indicates that the snapshot was held back because it hit the rate limit. If the line is red it means the snapshot was dropped by the network...Lots of thanx goes out to hacker, Erik, TeoH, and Wilka | A |
| cg_markoffset "1" | set marks (decals) offset. some video cards display the marks with the wrong offset, so you will be able to see the square decal that encapsulates the effect because the offset rises above the wall surface. change the offset the square goes away | |
| cg_marks "1" | toggle the marks the projectiles leave on the wall (bullet holes, etc) | A |
| cg_noplayeranims "0" | toggle player model animations. (the animation frame displayed when this is disabled is rather odd, though.) | C |
| cg_nopredict "0" | toggle client-side player prediction. (disabling causes the client to wait for updates from the server before updating the player location.) . | |
| cg_noProjectileTrail "0" | toggle the display of smoke trail effect behind rockets - Jax_Gator Dekard | A |
| cg_noTaunt "0" | possibly turn off the ability to hear voice taunts | A |
| cg_noVoiceChats "0" | possibly turn off the ability to hear voice chats | A |
| cg_noVoiceText "0" | possibly turn off the display of the voice chat text copied to the console | A |
| cg_oldPlasma "1" | toggle the use of old or new particle style plasma gun effect - 20 20 | A |
| cg_oldRail "0" | toggle the use of old or new spiral style rail trail effect - 20 20 | A |
| cg_oldRocket "1" | toggle the use of old or new style rocket trail effect - 20 20 | A |
| cg_predictItems "1" | toggle client-side item prediction. 0 option to not do local prediction of item pickup - John Carmack | U A |
| cg_railTrailTime "400" | set how long the railgun's trails last | A |
| cg_runpitch "0.002" | set amount player view bobs up and down while running | A |
| cg_runroll "0.005" | set amount player view rolls side to side while running (in 3rd person only?) | A |
| cg_scorePlums "1" | toggle the display of the floating scoring number balloons when a player scores a point or points (including negative points) in any game type, the awarded point value floats up from the target like a balloon and slowly fades out. | U A |
| cg_shadows "0" | set shadow detail level (0 = OFF, 1 = basic discs, 2 = stencil buffered 3 = simple stencil buffered(if r_stencilebits is not=0)) - Andre Lucas | A |
| cg_showcrosshair "1" | appeared in version 1.06 then removed in 1.07 now back in 1.08 then removed again in 1.09…hmm (replaced with multi-crosshairs) | |
| cg_showmiss "0" | toggle the display of missed packets or predictions on the HUD | |
| cg_simpleItems "0" | toggle the use of 2D sprite objects in place of the 3D animated objects makes some objects more "simple" (faster to render) - hacker | A |
| cg_smoothClients "0" | when g_smoothClients is enabled on the server and you enable cg_smoothClients then players in your view will be predicted and will appear more smooth even if they are on a bad network connection. however small prediction errors might appear. | U A |
| cg_stats "0" | toggles display of client frames in sequence missed frames are not shown | |
| cg_stereoSeparation "0.4" | the amount of stereo separation (for 3D glasses!) You ever take off your glasses at a 3D movie, remember how the images were separated into 3 colors? that's what this does | A |
| cg_swingSpeed "0.3" | set speed player model rotates to match position (1 is no delay, 0 will never turn) | C |
| cg_teamChatHeight "8" | set number of lines or strings of text that remain on screen in team play chat mode (messagemode2) values are 1 - 8 - LOKi | A |
| cg_teamChatsOnly "0" | when this is set to a one only chats from team mates will be displayed | A |
| cg_teamChatTime "3000" | set how long messages from teammates are displayed on the screen | A |
| cg_temp "0" | | |
| cg_testentities "0" | | |
| cg_thirdPerson "0" | toggle the use of and third person view | |
| cg_thirdPersonAngle "0" | change the angle of perspective you view your player (180 changes view to the front of the model) | C |
| cg_thirdPersonRange "40" | change the distance you view your player from when in 3rd person view | |
| cg_timescaleFadeEnd "1" | | |
| cg_timescaleFadeSpeed "0" | | |
| cg_tracerchance "0.4" | set frequency of tracer bullets (1 is all tracers) | C |
| cg_tracerlength "100" | set length of tracer bullets | C |
| cg_tracerwidth "1" | set width of tracer bullets | C |
| cg_trueLightning "0" | settings of the new shaft style. from the OSP readme...specifies the "lag" imposed on the rendering of the lightning gun shaft. a value of 0.0 is just like the baseq3 version "feel" of the LG. a value of 1.0 imposes no lag at all (shaft is always rendered on the crosshairs). a value of 0.5 is a good mix of the two to reduce the wet-noodle effect, while still maintaining consistency of where the server actually sees the shaft. I would like to thank all the readers who submitted good descriptions of this new variable to me, there were a ton, but the ones who had it correct are listed here. | A |
| cg_viewsize "100" | changes view port size 30 - 100 (you probably wouldn't want less than 100) | A |
| cg_zoomfov "22.5" | what the zoomed in field of view will be any thing more than 30 would not be sniper friendly | A |
| cg_waveamplitude "1" | | |
| cg_wavefrequency1 "0.4" | | |
| cheats "0" | enable cheating commands (give all) (serverside only) | S I L |
| cl_allowDownload "1" | toggle automatic downloading of maps, models, sounds, and textures | A |
| cl_anglespeedkey "1.5" | set the speed that the direction keys (not mouse) change the view angle | |
| cl_anonymous "0" | possibly to toggle anonymous connection to a server | U A |
| cl_avidemo "0" | toggle recording of a slideshow of screenshots records into the snapshot folder and appears to have overwritten some snapshots I had in there…)c: | |
| cl_cdkey "123456789" | variable to hold the CD key number to prevent bootleg/warez | A |
| cl_currentServerAddress | variable holds the IP address of the currently connected server | |
| cl_conXOffset "0" | offset the console message display 0 - top left 999 - extreme top right (off the page) | |
| cl_debugMove "0" | used for debugging cl_debugmove [1/2] from John Carmack's plan file | |
| cl_downloadName "" | variable holds filename of file currently downloading | |
| cl_forceavidemo "0" | | |
| cl_freelook "1" | toggle the use of freelook with the mouse (your ability to look up and down) | A |
| cl_freezeDemo "0" | stops a demo play back and freeze on one frame | |
| cl_maxpackets "30" | set the transmission packet size or how many packets are sent to client | A |
| cl_maxPing "800" | controls which servers are displayed in the in-game server browser - ata | A |
| cl_motd "1" | toggle the display of "Message of the day" When Quake 3 Arena starts a map up, it sends the GL_RENDERER string to the Message Of The Day server at id. This responds back with a message of the day to the client. If you wish to switch this option off, set CL_MOTD to 0. | |
| cl_motdString "" | possibly a MOTD from id's master server it is a read only variable | R |
| cl_mouseAccel "0" | toggle the use of mouse acceleration the mouse speeds up or becomes more sensitive as it continues in one direction | A |
| cl_nodelta "0" | disable delta compression (slows net performance, only use if net errors happen otherwise not recommended) | |
| cl_noprint "0" | printout messages to your screen or to the console (tired of all the chatter?) | |
| cl_packetdup "1" | default was 2 but changed to 1 since version 1.09 | A |
| cl_paused "0" | variable holds the status of the paused flag on the client side | R |
| cl_pitchspeed "140" | set the pitch rate when +lookup and/or +lookdown are active | A |
| cl_run "1" | always run...play without it I dare you! (c: | A |
| cl_running "1" | variable which shows weather or not a client game is running or weather we are in server/client mode (read only) | R |
| cl_serverStatusResendTime "750" | possibly allows the admin to change the rate of the heartbeats to the master server(s) | |
| cl_showmouserate "0" | show the mouse rate of mouse samples per frame (USB 1/per frame) | |
| cl_shownet "0" | display network quality info | |
| cl_showSend "0" | network debugging tool "John Carmack" | |
| cl_showTimeDelta "0" | display time delta between server updates | |
| cl_timeNudge "0" | effectively adds local lag to try to make sure you interpolate instead of extrapolate (try 100 for a really laggy server) | |
| cl_timeout "125" | seconds to wait before you are removed from the server when you lag out. | |
| cl_updateInfoString "" | "challenge\14985\motd\This is used by id when new versions come out" | R |
| cl_yawspeed "140" | set the yaw rate when +left and/or +right are active | A |
| cm_curveClipHack "0" | must have been a cheat!!! removed now | |
| cm_noAreas "0" | toggle the ability of the player bounding box to clip through areas? | C |
| cm_noCurves "0" | toggle the ability of the player bounding box to clip through curved surfaces | C |
| cm_playerCurveClip "1" | toggles the ability of the player bounding box to respect curved surfaces. | A C |
| color "1" | rail trail color blue/green/cyan/red/magenta/yellow/white respectively 1/2/3/4/5/6/7 | U A |
| color1 "2" | spiral rail trail color spiral core - special thanks to schiz Jax_Gator Dekard blue/green/cyan/red/magenta/yellow/white respectively 1/2/3/4/5/6/7 | U A |
| color2 "5" | spiral rail trail color spiral ring - special thanks to schiz Jax_Gator Dekard blue/green/cyan/red/magenta/yellow/white respectively 1/2/3/4/5/6/7 | U A |
| com_blood "1" | toggle the blood mist effect in the gib animations. 0 option for no gibs and no blood on hits "John Carmack" | A |
| com_buildScript "0" | possibly used for the loading and caching of game data like a list of things to be loaded and caches the data for quicker reloading | |
| com_cameraMode "0" | seems to toggle the view of your player model off and on when in 3D camera view | C |
| com_dropsim "0" | for testing simulates packet loss during communication drops | C |
| com_hunkMegs "20" | set the amount of memory you want quake3.exe to reserve for game play dedicated server memory optimizations. Tips: com_hunkMegs 4 sv_maxclients 3 bot_enable 0 "John Carmack" | A L |
| com_introplayed "1" | toggle displaying of intro cinematic once it has been seen this variable keeps it from playing each time, to see it again set this to zero | A |
| com_maxfps "100" | set max frames per second you receive from server (maxfps was removed) | A |
| com_showtrace "0" | toggle display of packet traces. 0=disables,1=toggles. | C |
| com_soundMegs "8" | com_soundmegs and com_zonemegs can be adjusted to provide better performance on systems with more than 64mb of memory. the default configuration is set to allow the game to run on a 64 MB system. on a 128 MB system we would run with the following:com_hunkMegs - 64 com_soundMegs - 16 com_zoneMegs - 24 | A L |
| com_speeds "0" | toggle display of frame counter, all, sv, cl, gm, rf, and bk whatever they are | |
| com_zoneMegs "16" | com_soundmegs and com_zonemegs can be adjusted to provide better performance on systems with more than 64mb of memory. the default configuration is set to allow the game to run on a 64 MB system. on a 128 MB system we would run with the following:com_hunkMegs - 64 com_soundMegs - 16 com_zoneMegs - 24 | A L |
| con_notifytime "3" | defines how long messages (from players or the system) are on the screen | |
| debuggraph "0" | | C |
| dedicated "0" | set console to server only 0 is a listen, 1 is lan, and 2 is internet (command line cvar causes engine not to load 3D game just a server console C:\Q3TEST\quake3.exe +set dedicated 2) - Dekard | L |
| developer "0" | enable developer mode (more verbose messages) | |
| dmflags "0" | set deathmatch flags originally I posted the values of Quake 2 dmflags but have since tested them and most of them don't work | |
| disable_<item name> | this command allows the administrator of a server to disable a particular item from the map. as an example: "/set disable_weapon_bfg 1" will make it so that the bfg does not show up. changing the value back to 0 and executing a /map_restart command will bring the disabled item back. - K2 | |
| disable.cfg | enable.cfg | |
| fixedtime "0" | toggle the rendering of every frame the game will wait until each frame is completely rendered before sending the next frame | C |
| fov "90" | field of view/vision "90" is default higher numbers give peripheral vision. | A |
| fraglimit "20" | set fraglimit on a server (0 is no limit) | S A |
| freelook "1" | steer aim and control head movement with the mouse…a must (c: | A |
| fs_basegame "" | allows people to base mods upon mods syntax to follow | I |
| fs_basepath "" | set base path root C:\Program Files\Quake III Arena for files to be downloaded from this path may change for TC's and MOD's | I |
| fs_cdpath "" | possibly a variable to use when the full CD was copied to the HDD | I |
| fs_copyfiles "0" | toggle if files can be copied from servers or if client will download | I |
| fs_debug "0" | possibly enables file server debug mode for download/uploads or something | |
| fs_game "" | set gamedir set the game folder/dir default is baseq3 (other for MODS) | S I |
| fs_homepath | possibly for TC's and MODS the default is the path to quake3.exe | I |
| fs_openedList "" | variable holds a list of all the pk3 files the client found | I |
| fs_referencedList "" | variable holds a list of all the pk3 files the client loaded data from | I |
| fs_restrict "" | demoversion if set to 1 restricts game to 4 arenas like the Q3A demo | I |
| g_aimTest "0" | removed possibly was a cheat (bot like aiming) | |
| g_allowVote "1" | toggle the use of voting on a server | |
| g_arenaName "0" | possibly toggles the display of the name of the current arena? | |
| g_arenaRank "" | possibly a variable to hold the value for your rank in the current series | A |
| g_arenaScores "" | possibly a variable to hold the value of previous arena series scores | A |
| g_arenasFile "" | sets the file name to use for map rotation and bot names and game type for each arena default scripts/arenas.txt within the PK3 file | R I |
| g_banIPs "" | ban specified TCP/IP address from connecting to your server | A |
| g_blueTeam "" | set the icon for the blue team (example Pagans) | S A |
| g_botsFile "" | sets the file name to use for setting up the bots configuration and characters for each bot default scripts/bots.txt within the PK3 file | R I |
| g_debugAlloc "0" | possibly debugging tool for memory allocation? | |
| g_debugDamage "0" | debugging tool for damage effects? | |
| g_debugMove "0" | debugging tool for brush/entity movements? | |
| g_doWarmup "0" | toggle the use of a warmup period before a match game | A |
| g_enableBreath "0" | enable breath in cold maps you can see the players breath - Dekard | |
| g_enableDust "0" | enable dust to be kicked up from feet in areas that have that map entity - Dekard | |
| g_filterBan "1" | toggle the banning of players that match a certain criteria/filter? | A |
| g_forcerespawn "10" | set the respawn time in seconds, 0 = don't force respawn | |
| g_friendlyFire "0" | toggle damage caused by friendly fire 1 = can kill or injure teammate | A |
| g_gametype "0" | 0 - Free For All 	1 - Tournament 	2 - Single Player<br>3 - Team Deathmatch 	4 - Capture the Flag 	<br>to start a dedicated server in tournament mode, you would use: quake3.exe +set dedicated 2 +set sv_zone tournaments +set g_gametype 1 +map q3tourney2, "Graeme Devine" thanks also to TheKiller<br>5 - One Flag CTF 	6 - Overload 	7 - Harvester (Team Arena only) | S L |
| g_gravity "800" | set the gravity level. (this is normally set by a property of the map loaded) | |
| g_inactivity "0" | set the amount of time a player can remain inactive before kicked | |
| g_knockback "1000" | the knockback from a weapon, higher number = greater knockback. | |
| g_listEntity "0" | toggles the display of map entities shows them by number | |
| g_log "1" | toggles logging of game data or statistics John Carmack made g_log a filename instead of a 0/1 in this version | A |
| g_logSync "0" | toggle the logging to append to the existing file and not overwrite | A |
| g_maxGameClients "0" | set maximum # of players who may join the game the remainder of clients are forced to spectate - Holesinswiss | S A L |
| g_motd "" | set message of the day to "X" (see "cl_motd" to display it) | |
| g_needpass "0" | variable alerts the client that a password is needed to join your server | S R |
| g_password "" | set the serverside password players use to get on the server | U |
| g_podiumDist "80" | sets the draw distance of the podium object player models stand on after a single player bot match - LOKi | |
| g_podiumDrop "70" | sets the height of the podium object player models stand on after a single player bot match - LOKi | |
| g_quadfactor "3" | allows the admin to set the amount of damage the quad damage will do. | |
| g_rankings "0" | | |
| g_redTeam "" | set the team icon for the red team (example Stroggs) | S A |
| g_restarted "0" | read only variable that is toggled when the game has been restarted in match mode this sets an event trap for if warmup is needed | R |
| g_singlePlayer "0" | possibly to allow 3rd party's to make TC's for single player style games? | R |
| g_smoothClients "1" | enable players to use the smooth clients option on the server (cg_smoothClients) | |
| g_spAwards "" | variable holds the names of the award icons that have been earned in the tier levels in single player mode | R A |
| g_speed "320" | how fast you move in Q3Test. The greater the number, the greater the velocity | |
| g_spScores1 "" | holds your scores on skill level 1 in single player games - Dr Qube | R A |
| g_spScores2 "" | holds your scores on skill level 2 in single player games - Dr Qube | R A |
| g_spScores3 "" | holds your scores on skill level 3 in single player games - Dr Qube | R A |
| g_spScores4 "" | holds your scores on skill level 4 in single player games - Dr Qube | R A |
| g_spScores5 "" | holds your scores on skill level 5 in single player games - Dr Qube | R A |
| g_spSkill "2" | holds your current skill level for single player 1 = I can win 2 = bring it on 3 = hurt me plenty 4 = hardcore and 5 = nightmare | A L |
| g_spVideos "" | variable holds the names of the cinematic videos that are unlocked at the end of each tier completion | R A |
| g_syncronousClients "0" | toggle synching of all client movements (1 required to record server demo) show "snc" on lagometer "John Carmack" | |
| g_teamAutoJoin "0" | toggle the automatic joining of the smallest or loosing team | A |
| g_teamForceBalance "0" | toggle the forcing of teams to be as even as possible on a server | A |
| g_warmup "" | the warmup time for tournament play is set with g_warmup. A tournament game is implicitly a one on one match, and further players are automatically entered as spectators (note, when the game starts, all clients, including the spectators respawn). You can follow the players by using Steam follow1T, Steam follow2T, and you can be a scoreboard by using Steam scoreboardT., "Graeme Devine" | A |
| g_weaponrespawn "5" | set time before a picked up weapon will respawn again 0 = weapons stay | |
| g_weaponTeamRespawn "30" | | |
| gamedate "" | Aug 20 2001 | R |
| gamename "baseq3" | display the game name for TC's basedir would be other than baseq3 | S R |
| graphheight "32" | set height, in pixels?, for graph displays | C |
| graphscale "1" | set scale multiplier for graph displays | C |
| graphshift "0" | set offset for graph displays | C |
| handicap "100" | set player handicap (max health), valid values 1 - 99 | U A |
| headmodel "" | changes only the head of the model to another model Example: If you are playing as the Grunt model, /headmodel "sarge" will stick Sarge's head on Grunt's body selecting a new model will load both the model and its matching head | U A |
| host_speeds "0" | toggle the display of timing information sv=server cl=client gm=gametime rf=render time all=total time | |
| in_debugjoystick "0" | possibly to set the debug level of direct input | |
| in_joyBallScale "0.02" | possibly sets the scale of a joyball rotation to player model rotation? | A |
| in_joyBall "0" | possibly to allow support for trackball style joy sticks and orb's | A |
| in_joystick "0" | toggle the initialization of the joystick (command line) | A L |
| in_midi "0" | toggle the use of a midi port as an input device r-d-x | A |
| in_midichannel "1" | toggle the use of a midi channel as an input device r-d-x | A |
| in_mididevice "0" | toggle the use of a midi device as an input device r-d-x | A |
| in_midiport "1" | toggle the use of a midi port as an input device r-d-x | A |
| in_mouse "1" | toggle initialization of the mouse as an input device (command line) | AL |
| journal "0" | possibly logs console events but is read only and can not be toggled | I |
| joy_threshold "0.15" | possibly an overall threshold setting all other joy variables removed in 1.08 | A |
| logfile "0" | enable console logging 0=no log 1=buffered 2=continuous 3=append so as not to overwrite old logs | |
| m_filter "1" | toggle use of mouse "smoothing" | A |
| m_forward "0.25" | set the back and forth movement distance of the player in relation to how much the mouse moves | A |
| m_pitch "0.022" | set the up and down movement distance of the player in relation to how much the mouse moves | A |
| m_side "0.25" | set the strafe movement distance of the player in relation to how much the mouse moves | A |
| m_yaw "0.022" | set the speed at which the player's screen moves left and right while using the mouse | A |
| mapname "" | display the name of the current map being used | S R |
| memorydump "0" | possibly used for debugging memory allocation/use? | |
| maxfps "0" | set the max frames per second the server should send you | |
| model "visor/blue" | set the model used to represent your player Hey John a 3D Keen model would be nice…(c: | U A |
| name "Commander Keen" | pick your own be original (no Player) | U A |
| net_ip "localhost" | variable holds the IP of the local machine (or the "hosts" name) passed from the OS environment | L |
| net_noipx "0" | toggle the use of IPX/SPX network protocol (command line only) | A L |
| net_noudp "0" | toggle the use of TCP/IP network protocol (command line only) | A L |
| net_port "27960" | set port number server will use if you want to run more than one instance of Q3A server on the same machine | L |
| net_qport "16392" | set internal network port. this allows more than one person to play from behind a NAT router by using only one IP address - Questy | I |
| net_socksEnabled "0" | toggle the use of network socks 5 protocol enabling firewall access (only settable at init time from the OS command line) - Graeme Devine | A L |
| net_socksPassword "" | variable holds password for socks firewall access supports no authentication and username/password authentication method (RFC-1929); it does NOT support GSS-API method (RFC-1961) authentication (only settable at init time from the OS command line) - Graeme Devine | A L |
| net_socksPort "1080" | set proxy and/or firewall port default is 1080 (only settable at init time from the OS command line) - Graeme Devine | A L |
| net_socksServer "" | set the address (name or IP number) of the SOCKS server (firewall machine), NOT a Q3ATEST server. (only settable at init time from the OS command line) - Graeme Devine | A L |
| net_socksUsername "" | variable holds username for socks firewall supports no authentication and username/password authentication method (RFC-1929); it does NOT support GSS-API method (RFC-1961) authentication (only settable at init time from the OS command line) - Graeme Devine | A L |
| nextmap "" | variable holds the name of the next map in the server rotation myserver.cfg | |
| password "" | set password for entering a password protected server | U |
| pmove_fixed "0" | typically the player physics advances in small time steps. when this option is enabled all players will use fixed frequency player physics, the time between two advances of the phsysics will be the same for all players. the actual time between two advances of the player physics can be set with the pmove_msec variable. enabling this option will make the player physics the same for all players independent from their framerate. should do what you want for prediction and should even out the machine dependent rates. - Robert Duffy | |
| pmove_msec "8" | set the time in milliseconds between two advances of the player physics. should do what you want for prediction and should even out the machine dependent rates. - Robert Duffy | |
| protocol "66" | display network protocol version. Useful for backward compatibility with servers with otherwise incompatible versions < maddog read only | S R |
| r_allowExtensions "1" | use all of the OpenGL extensions your card is capable of | AL |
| r_allowSoftwareGL "0" | toggle the use of the default software OpenGL driver supplied by the Operating System < maddog | L |
| r_ambientScale "0.5" | set the scale or intensity of ambient light | C |
| r_clear "0" | toggle the clearing of the screen between frames | C |
| r_colorbits "16" | set number of bits used for each color from 0 to 32 bit | AL |
| r_colorMipLevels "0" | "texture visualization tool" John Carmack | L |
| r_customaspect "1" | toggle the use of custom screen resolution/sizes | AL |
| r_customheight "1024" | custom resolution (Height) | AL |
| r_customwidth "1600" | custom resolution (Width) | AL |
| r_debuglight "0" | possibly toggle debugging of lighting effects | |
| r_debugSort "0" | possibly toggle debugging of sorting of list like scoreboard | C |
| r_debugSurface "0" | possibly used for debugging the curve rendering and possibly for map debugging. | C |
| r_debugSurfaceUpdate "1" | possibly used for debugging the curve rendering and possibly for map debugging. | |
| r_depthbits "16" | set number of bits used for color depth from 0 to 24 bit | A L |
| r_detailtextures "1" | toggle the use of detailed textures, when disabled every stage of a shader is rendered except those with the keyword "detail". when enabled detail stages are also rendered. in proper use the detail stages are supposed to enhance the texture's visual quality when viewed close up. more information is available in the shader manual included in the GTK Radiant install. - Rroff | A L |
| r_directedScale "1" | set scale/intensity of light shinning directly upon objects | C |
| r_displayRefresh "0" | monitor refresh rate in game (will change desktop settings too in Windows 98 anyway) | L |
| r_dlightBacks "1" | "brighter areas are changed more by dlights than dark areas. I don't feel TOO bad about that, because its not like the dlight is much of a proper lighting simulation even in the best case..."John Carmack | A |
| r_drawBuffer "GL_BACK" | set which frame buffer to draw into. basically you draw into a "back" buffer while simultaneously showing a "front" buffer. next frame you "swap" these. the benefit is that you won't "see" the actual painting of the image take place. - Questy/Carl | |
| r_drawentities "1" | toggle display of brush entities | C |
| r_drawstrips "1" | toggle triangle strips rendering method | |
| r_drawSun "1" | set to zero if you do not want to render sunlight into the equation of lighting effects | A |
| r_drawworld "1" | toggle rendering of map architecture | C |
| r_dynamiclight "0" | toggle dynamic lighting (different "dynamic" method of rendering lights) | A |
| r_ext_compiled_vertex_array "" | toggle hardware compiled vertex array rendering method default is 1 | AL |
| r_ext_compress_textures "1" | toggle compression of textures | AL |
| r_ext_compressed_textures "1" | toggle compression of textures (1.27g changed to past tense compressed) | AL |
| r_ext_gamma_control "1" | enable external gamma control settings | AL |
| r_ext_multitexture "1" | toggle hardware mutitexturing if set to zero is a direct FPS benefit | AL |
| r_ext_swapinterval "1" | toggle hardware frame swapping | AL |
| r_ext_texenv_add "1" | possible duplicate cvar or an extension to the r_ext_texture_add variable | AL |
| r_ext_texture_env_add "1" | toggle additive blending in multitexturing. If not present, OpenGL limits you to multiplicative blending only, so additive will require an extra pass. - Questy/Carl | AL |
| r_facePlaneCull "1" | toggle culling of brush faces not in view (0 will slow FPS) | A |
| r_fastsky "1" | toggle fast rendering of sky if set to 1 (0 is default and will slow FPS when outdoors 1 will disable your ability to see through portals)...Thanx hacker | A |
| r_finish "1" | toggle synchronization of rendered frames (engine will wait for GL calls to finish) | A |
| r_fixtjunctions "1" | toggle fixing of a problem with a certain type of vertex in models that can make gaps appear between polygons - Andre Lucas | L |
| r_flareFade "7" | set scale of fading of flares in relation to distance | C |
| r_flares "0" | toggle projectile flare and lighting effect. the flare effect is a translucent disk that is used to alter the colors around lights with a corona effect | A |
| r_flaresSize "40" | set the size of flares? I wish you could make the big balls smaller now those are flares | C |
| r_fullbright "0" | toggle textures to full brightness level (is set as a cheat code?) boy who turned on the lights…(c: | L C |
| r_fullscreen "1" | toggle full screen or play in a window | A L |
| r_gamma "1" | gamma correction | A |
| r_glDriver "opengl32" | used "x" OpenGL driver (Standard OpenGL32 or 3dfxvgl) | A L |
| r_ignore "0" | possibly ignores hardware driver settings in favor of variable settings | C |
| r_ignoreFastPath "0" | possibly to disable the looking outside of the PAK file first feature in case of duplicate file names etc. | A L |
| r_ignoreGLErrors "1" | ignores OpenGL errors that occur | A |
| r_ignorehwgamma "0" | possibly to toggle the use of DirectX gamma correction or video driver gamma correction? | A L |
| r_ignoreOffset "0" | see r_offsetfactor this will just turn the offset off completely | A L |
| r_inGameVideo "1" | toggle the display of in game animations on bigscreen map objects that display a camera view of the current game | A |
| r_intensity "1" | increase brightness of texture colors (may be like gl_modulate?) | L |
| r_lastValidRenderer "" | last known video driver (RIVA 128/RIVA 128 ZX (PCI)) | A |
| r_lightmap "0" | toggle entire map to full brightness level all textures become blurred with light (is set as a cheat code?) | |
| r_lightningSegmentLength "32" | possibly to set the distance between bends in the lightning bolt of the lightning gun…(c: | A |
| r_lockpvs "0" | disable update to PVS table as player moves through map (new areas not rendered) - Randy | C |
| r_lockview "0" | possibly was intended to lock a certain Field Of View (FOV) is removed now | |
| r_lodbias "0" | change the geometric level of detail (0 - 2) | A |
| r_lodCurveError "250" | another level of detail setting if set to 10000 "don't drop curve rows for a long time" John Carmack (really mean 3D cards only??) | A |
| r_lodscale "5" | set scale for level of detail adjustment | C |
| r_logFile "0" | possibly toggles logging of rendering errors | C |
| r_mapOverBrightBits "2" | set intensity level of lights reflected from textures | L |
| r_maskMinidriver "0" | treat the current OpenGL32 driver as an ICD, even if it is in fact a MCD Questy/Zoid | L |
| r_maxpolys "600" | | |
| r_maxpolyverts "3000" | | |
| r_measureOverdraw "0" | overdraw' is when the same pixel is written to more than once when rendering a scene. I guess r_measureOverdraw is used to see how much is going on. used for software rendering | C |
| r_mode "3" | set video display mode (resolution), use listmodes for list of modes (3 is 640X480) | A L |
| r_nobind "0" | toggle the binding of textures to triangles | C |
| r_nocull "0" | toggle rendering of hidden objects (1=slow performance) | C |
| r_nocurves "0" | map diagnostic command toggle the use of curved geometry | C |
| r_nolightcalc "0" | disable lighting and shadow calculations…hmm | |
| r_noportals "0" | toggle player view through portals | C |
| r_norefresh "0" | toggle the refreshing of the rendered display | C |
| r_novis "0" | the VIS tables hold information about which areas should be displayed from other areas. | C |
| r_offsetfactor "-1" | control the OpenGL Polygon Offset, If you see lines appearing in decals, or they seem to flick on and off, these variables may help out. - Questy/Andre | C |
| r_offsetunits "-2" | see r_offsetfactor | C |
| r_overBrightBits "1" | possibly similar to r_mapOverBrightBits (no visible effect on mine) | A L |
| r_picmip "1" | set maximum texture size (0 - 3, 3=fastest 0=quality) | A L |
| r_portalOnly "0" | when set to "1" turns off stencil buffering for portals, this allows you to see the entire portal before it's clipped, i.e. more of the room, to get a better feel for who's in there before you jump in. | |
| r_preloadTextures "0" | enable video processor to pre-cache textures | A L |
| r_primitives "0" | set the rendering method. -1 = skips drawing 0 = uses glDrawElements if compiled vertex arrays are present, or strips of glArrayElement if not present 1 = forces strips 2 = forces drawElements 3 = path for non-vertex array testing "John Carmack" | A |
| r_printShaders "0" | possibly toggle the printing on console of the number of shaders used? | A |
| r_railCoreWidth "16" | set size of the rail trail's core | A |
| r_railSegmentLength "64" | set distance between rail "sun bursts" | A |
| r_railWidth "128" | set width of the rail trail | A |
| r_roundImagesDown "1" | set rounding down amount (larger = faster, lower quality) - Randy | A L |
| r_saveFontData "0" | | |
| r_showcluster "0" | toggle the display of clusters by number as the player enters them on the currently loaded map<maddog | C |
| r_showImages "0" | toggle displaying a collage of all image files when set to a one...texture use debugging tool | |
| r_shownormals "0" | toggle the drawing of short lines indicating brush and entity polygon vertices, useful when debugging model lighting - Andre Lucas < maddog | C |
| r_showsky "0" | enable rendering sky in front of other objects | C |
| r_showSmp "0" | toggle display of multi processor (SMP) info on the HUD | C |
| r_showtris "0" | map diagnostic command show triangles, pretty cool looking... | C |
| r_simpleMipMaps "1" | toggle the use of "simple" mip mapping. used to "dumb-down" resoluiton displays for slower machines - Questy | A L |
| r_singleShader "0" | possibly toggles use of 1 shader for objects that have multiple shaders | L C |
| r_skipBackEnd "0" | possibly to toggle the skipping of the backend video buffer | C |
| r_smp "0" | toggle the use of multi processor acceleration code | A L |
| r_speeds "0" | show the rendering info e.g. how many triangles are drawn added r_speeds timing info to cinematic texture uploads "John Carmack" | C |
| r_stencilbits "8" | stencil buffer size (0, 8bit, and 16bit) | A L |
| r_stereo "0" | toggle the use of stereo separation for 3D glasses | A L |
| r_subdivisions "4" | set maximum level of detail. (an example would be the complexity of curves. 1=highest detail) | A L |
| r_swapInterval "0" | toggle frame swapping. | A |
| r_texturebits "0" | set number of bits used for each texture from 0 to 32 bit | A L |
| r_textureMode "" | select texture mode. "GL_LINEAR_MIPMAP_NEAREST" (nearest or linear) | A |
| r_uiFullScreen "0" | | |
| r_verbose "0" | toggle display of rendering commands as they happen on the console | C |
| r_vertexLight "1" | enable vertex lighting (faster, lower quality than lightmap) removes lightmaps, forces every shader to only use a single rendering pass, no layered transparancy, environment mapping, world lighting is completely static, and there is no dynamic lighting when in vertex lighting mode. (recommend dynamiclight 0 and this 1) direct FPS benefit "John Carmack" | A L |
| r_znear "4" | set how close objects can be to the player before they're clipped out of the scene - Questy/Andre | C |
| rate "" | modem speed/rate of data transfer "4500" (take a zero off the end of your connection speed?) | U A |
| rconAddress "" | variable holds IP address of the server for rcon | |
| rconPassword "" | set password for remote console control of the server | |
| s_doppler "1.0" | vortex of sound - has a good description of this A3D variable | A |
| s_initsound "1" | toggle weather sound is initialized or not (on next game) | |
| s_khz "11" | set the sampling frequency of sounds lower=performance higher=quality | A |
| s_mixahead "0.2" | set delay before mixing sound samples. | A |
| s_mixPreStep "0.05" | possibly to set the prefetching of sound on sound cards that have that power | A |
| s_musicvolume "1" | music volume level 0=off | A |
| s_separation "0.5" | set separation between left and right sound channels (this one is it) | A |
| s_show "0" | toggle display of paths and filenames of all sound files as they are played. | C |
| s_testsound "0" | toggle a test tone to test sound system. 0=disables,1=toggles. | C |
| s_volume "0.7" | Sound FX Volume | A |
| scr_conspeed "3" | set how fast the console goes up and down | |
| sensitivity "9" | set how far your mouse moves in relation to travel on the mouse pad | A |
| server1 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server2 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server3 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server4 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server5 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server6 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server7 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server8 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server9 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server10 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server11 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server12 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server13 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server14 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server15 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| server16 "" | holds IP/URL of a servers from the favorite servers list - Dr Qube | A |
| sex "male" | set gender for model characteristics (sounds, obituary's etc.) | U A |
| showdrop "0" | toggle display of dropped packets. 0=disables,1=toggles. | |
| showpackets "0" | toggle display of all packets sent and received. 0=disables,1=toggles. | |
| snaps "20" | set the number of snapshots sever will send to a client (server run at 40Hz, so use 40, 20, or 10) -Randy | U A |
| sv_allowAnonymous "0" | possibly to toggle the allowing of anonymous clients to connect to your server | S |
| sv_allowdownload "1" | toggle the ability for clients to download files maps etc. from server. . | |
| sv_cheats "1" | enable cheating commands (give all) (serverside only) | R |
| sv_floodProtect "1" | toggle server flood protection to keep players from bringing the server down | S A |
| sv_fps "20" | set the max frames per second the server sends the client | |
| sv_hostname "" | set the name of the server "Shadowlands" | S A |
| sv_keywords "" | variable holds the search string entered in the internet connection menu | S |
| sv_killserver "0" | if set to a one the server goes down (server console only I hope) | |
| sv_mapChecksum "" | allows check for client server map to match | R |
| sv_mapname "" | display the name of the current map being used on a server | S R |
| sv_master1 "" | set URL or address to master server "master3.idsoftware.com" | |
| sv_master2 "" | optional master 2 | A |
| sv_master3 "" | optional master 3 | A |
| sv_master4 "" | optional master 4 | A |
| sv_master5 "" | optional master 5 | A |
| sv_maxclients "8" | maximum number of people allowed to join the server dedicated server memory optimizations. Tips: com_hunkMegs 4 sv_maxclients 3 bot_enable 0 "John Carmack" | S A L |
| sv_maxPing "0" | set the maximum ping aloud on the server to keep HPB out | S A |
| sv_maxRate "" | option to force all clients to play with a max rate. This can be used to limit the advantage of LPB, or to cap bandwidth utilization for a server. Note that rate is ignored for clients that are on the same LAN. Father John stepping in, in the name of fairness…(c: (ever notice when 3 or so LPB's join a server your PING takes a dump? It's because your slice of the pie got smaller because theirs is so big…die bandwidth suckers) | S A |
| sv_minPing "0" | set the minimum ping aloud on the server to keep LPB out | S A |
| sv_padPackets "0" | possibly toggles the padding of network packets on the server PAD - Packet Assembler/Disassembler | |
| sv_pakNames "antilogic" | variable holds a list of all the pk3 files the server found "antilogic" | R |
| sv_paks "182784856 " | variable holds the checksum of all pk3 files | R |
| sv_paused "0" | allow the game to be paused from the server console? | R |
| sv_privateClients "0" | the number of spots, out of sv_maxclients, reserved for players with the server password (sv_privatePassword) - Holesinswiss | S |
| sv_privatePassword "" | set password for private clients to login with | |
| sv_pure "1" | disallow native DLL loading if sv_pure, requires clients to only get data from pk3 files the server is using "John Carmack" | |
| sv_reconnectlimit "3" | number of times a disconnected client can come back and reconnect | |
| sv_referencedPakNames "" | variable holds a list of all the pk3 files the server loaded data from. these pk3 files will be autodownloaded by a client if the client does not have them. "baseq3/pak2 baseq3/pak0" | R |
| sv_referencedPaks "" | variable holds the checksum of the referenced pk3 files | R |
| sv_running "1" | variable flag tells the console weather or not a local server is running | R |
| sv_serverid "" | hmm…"8021204" | R |
| sv_showloss "0" | toggle sever packet loss display | |
| sv_timeout "120" | sets the amount of time for the server to wait for a client packet before assuming a disconnected state. | |
| sv_zombietime "2" | the amount of time in minutes before a frozen character is removed from the map. | |
| sys_cpuid "33" | more snooping into your CPU | |
| sys_cpustring "" | variable holds a string that identifies your processor | |
| team_headmodel "" | set head of team_model to a head that will only be used during team game play | U A |
| team_model "" | set player model that will only be used during team game play | U A |
| teamoverlay "0" | toggle the drawing of the colored team overlay on the HUD | U R |
| teamtask "0" | variable holds the number of the team task you are currently asigned 1 - offense 2 - defense 3 - point/patroll 4 - following 5 - retrieving 6 - escort(gaurding flag carrier) 7 - camping | U |
| timedemo "0" | when set to "1" times a demo and returns frames per second like a benchmark | C |
| timegraph "0" | toggle the display of the timegraph. . | C |
| timelimit "0" | amount of time before new map loads or next match begins | S A |
| timescale "1" | set the ratio between game time and real time | C |
| ui_bigFont "0.4" | | A |
| ui_browserGameType "0" | set server search game type in the browser list (see g_gametype) | A |
| ui_browserMaster "0" | set server search 0=LAN 1=Mplayer 2=Internet 3=Favorites - WeeJoker | A |
| ui_browserShowEmpty "1" | toggle the displaying of empty servers in the browser list | A |
| ui_browserShowFull "1" | toggle the displaying of full servers in the browser list | A |
| ui_browserSortKey "4" | set the field number to sort by in the browser list 0=Server Name 1=Map Name 2=Open Player Spots 3=Game Type 4=PingTime | A |
| ui_cdkeychecked "1" | set to a 1 after the cdkey has been checked so won't ask again | R |
| ui_ctf_capturelimit "8" | set the menu default capture limit for single player bot matches | A |
| ui_ctf_friendly "0" | toggle team mate damage in single player CTF bot matches | A |
| ui_ctf_timelimit "30" | set the menu default CTF time limit for single player bot matches | A |
| ui_ffa_fraglimit "20" | set the menu default frag limit for single player FFA bot matches | A |
| ui_ffa_timelimit "0" | set the menu default time limit for single player FFA bot matches | A |
| ui_singlePlayerActive "0" | | |
| ui_smallFont "0.25" | | A |
| ui_spSelection "2" | set the menu default gametype of single player? 16 = CTF 2 = FFA DM | R |
| ui_team_fraglimit "0" | set the menu default frag limit for single player team bot matches | A |
| ui_team_friendly "1" | toggle default team mate damage in single player team bot matches | A |
| ui_team_timelimit "20" | set the menu default time limit for single player team bot matches | A |
| ui_tourney_fraglimit "0" | set the menu default frag limit for single player tourney bot matches | A |
| ui_tourney_timelimit "15" | sets the menu default time limit for single player tourney bot matches | A |
| username "vern" | variable holds your network login id from %username% env variable…hmmm? id hackers! | |
| version "" | Q3 1.30 win-x86 Aug 20 2001 | S R |
| vid_xpos "30" | x position when windowed | A |
| vid_ypos "30" | y position when windowed | A |
| viewlog "0" | toggle the display of the startup console window over the game screen | C |
| vm_cgame "0" | part of the virtual machine interpreter which allows PC MOD makers to not have to know MAC code and MAC MOD makers to not have to know PC | A |
| vm_game "0" | toggle the virtual machine interpreter, cgame can switch between being loaded as a binary .dll or an interpreted .qvm at the change of this cvar | A |
| vm_ui "0" | part of the virtual machine interpreter which allows PC MOD makers to not have to know MAC code and MAC MOD makers to not have to know PC | A |
| win_hinstance "" | address of the handle instance of quake3 under windows - LOKi | R |
| win_wndproc "" | hmm..."4368704" | R |


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
