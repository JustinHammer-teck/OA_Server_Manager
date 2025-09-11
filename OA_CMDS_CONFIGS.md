# Quake III Console Commands (from Joz3D Archive)

| Command | Description |
|---|---|
| +attack | start attacking (shooting, punching) |
| +back | start moving backwards |
| +button0 | start firing same as mouse button 1 (fires weapon) |
| +button1 | start displaying chat bubble |
| +button2 | start using items (same as enter) |
| +button3 | start player taunt animation |
| +button4 | fixed +button4 not causing footsteps "John Carmack" |
| +button5 | used for MODS also used by Team Arena Mission Pack |
| +button6 | used for MODS also used by Team Arena Mission Pack |
| +button7 | start hand signal, player model looks like it's motioning to team "move forward" (Team Arena Models Only) |
| +button8 | start hand signal, player model looks like it's motioning to team "come here" (Team Arena Models Only) |
| +button9 | stop hand signal, player model looks like it's motioning to team "come to my left side" (Team Arena Models Only) |
| +button10 | start hand signal, player model looks like it's motioning to team "come to my right side" (Team Arena Models Only) |
| +button11 | — |
| +button12 | — |
| +button13 | — |
| +button14 | — |
| +forward | start moving forward |
| +info | start displaying server information (sv_hostname, map, rules, g_gametype, fraglimit) |
| +left | start turning left |
| +lookdown | start looking down |
| +lookup | start looking up |
| +mlook | start using mouse movements to control head movement |
| +movedown | start moving down (crouch, climb down, swim down) |
| +moveleft | start strafing to the left |
| +moveright | start strafing to the right |
| +moveup | start moving up (jump, climb up, swim up) |
| +right | start turning right |
| +scores | start displaying current scores |
| +speed | speed toggle bound to shift key by default toggles run/walk |
| +strafe | start changing directional movement into strafing movement |
| +zoom | zoom in to fov specified by the zoomfov variable |
| addbot | add one bot <botlib> name of the bot library <name> name of the bot <skin> skin of the bot <charfile> file with the bot character <charname> name of the character - "Mr. Elusive" bots can be given a fractional skill when adding them from the console. for instance use "/addbot grunt 4.6 blue" to add a 4.5 skill Grunt to team blue. |
| arena | load arena and bots "name" from arena.txt (arena <name>) |
| -attack | stop attacking (shooting, punching) |
| -back | stop moving backwards |
| banClient | ban a client by slot number used in conjunction with serverstatus you can ban players by their slot number regardless of player name (from server console only) part of the client banning system which depends on a master banned list on the master server at id software |
| banUser | ban a client by their player name. once the name is entered the players name, IP, and CD-Key are sent to the master server where the player will be banned for a length of time determined by id software. |
| bind | assign a key to command(s). `(bind <key> "<command>")` |
| bindlist | list all currently bound keys and what command they are bound to |
| -button0 | stop firing same as mouse button 1 (fires weapon) |
| -button1 | stop displaying chat bubble |
| -button2 | stop using items (same as releasing enter) |
| -button3 | stop player taunt animation |
| -button4 | fixed +button4 not causing footsteps "John Carmack" |
| -button5 | used for MODS also used by Team Arena Mission Pack |
| -button6 | used for MODS also used by Team Arena Mission Pack |
| -button7 | stop hand signal, player model looks like it's motioning to team "move forward" (Team Arena Models Only) |
| -button8 | stop hand signal, player model looks like it's motioning to team "come here" (Team Arena Models Only) |
| -button9 | stop hand signal, player model looks like it's motioning to team "come to my left side" (Team Arena Models Only) |
| -button10 | stop hand signal, player model looks like it's motioning to team "come to my right side" (Team Arena Models Only) |
| -button11 | — |
| -button12 | — |
| -button13 | — |
| -button14 | — |
| callteamvote | allows a team to vote for a captain or team leader |
| callvote | `callvote <command> vote <y/n>` — Caller automatically votes yes; vote has a 30 second timeout; each client can only call 3 votes a level. Vote commands are: map_restart, nextmap, map, g_gametype and kick. |
| centerview | quickly move current view to the center of screen |
| changeVectors | change to vector defined by FIND_NEW_CHANGE_VECTORS as in vector graphics |
| cinematic | play the q3a movie RoQ files (cinematic intro.RoQ) |
| clear | clear all text from console |
| clientinfo | display name, rate, number of snaps, player model, rail color, and handicap (state number?) |
| clientkick | kick a client by slot number used in conjunction with serverstatus you can kick players by their slot number regardless of player name (from server console only) |
| cmd | send a command to server remote console |
| cmdlist | list all available console commands |
| condump | `condump "x"` write the console text to a file where `"x"` is the name of that file |
| configstrings | list the current config strings in effect |
| connect | connect to server (connect 204.52.135.50) or (connect serverURL.com) |
| crash | causes Q3TEST.EXE to perform an illegal operation in Windows |
| cvar_restart | reset all variables back to factory defaults (could be handy) |
| cvarlist | list all available console variables and their values |
| demo | play demo (`demo q3demo001.dm3`) |
| devmap | load maps in development mode? (loads map with cheats enabled) |
| dir | display directory if syntax is correct ex. `(dir \)` or `(dir ..\)` or `(dir ..\baseq3)` |
| disconnect | disconnects you from server (local included) |
| dumpuser | display user info (handicap, model/color, rail color, more…)(dumpuser "<name>") |
| echo | echo a string to the message display to your console only |
| error | execute an error routine to protect the server |
| exec | execute a config file or script |
| fdir | search directory for file filters, e.g. `fdir *q3dm?.bsp` |
| follow | switch to follow mode (`follow "<name>"`) or follow1/2 etc. |
| freeze | freeze game and all animation for specified time (e.g. `freeze 5`) |
| gfxinfo | returns extensive information about video settings |
| fs_openedList | display the file name of open pak files (pk3) |
| Fs_pureList | displays contents of the `sv_referencedPaks` variable |
| Fs_referencedList | display the contents of `sv_referencedPakNames` variable |
| give | (cheat) give player item (give railgun) |
| globalservers | list public servers on the internet |
| god | cheat – give player invulnerability |
| heartbeat | send a manual heartbeat to the master servers |
| hunk_stats | returns value of some registers: how many bits high/low and total (memory stats) |
| imagelist | list currently open images/textures used by the current map; also shows the amount of texture memory the map is using |
| in_restart | restarts all the input drivers, joystick, etc |
| -info | stop displaying server information (sv_hostname, map, rules, g_gametype, fraglimit) |
| joy_advancedupdate | removed — joy support still broken |
| kick | kick the player with the given name off the server |
| kill | kills your player (suicide) |
| killserver | stops server from running and broadcasting heartbeat |
| -left | stop turning left |
| levelshot | display the image used at the end of a level |
| loaddefered | load models and skins that have not yet been loaded |
| loaddeferred | load models and skins that have not yet been loaded (corrected spelling) |
| localservers | list servers on LAN or local subnet only |
| -lookdown | stop looking down |
| -lookup | stop looking up |
| map | loads specified map (e.g. `map q3dm7`) |
| map_restart | resets the game on the same map (also plays fight! sound file and displays FIGHT!) |
| meminfo | meminfo command replaces `hunk_stats` and `z_stats` |
| messagemode | send a message to everyone on the server |
| messagemode2 | send a message to teammates |
| messagemode3 | send a message to tourney opponents? |
| messagemode4 | send a message to attacker? (does not work) |
| midiinfo | display information about MIDI music system |
| -mlook | stop using mouse look |
| model | display the name of current player model if no parameters are given (see also model variable) |
| modelist | list of accessible screen resolutions |
| modellist | list of currently open player models |
| -movedown | stop moving down (crouch, climb down, swim down) |
| -moveleft | stop strafing to the left |
| -moveright | stop strafing to the right |
| -moveup | stop moving up (jump, climb up, swim up) |
| music | plays specified music file (e.g. `music music.wav`) |
| net_restart | reset all the network related variables like rate etc. |
| nextframe | change the animation frame of testmodel etc. (bound to keys in default config) |
| nextskin | change to next skin of testmodel etc. |
| noclip | no clipping mode — objects/walls are not solid |
| notarget | bots will not fight/see you (good for screenshots) |
| path | display all current game paths |
| ping | manually ping a server (by hostname or IP) |
| play | play a sound file (e.g. `play sound.wav`) |
| prevframe | previous frame (testmodel) |
| prevskin | previous skin (testmodel) |
| quit | quit arena and return to OS |
| rcon | start a remote console to a server |
| reconnect | reconnect to last server you were connected to |
| record | records a demo (e.g. `record mydemo.dm3`) |
| reset | reset specified variable (e.g. `reset model`) — single variable reset |
| restart | restart game on current map (server only) |
| -right | stop turning right |
| s_info | display information about sound system |
| s_list | display filenames of sound files as they play |
| s_stop | stop sound playing currently |
| s_disable_a3d | disable A3D sound system support |
| s_enable_a3d | enable A3D sound support |
| say | say message to everyone on server |
| say_team | say message only to your team |
| scanservers | scan LAN for servers |
| -scores | stop displaying current scores |
| screenshot | save current view as TARGA image |
| screenshotJPEG | save current view as JPEG image |
| sectorlist | list sectors and number of entities in each on the current map |
| serverinfo | give server information from server console |
| serverstatus | display status of connected server + client slots |
| serverrecord | record a server-side demo |
| serverstop | stop server-side demo recording |
| set | set a cvar (non-archived) |
| seta | set a cvar with archive flag (saved to config) |
| sets | set a cvar with serverinfo flag (visible to clients) |
| setu | set a cvar with userinfo flag |
| setenv | set environment variable |
| setviewpos | sets the player’s view coordinates on the map |
| shaderlist | list currently loaded shaders |
| showip | display your current IP address |
| sizedown | make viewport one size smaller |
| sizeup | make viewport one size larger |
| skinlist | list currently loaded skins |
| snd_restart | reinitialize sound system |
| soundinfo | info about sound system |
| soundlist | list sound files in use |
| spdevmap | load a devmap with bots spawned (cheats enabled) |
| -speed | stop speed toggle (reverse of +speed) |
| spmap | load a map with bots spawned in standard (no cheats) |
| startOrbit | start 3rd person display orbiting your player model |
| stats | — |
| status | status of currently connected server |
| stoprecord | stop recording demo |
| stopdemo | stop demo recording |
| stopsound | stop currently playing sound |
| -strafe | stop strafing movement |
| systeminfo | returns values for: `g_syncronousClients, sv_serverid, timescale` |
| tcmd | display current target command or code address |
| team | set player status / team / spectator etc. |
| teamtask | display/assign current team task (offense / defense / etc.) |
| teamvote | allows casting a vote on a called team-vote |
| tell | send private message to individual player |
| tell_attacker | private message to your last known attacker? |
| tell_target | private message to last target? |
| testfog | (removed / dev) for fog emulation |
| testgun | hide weapon model + model test frames/skins |
| testmodel | spawn a model in front of you for viewing/testing skins/frames |
| testshader | apply a shader to map or model for testing |
| toggle | toggle a cvar between two values (e.g. `toggle cg_autoswitch`) |
| toggleconsole | open/close the console |
| touchFile | make a zero-byte file (dev/test) |
| unbind | remove a key binding |
| unbindall | remove all key bindings |
| userinfo | list user info like via clientinfo |
| vid_restart | restart video / reinitialize graphics driver / resolution etc. |
| viewpos | returns player coordinates x y z on map |
| vminfo | display virtual machine interpreter info |
| vosay | use a predefined voice message to all |
| vosay_team | voice message to team only |
| vote | cast vote (yes/no) on a previously called vote |
| vsay | use predefined voice message to all |
| vsay_team | voice message to team only |
| vstr | execute variable’s content as console command string |
| vtaunt | voice taunt to all |
| vtell | voice taunt to a specific player |
| vtell_attacker | voice taunt to your attacker |
| vtell_target | voice taunt to your target |
| wait | insert one game tick delay in script or command chain |
| weapnext | switch to next weapon |
| weapon | select a weapon by number (e.g. `weapon "5"`) |
| weapprev | switch to previous weapon |
| writeconfig | save current configuration to file |
| z_stats | display memory stats for Z-buffer etc |




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
