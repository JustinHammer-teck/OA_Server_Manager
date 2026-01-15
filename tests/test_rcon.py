#!/usr/bin/env python
"""Test script for Dota 2 RCON connection."""

import asyncio
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import core.utils.settings as settings
from core.adapters.dota2.rcon_client import SourceRCONClient, RCONError


async def test_rcon_connection():
    """Test RCON connection to Dota 2 server."""
    host = settings.dota2_rcon_host
    port = settings.dota2_rcon_port
    password = settings.dota2_rcon_password

    print("=" * 60)
    print("Dota 2 RCON Connection Test")
    print("=" * 60)
    print(f"Host:     {host}")
    print(f"Port:     {port}")
    print(f"Password: {'*' * len(password) if password else '(empty)'}")
    print("=" * 60)

    rcon = SourceRCONClient(host=host, port=port, password=password, timeout=10.0)

    try:
        print("\n[1/3] Connecting to server...")
        await rcon.connect()
        print("  ✓ Connected and authenticated successfully!")

        print("\n[2/3] Sending 'status' command...")
        response = await rcon.execute("status")
        print("  ✓ Command executed successfully!")
        print("\n--- Status Response ---")
        print(response[:1000] if len(response) > 1000 else response)
        print("-" * 40)

        print("\n[3/3] Sending 'echo RCON_TEST' command...")
        response = await rcon.execute("echo RCON_TEST")
        print(f"  ✓ Response: {response.strip() or '(empty)'}")

        print("\n" + "=" * 60)
        print("✓ All tests passed! RCON connection is working.")
        print("=" * 60)

    except RCONError as e:
        print(f"\n✗ RCON Error: {e}")
        print("\nPossible causes:")
        print("  - Server not running or not reachable")
        print("  - Wrong host/port")
        print("  - Wrong RCON password")
        print("  - RCON not enabled on server (need -rcon_password launch param)")
        return False

    except asyncio.TimeoutError:
        print("\n✗ Connection timed out")
        print("\nPossible causes:")
        print("  - Server not reachable (firewall, network)")
        print("  - Wrong port")
        return False

    except Exception as e:
        print(f"\n✗ Unexpected error: {type(e).__name__}: {e}")
        return False

    finally:
        await rcon.disconnect()
        print("\nConnection closed.")

    return True


if __name__ == "__main__":
    success = asyncio.run(test_rcon_connection())
    sys.exit(0 if success else 1)
