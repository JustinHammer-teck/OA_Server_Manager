"""Tests for unified sync/async command pattern.

This module tests the consolidation of send_command_sync() into the base
GameAdapter class, ensuring all adapters inherit the same implementation
rather than duplicating code.

TDD Phase: RED - These tests define the expected behavior.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch


class TestBaseAdapterSyncCommand:
    """Test base adapter send_command_sync implementation."""

    def test_base_adapter_has_send_command_sync(self):
        """Base GameAdapter should have send_command_sync method."""
        from core.adapters.base import GameAdapter

        assert hasattr(GameAdapter, "send_command_sync")

    def test_send_command_sync_is_concrete_not_abstract(self):
        """send_command_sync should be a concrete implementation, not abstract."""
        from core.adapters.base import GameAdapter

        # Check that it's not an abstract method
        method = getattr(GameAdapter, "send_command_sync", None)
        assert method is not None
        assert not getattr(method, "__isabstractmethod__", False)

    def test_send_command_sync_signature(self):
        """send_command_sync should accept command string and return None."""
        from core.adapters.base import GameAdapter
        import inspect

        sig = inspect.signature(GameAdapter.send_command_sync)
        params = list(sig.parameters.keys())

        # Should have self and command parameters
        assert "self" in params
        assert "command" in params


class TestSendCommandSyncEventLoopHandling:
    """Test event loop handling in send_command_sync."""

    def test_sync_calls_async_when_no_loop_running(self):
        """send_command_sync should call async send_command when no loop running."""
        from core.adapters.openarena.adapter import OAGameAdapter
        from core.adapters.base import GameAdapterConfig

        config = GameAdapterConfig(
            game_type="openarena",
            binary_path="/fake/path",
        )
        adapter = OAGameAdapter(config)
        adapter.send_command = AsyncMock()

        # Patch asyncio to simulate no running loop
        with patch("asyncio.get_event_loop") as mock_get_loop:
            mock_loop = MagicMock()
            mock_loop.is_running.return_value = False
            mock_get_loop.return_value = mock_loop

            adapter.send_command_sync("test command")

            # Should have called run_until_complete
            mock_loop.run_until_complete.assert_called_once()

    def test_sync_creates_task_when_loop_running(self):
        """send_command_sync should create task when loop already running."""
        from core.adapters.dota2.adapter import Dota2GameAdapter
        from core.adapters.base import GameAdapterConfig

        config = GameAdapterConfig(
            game_type="dota2",
            host="localhost",
            port=27015,
            password="test",
        )
        adapter = Dota2GameAdapter(config)
        adapter.send_command = AsyncMock()

        with patch("asyncio.get_event_loop") as mock_get_loop:
            mock_loop = MagicMock()
            mock_loop.is_running.return_value = True
            mock_get_loop.return_value = mock_loop

            with patch("asyncio.create_task") as mock_create_task:
                adapter.send_command_sync("status")
                mock_create_task.assert_called_once()

    def test_sync_handles_runtime_error(self):
        """send_command_sync should handle RuntimeError (no event loop)."""
        from core.adapters.amp.adapter import AMPGameAdapter
        from core.adapters.base import GameAdapterConfig

        config = GameAdapterConfig(
            game_type="amp",
            host="http://localhost:8080",
            password="admin:password",
        )
        adapter = AMPGameAdapter(config)
        adapter.send_command = AsyncMock()

        with patch("asyncio.get_event_loop") as mock_get_loop:
            mock_get_loop.side_effect = RuntimeError("No event loop")

            with patch("asyncio.run") as mock_run:
                adapter.send_command_sync("test")
                mock_run.assert_called_once()


class TestAdaptersDontDuplicateSyncCommand:
    """Test that adapters don't override send_command_sync unnecessarily."""

    def test_oa_adapter_uses_base_implementation(self):
        """OAGameAdapter should inherit send_command_sync from base."""
        from core.adapters.openarena.adapter import OAGameAdapter
        from core.adapters.base import GameAdapter

        # The method should be inherited, not overridden
        assert OAGameAdapter.send_command_sync is GameAdapter.send_command_sync

    def test_dota2_adapter_uses_base_implementation(self):
        """Dota2GameAdapter should inherit send_command_sync from base."""
        from core.adapters.dota2.adapter import Dota2GameAdapter
        from core.adapters.base import GameAdapter

        assert Dota2GameAdapter.send_command_sync is GameAdapter.send_command_sync

    def test_amp_adapter_uses_base_implementation(self):
        """AMPGameAdapter should inherit send_command_sync from base."""
        from core.adapters.amp.adapter import AMPGameAdapter
        from core.adapters.base import GameAdapter

        assert AMPGameAdapter.send_command_sync is GameAdapter.send_command_sync


class TestSendCommandSyncIntegration:
    """Integration tests for send_command_sync behavior."""

    def test_oa_adapter_sync_command_delegates_to_async(self):
        """OAGameAdapter sync command should delegate to async send_command."""
        from core.adapters.openarena.adapter import OAGameAdapter
        from core.adapters.base import GameAdapterConfig

        config = GameAdapterConfig(
            game_type="openarena",
            binary_path="/fake/path",
        )
        adapter = OAGameAdapter(config)

        # Create a mock for the async method
        send_command_mock = AsyncMock(return_value=None)
        adapter.send_command = send_command_mock

        # Run sync command with a controlled event loop
        with patch("asyncio.get_event_loop") as mock_get_loop:
            mock_loop = MagicMock()
            mock_loop.is_running.return_value = False

            # Capture the coroutine passed to run_until_complete
            captured_coro = None

            def capture_coro(coro):
                nonlocal captured_coro
                captured_coro = coro
                # Actually run it to verify it calls send_command
                return (
                    asyncio.get_event_loop_policy()
                    .new_event_loop()
                    .run_until_complete(coro)
                )

            mock_loop.run_until_complete = capture_coro
            mock_get_loop.return_value = mock_loop

            adapter.send_command_sync("test command")

            # Verify send_command was called with the right argument
            send_command_mock.assert_awaited_once_with("test command")

    def test_all_adapters_have_consistent_sync_behavior(self):
        """All adapters should have the same send_command_sync behavior."""
        from core.adapters.openarena.adapter import OAGameAdapter
        from core.adapters.dota2.adapter import Dota2GameAdapter
        from core.adapters.amp.adapter import AMPGameAdapter
        from core.adapters.base import GameAdapterConfig

        # Create all adapter types
        oa_config = GameAdapterConfig(game_type="openarena", binary_path="/fake")
        dota_config = GameAdapterConfig(
            game_type="dota2", host="localhost", port=27015, password="test"
        )
        amp_config = GameAdapterConfig(
            game_type="amp", host="http://localhost:8080", password="admin:pass"
        )

        oa_adapter = OAGameAdapter(oa_config)
        dota_adapter = Dota2GameAdapter(dota_config)
        amp_adapter = AMPGameAdapter(amp_config)

        # All should use the same method implementation
        assert (
            type(oa_adapter).send_command_sync is type(dota_adapter).send_command_sync
        )
        assert (
            type(dota_adapter).send_command_sync is type(amp_adapter).send_command_sync
        )


class TestSendCommandSyncReturnType:
    """Test that send_command_sync returns None."""

    def test_sync_command_returns_none(self):
        """send_command_sync should return None (fire-and-forget)."""
        from core.adapters.openarena.adapter import OAGameAdapter
        from core.adapters.base import GameAdapterConfig

        config = GameAdapterConfig(
            game_type="openarena",
            binary_path="/fake/path",
        )
        adapter = OAGameAdapter(config)
        adapter.send_command = AsyncMock(return_value="response")

        with patch("asyncio.get_event_loop") as mock_get_loop:
            mock_loop = MagicMock()
            mock_loop.is_running.return_value = False
            mock_loop.run_until_complete.return_value = "response"
            mock_get_loop.return_value = mock_loop

            result = adapter.send_command_sync("test")

            # send_command_sync should return None even if async returns value
            assert result is None
