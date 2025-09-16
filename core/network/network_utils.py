import os


class NetworkUtils:
    """
    apply different latencies to each client ip using tc and nftables.

    args:
        ip_latency_map (dict): a dictionary mapping ips to their latency values (in ms).
        interface (str): the network interface to configure (e.g., "enp1s0").
    """

    @staticmethod
    def apply_latency_rules(ip_latency_map, interface):
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

    @staticmethod
    def dispose(interface):
        os.system(
            f"/usr/bin/sudo /sbin/tc qdisc replace dev {interface} root pfifo_fast"
        )
