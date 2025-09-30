import time


class ShutdownStrategy:
    def handle(self, server, msg):
        raise NotImplementedError


class MatchEndStrategy(ShutdownStrategy):
    def handle(self, server, msg):
        server.logger.info("ShutdownGame: Match ended completely")

        result = server.game_state_manager.handle_match_end_detected()

        if result and "actions" in result:
            server._process_match_end_actions(result["actions"])


        if result and result.get("experiment_finished"):
            server._run_async(
                server.obs_connection_manager.stop_match_recording(
                    server.game_state_manager
                )
            )
            time.sleep(3)

            server.send_command("say Experiment completed! Server shutting down in 3 seconds...")
            time.sleep(3)

            server.send_command("killserver")
            server.logger.info("Sent killserver command to stop the server")
        else:
            server.send_command("say Match completed!")



class WarmupEndStrategy(ShutdownStrategy):
    def handle(self, server, msg):
        server.logger.info("ShutdownGame: Warmup ended, match starting")

        if server._insufficient_humans:
            server.game_manager.set_next_round_with_warmup_phase()
            server.game_manager.restart_map()
            return

        result = server.game_state_manager.handle_match_start_detected()
        if result and "actions" in result:
            actions = result["actions"]
            if "start_match_recording" in actions:
                server._run_async(server.obs_connection_manager.start_match_recording(server.game_state_manager))
            if "apply_latency" in actions:
                if server.network_manager.is_enabled():
                    server.network_manager.apply_latency_rules()