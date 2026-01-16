class ShutdownStrategy:
    def handle(self, server, msg):
        raise NotImplementedError


class MatchShutdownStrategy(ShutdownStrategy):
    def handle(self, server, msg):
        server.logger.info("ShutdownGame: Match ended completely")

        server.run_async(
            server.obs_connection_manager.stop_match_recording(
                server.game_state_manager
            )
        )

        result = server.game_state_manager.handle_match_shutdown_detected()

        if result and "actions" in result:
            self._process_match_shutdown_actions(server, result["actions"])

        if result and result.get("experiment_finished"):
            server.send_command("killserver")
            server.logger.info("Sent killserver command to stop the server")
        else:
            server.send_command("say Match completed!")

        server.game_state_manager.reset_to_waiting()

    @staticmethod
    def _process_match_shutdown_actions(server, actions):
        if "rotate_latency" in actions:
            server.network_manager.rotate_latencies()


class WarmupShutdownStrategy(ShutdownStrategy):
    def handle(self, server, msg):
        server.logger.info("ShutdownGame: Warmup ended, match starting")

        if server.insufficient_humans:
            server.game_manager.set_next_round_with_warmup_phase()
            return

        result = server.game_state_manager.handle_match_start_detected()
        if result and "actions" in result:
            actions = result["actions"]
            if "start_match_recording" in actions:
                server.run_async(
                    server.obs_connection_manager.start_match_recording(
                        server.game_state_manager
                    )
                )
            if "apply_latency" in actions:
                if server.network_manager.is_enabled():
                    server.network_manager.apply_latency_rules()

        server.game_state_manager.reset_to_waiting()
