#!/usr/bin/env python3

import argparse
import errno
import os
import random
import re
import signal
import sys
import time
from datetime import datetime
from enum import Enum
from subprocess import PIPE, Popen

# Specify the desired egress (downstream) bandwidth in Mb/s
# BANDWIDTH = 100

nplayers_threshold = 2  # Changed to match the non-Andrew script
timelimit = 2
warmup_timelimit = 5  # Added from original script
repeats = 1

# Bot configuration
bot_count = 4  # Default number of bots to add
# Default bot difficulty: 3 = Hard
bot_difficulty = 1  # Single difficulty level for all bots
# Valid OpenArena bot names
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

# Network latency settings - matching original script
latencies = [200]  # Changed to match the original script
random.shuffle(latencies)
print("Initial latencies (shuffled): ", latencies)

max_rounds = len(latencies) * repeats

parser = argparse.ArgumentParser(
    "Start openarena server, wait for clients to connect, start experiment sequence, and upload results"
)


def ranged_type(value_type, min_value, max_value):
    def range_checker(arg: str):
        try:
            f = value_type(arg)
        except ValueError:
            raise argparse.ArgumentTypeError(f"must be a valid {value_type}")

        if f < min_value or f > max_value:
            raise argparse.ArgumentTypeError(
                f"must be within range [{min_value}, {max_value}]"
            )

        return f

    # Return function handle to checking function
    return range_checker


parser.add_argument("--interface", default="enp1s0")
parser.add_argument(
    "--bots",
    default=bot_count,
    type=ranged_type(int, 0, 10),
    help="Number of bots to add (0-10 inclusive)",
)
parser.add_argument(
    "--difficulty",
    default=bot_difficulty,
    type=ranged_type(int, 1, 5),
    help="Difficulty level for all bots (1-5): 1=Rookie, 2=Average, 3=Hard, 4=Very Hard, 5=Godlike",
)
args = parser.parse_args()


def apply_latency_rules(ip_latency_map, interface):
    """
    apply different latencies to each client ip using tc and nftables.

    args:
        ip_latency_map (dict): a dictionary mapping ips to their latency values (in ms).
        interface (str): the network interface to configure (e.g., "enp1s0").
    """
    # clear existing tc rules
    print("clearing existing tc rules...")
    os.system(f"/usr/bin/sudo /sbin/tc qdisc del dev {interface} root || true")

    # create nftables table if it doesn't exist
    print("setting up nftables...")
    os.system("/usr/bin/sudo nft add table ip netem || true")
    os.system(
        "/usr/bin/sudo nft add chain ip netem output '{ type filter hook output priority 0; }' || true"
    )

    # set up htb qdisc
    print("setting up htb qdisc...")
    os.system(
        f"/usr/bin/sudo /sbin/tc qdisc add dev {interface} root handle 1: htb default 1"
    )

    for i, (ip, latency) in enumerate(ip_latency_map.items(), start=1):
        class_id = f"1:{i + 10}"
        mark_id = i * 100  # unique mark per ip

        print(f"applying {latency}ms latency to {ip}...")

        # create a class under htb
        os.system(
            f"/usr/bin/sudo /sbin/tc class add dev {interface} parent 1: classid {class_id} htb rate 1000mbit"
        )

        # apply netem to this class
        os.system(
            f"/usr/bin/sudo /sbin/tc qdisc add dev {interface} parent {class_id} handle {i + 10}: netem delay {latency}ms"
        )

        # use tc filter to assign marked packets to the correct class
        os.system(
            f"/usr/bin/sudo /sbin/tc filter add dev {interface} protocol ip parent 1: prio 1 handle {mark_id} fw classid {class_id}"
        )

        # use nftables to mark packets based on destination ip
        os.system(
            f"/usr/bin/sudo nft add rule ip netem output ip daddr {ip} meta mark set {mark_id}"
        )

    print("latency rules applied successfully.")


def add_bots(server, num_bots, difficulty, bot_names):
    """
    Add bots to the server with the same difficulty level.

    Args:
        server: The server process to send commands to
        num_bots: Number of bots to add
        difficulty: Single difficulty level for all bots (1-5)
        bot_names: List of valid bot names
    """
    print(f"Adding {num_bots} bots to the server with difficulty {difficulty}...")

    # Make sure there are enough names
    while len(bot_names) < num_bots:
        bot_names.extend(bot_names)
    bot_names = bot_names[:num_bots]

    # Add each bot with the same difficulty
    for i in range(num_bots):
        name = bot_names[i]

        print(f"Adding bot {name} with difficulty {difficulty}")
        # Format: "addbot [name] [difficulty]"
        server.stdin.write(f"addbot {name} {difficulty}\r\n".encode())
        server.stdin.flush()
        time.sleep(1)  # Small delay between adding bots

    print("All bots added successfully")


# Handle Ctrl-C interrupt signal
def signal_handler(sig, frame):
    print("Interrupted; cleaning up", file=sys.stderr)
    os.system(
        f"/usr/bin/sudo /sbin/tc qdisc replace dev {args.interface} root pfifo_fast"
    )
    sys.exit(0)


# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

timestamp = datetime.now().strftime("%Y%m%d_%H.%M")
filename = "openarena_%s.log" % timestamp

print("Opening %s for writing" % filename, file=sys.stderr)

# Open output log file
try:
    log = open(filename, "w")
except:
    print(
        'Error: unable to open output file "%s" for writing: %s'
        % (filename, os.strerror(errno)),
        file=sys.stderr,
    )
    sys.exit(-2)

print("Reading server output; conditions set to nominal", file=sys.stderr)

# Open pipe to ioquake3:
server = Popen(
    [
        "oa_ded",
        "+set",
        "dedicated",
        "1",
        "+set",
        "net_port",
        "27960",
        "+set",
        "com_legacyprotocol",
        "71",
        "+set",
        "com_protocol",
        "71",
        "+set",
        "sv_master1",
        "dpmaster.deathmask.net",
        "+set",
        "cl_motd",
        "0",
        "+set",
        "com_homepath",
        "server.oa",
        "+exec",
        "andrew_server.cfg",
    ],
    stdout=PIPE,
    stdin=PIPE,
    stderr=PIPE,
    universal_newlines=False,
)

# Keep going forever
i = 0
nplayers = 0

player_list = []
ip_latency_map = {}

print("Setting maximum number of clients to %i" % (nplayers_threshold + args.bots))
server.stdin.write(f"set sv_maxclients {nplayers_threshold + args.bots}\r\n".encode())
server.stdin.flush()

# Make sure bots are enabled
server.stdin.write(b"set bot_enable 1\r\n")
server.stdin.flush()
server.stdin.write(b"set bot_nochat 1\r\n")
server.stdin.flush()
server.stdin.write(b"set bot_minplayers 0\r\n")
server.stdin.flush()


# State definitions:
# WAITING: players are joining. While we have fewer than nplayers_threshold, let them run around and play with no time/frag limit. No latency added.
# When we reach nplayers_threshold, go to next map, set timelimit to 5 minutes and transition to WARMUP.
# WARMUP: no latency applied, 5 minutes running around. At the next map rollover, switch to RUNNING
# RUNNING: the experiment has started; apply latency and off we go!
class state(Enum):
    WAITING = 1
    WARMUP = 2
    RUNNING = 3


STATE = state.WAITING

k = 0
bots_added = False

while True:
    t = time.time()
    msgFromServer = server.stderr.readline().decode("utf-8", errors="replace").rstrip()
    print("%f: %s" % (t, msgFromServer), file=log)
    log.flush()

    m = re.match(
        "^Client ([0-9]+) connecting with ([0-9]+) challenge ping$", msgFromServer
    )

    # If a new player has connected...
    if m:
        print(
            "Client %i has connected with %i challenge ping."
            % (int(m.group(1)), int(m.group(2))),
            file=sys.stderr,
        )
        infotext = server.stderr.readline().decode("utf-8", errors="replace")
        print("Returned info of length %i" % len(infotext))

        # If someone has tried to connect, but the server is full...
        if len(infotext) < 100:
            continue

        # Switch to parsing server output like the original script
        server.stdin.write(b"status\r\n")
        server.stdin.flush()

        line_n = 0

        while True:
            msgFromServer = (
                server.stderr.readline().decode("utf-8", errors="replace").rstrip()
            )

            if len(msgFromServer) == 0:
                break

            if line_n > 4:  # Skip the header lines
                ip = msgFromServer.split()[4]
                if "^7" in ip:  # Check if IP format matches first script
                    ip = ip.split("^7")[1]
                print(f"Client IP address: {ip}")
                if ip not in ip_latency_map:  # Avoid duplicate entries
                    ip_latency_map[ip] = latencies[len(ip_latency_map) % len(latencies)]

            line_n = line_n + 1

        nplayers = len(ip_latency_map)
        print(f"{nplayers} players in the game")

        # Have we reached the threshold? If so, start the experiment map cycle
        if STATE == state.WAITING:
            if nplayers >= nplayers_threshold:
                t = time.time()

                print("Full list of players:", file=sys.stderr)
                print("%f: Full list of players:" % t, file=log, end="")

                for ip in ip_latency_map.keys():
                    print(f"\tPlayer {ip}", file=sys.stderr)
                    print(f" {ip}", file=log, end="")

                print("", file=log)

                # Add bots if they haven't been added yet
                if not bots_added and args.bots > 0:
                    print("Adding bots before starting warmup...")
                    add_bots(server, args.bots, args.difficulty, bot_names)
                    bots_added = True
                    time.sleep(2)  # Give time for bots to join

                server.stdin.write(b"vstr m0\r\n")
                server.stdin.flush()

                server.stdin.write(f"timelimit {warmup_timelimit}\r\n".encode())
                server.stdin.flush()

                server.stdin.write(
                    f"say Starting warmup round: {warmup_timelimit} minutes!\r\n".encode()
                )
                server.stdin.flush()

                STATE = state.WARMUP
                print("State changed from WAITING to WARMUP")
            else:
                server.stdin.write(
                    f"say WAITING ROOM: {nplayers}/{nplayers_threshold} players connected\r\n".encode()
                )
                server.stdin.flush()

    # If we have just started a new level (this gets printed just before it starts)
    # AND we now have enough players (theoretically this is the only way this can have happened
    # other than an rcon)...

    m = re.match("^AAS initialized.$", msgFromServer)

    if nplayers >= nplayers_threshold and m:
        if STATE == state.RUNNING:
            t = time.time()

            if i == max_rounds + 1:
                print("Final round %i completed." % (i - 1), file=sys.stderr)
                print("%f: Final round %i completed." % (t, i - 1), file=log)
                log.flush
                break

            if i == 0:
                print(
                    "Warmup round complete: applying initial network conditions.",
                    file=sys.stderr,
                )
                print(
                    "%f: Warmup round complete: applying initial network conditions."
                    % t,
                    file=log,
                )
            else:
                print(
                    "Round %i complete: changing network conditions." % i,
                    file=sys.stderr,
                )
                print(
                    "%f: Round %i complete: changing network conditions." % (t, i),
                    file=log,
                )
                # Rotate latencies like in the original script
                latencies = latencies[1:] + latencies[:1]
                print("Rotated latencies:", latencies)

            log.flush()

            n = 0
            # Update latency mapping for each IP
            for ip in ip_latency_map.keys():
                ip_latency_map[ip] = latencies[n % len(latencies)]
                n += 1

            print("Latency map:")
            print("\t", ip_latency_map)
            print("%f: Latency map: " % t, ip_latency_map, file=log)
            log.flush()

            apply_latency_rules(ip_latency_map, args.interface)

            i = i + 1

        elif STATE == state.WARMUP:
            if k == 1:
                STATE = state.RUNNING
                print("State changed from WARMUP to RUNNING")

                # Set timelimit for actual gameplay rounds
                print("Setting timelimit to %i minutes" % timelimit)
                server.stdin.write(f"set timelimit {timelimit}\r\n".encode())
                server.stdin.flush()

                # Apply initial latency
                apply_latency_rules(ip_latency_map, args.interface)
            else:
                k = k + 1

# Handle the case where a player has disconnected
m = re.match("^ClientDisconnect: ([0-9]+)$", msgFromServer)
if m:
    client_id = int(m.group(1))
    print(f"Client {client_id} has disconnected. Updating player list.")
    # Would need to map client ID back to IP and update ip_latency_map
    # This would require tracking client IDs in the player info
