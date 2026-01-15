"""
Integration test for sending RCON commands via AMP API.

This test connects to a real AMP instance and tests command execution.

Usage:
    uv run pytest tests/test_amp_rcon_command.py -v

Environment variables (required):
    AMP_URL         - AMP panel URL (e.g., https://your-amp-panel.com)
    AMP_USERNAME    - AMP username
    AMP_PASSWORD    - AMP password
    AMP_INSTANCE_ID - Instance ID to connect to
"""

import asyncio
import os
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.adapters.amp.amp_api_client import AMPAPIClient, AMPAPIError


# Get credentials from environment
AMP_URL = os.environ.get("AMP_URL", "")
AMP_USERNAME = os.environ.get("AMP_USERNAME", "")
AMP_PASSWORD = os.environ.get("AMP_PASSWORD", "")
AMP_INSTANCE_ID = os.environ.get("AMP_INSTANCE_ID", "")


def requires_amp_credentials():
    """Skip test if AMP credentials are not configured."""
    return pytest.mark.skipif(
        not all([AMP_URL, AMP_USERNAME, AMP_PASSWORD, AMP_INSTANCE_ID]),
        reason="AMP credentials not configured (set AMP_URL, AMP_USERNAME, AMP_PASSWORD, AMP_INSTANCE_ID)",
    )


@pytest.fixture
async def amp_client():
    """Create and authenticate an AMP API client."""
    client = AMPAPIClient(
        base_url=AMP_URL,
        username=AMP_USERNAME,
        password=AMP_PASSWORD,
        instance_id=AMP_INSTANCE_ID,
    )

    try:
        await client.login()
        yield client
    finally:
        await client.close()


@requires_amp_credentials()
@pytest.mark.asyncio
async def test_send_status_command(amp_client):
    """Test sending 'status' command to AMP server."""
    result = await amp_client.send_console_message("status")
    assert result is True
    print("Successfully sent 'status' command")


@requires_amp_credentials()
@pytest.mark.asyncio
async def test_send_command_and_get_response(amp_client):
    """Test sending command and checking for console response."""
    # Send a command
    await amp_client.send_console_message("status")

    # Wait briefly for the command to process
    await asyncio.sleep(2)

    # Get updates to see if we got a response
    updates = await amp_client.get_updates()

    print(f"Received {len(updates.console_entries)} console entries")
    for entry in updates.console_entries:
        print(f"  [{entry.timestamp}] {entry.source}: {entry.contents[:80]}")

    # We should have some response
    # Note: depending on server state, we may or may not get entries
    assert updates is not None


@requires_amp_credentials()
@pytest.mark.asyncio
async def test_send_custom_command(amp_client):
    """Test sending a custom RCON command."""
    # This test allows testing any command - modify as needed
    test_command = os.environ.get("AMP_TEST_COMMAND", "status")

    result = await amp_client.send_console_message(test_command)
    assert result is True
    print(f"Successfully sent command: {test_command}")

    # Wait and check response
    await asyncio.sleep(2)
    updates = await amp_client.get_updates()
    print(f"Got {len(updates.console_entries)} console entries after command")


@requires_amp_credentials()
@pytest.mark.asyncio
async def test_connection_and_authentication():
    """Test that we can connect and authenticate to AMP."""
    client = AMPAPIClient(
        base_url=AMP_URL,
        username=AMP_USERNAME,
        password=AMP_PASSWORD,
        instance_id=AMP_INSTANCE_ID,
    )

    try:
        success = await client.login()
        assert success is True
        assert client.is_authenticated
        print(f"ADS Session: {client._session_id[:20] if client._session_id else 'None'}...")
        print(f"Instance Session: {client._instance_session_id[:20] if client._instance_session_id else 'None'}...")
    finally:
        await client.close()


@requires_amp_credentials()
@pytest.mark.asyncio
async def test_get_server_status(amp_client):
    """Test getting server status before sending commands."""
    status = await amp_client.get_status()

    print(f"Server status: {status}")

    # Status should contain some expected fields
    assert status is not None
    if "State" in status:
        print(f"Server state: {status['State']}")


if __name__ == "__main__":
    # Allow running directly for quick testing
    async def main():
        if not all([AMP_URL, AMP_USERNAME, AMP_PASSWORD, AMP_INSTANCE_ID]):
            print("Error: Set environment variables:")
            print("  AMP_URL, AMP_USERNAME, AMP_PASSWORD, AMP_INSTANCE_ID")
            return

        print(f"Connecting to {AMP_URL} (instance: {AMP_INSTANCE_ID})")

        client = AMPAPIClient(
            base_url=AMP_URL,
            username=AMP_USERNAME,
            password=AMP_PASSWORD,
            instance_id=AMP_INSTANCE_ID,
        )

        try:
            print("Logging in...")
            await client.login()
            print(f"Authenticated: {client.is_authenticated}")

            print("\nGetting server status...")
            status = await client.get_status()
            print(f"Status: {status.get('State', 'Unknown')}")

            print("\nSending 'status' command...")
            result = await client.send_console_message("status")
            print(f"Command sent: {result}")

            print("\nWaiting for response...")
            await asyncio.sleep(2)

            updates = await client.get_updates()
            print(f"Console entries: {len(updates.console_entries)}")
            for entry in updates.console_entries[-5:]:
                print(f"  {entry.contents[:100]}")

        except AMPAPIError as e:
            print(f"Error: {e}")
        finally:
            await client.close()
            print("\nDone.")

    asyncio.run(main())
