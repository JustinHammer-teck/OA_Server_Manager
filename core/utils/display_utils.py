"""Display utilities for formatted console output."""

import logging
from typing import List, Dict, Any
from tabulate import tabulate


class DisplayUtils:
    """Utility class for formatted display output."""
    
    @staticmethod
    def display_client_table(client_manager, title: str = "CLIENT INFORMATION") -> None:
        """
        Display formatted client information table.
        
        Args:
            client_manager: ClientManager instance with client data
            title: Title for the table display
        """
        logger = logging.getLogger(__name__)
        
        # Get table data from client manager
        table_data = client_manager.get_client_info_table()
        
        if not table_data:
            logger.info("No clients connected")
            return
        
        # Define headers
        headers = ["Client ID", "IP Address", "Type", "Latency", "OBS Status", "Name"]
        
        # Create formatted output
        print("\n" + "=" * 80)
        print(f"{title:^80}")
        print("=" * 80)
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("=" * 80)
        
        # Log summary
        human_count = client_manager.get_human_count()
        bot_count = client_manager.get_bot_count()
        logger.info(f"Total clients: {human_count} humans, {bot_count} bots")
    
    @staticmethod
    def display_obs_connection_results(connection_results: Dict[str, bool],
                                        title: str = "OBS CONNECTION RESULTS") -> None:
        """
        Display OBS connection results in a formatted table.
        
        Args:
            connection_results: Dictionary mapping IP to connection success
            title: Title for the table display
        """
        logger = logging.getLogger(__name__)
        
        if not connection_results:
            logger.info("No OBS connections attempted")
            return
        
        # Prepare table data
        table_data = []
        for ip, connected in connection_results.items():
            status = "✓ Connected" if connected else "✗ Failed"
            action = "Ready" if connected else "Will be kicked"
            table_data.append([ip, status, action])
        
        # Define headers
        headers = ["Client IP", "OBS Connection", "Action"]
        
        # Create formatted output
        print("\n" + "=" * 60)
        print(f"{title:^60}")
        print("=" * 60)
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("=" * 60)
        
        # Log summary
        connected_count = sum(1 for connected in connection_results.values() if connected)
        total_count = len(connection_results)
        logger.info(f"OBS connections: {connected_count}/{total_count} successful")

    @staticmethod
    def display_match_start(round_num: int, max_rounds: int) -> None:
        """
        Display match start information.
        
        Args:
            round_num: Current round number
            max_rounds: Total number of rounds
        """
        print("\n" + "╔" + "═" * 48 + "╗")
        print(f"║{'MATCH STARTING':^48}║")
        print(f"║{'Round ' + str(round_num) + '/' + str(max_rounds):^48}║")
        print("╚" + "═" * 48 + "╝")
    
    @staticmethod
    def display_match_end(round_num: int, max_rounds: int) -> None:
        """
        Display match end information.
        
        Args:
            round_num: Current round number
            max_rounds: Total number of rounds
        """
        print("\n" + "╔" + "═" * 48 + "╗")
        print(f"║{'MATCH COMPLETED':^48}║")
        print(f"║{'Round ' + str(round_num) + '/' + str(max_rounds) + ' finished':^48}║")
        print("╚" + "═" * 48 + "╝")
    
    @staticmethod
    def display_warmup_status(human_count: int, threshold: int, obs_connecting: bool = False) -> None:
        """
        Display warmup phase status.
        
        Args:
            human_count: Current number of human players
            threshold: Required threshold
            obs_connecting: Whether OBS connections are in progress
        """
        print("\n" + "┌" + "─" * 48 + "┐")
        print(f"│{'WARMUP PHASE':^48}│")
        print(f"│{'Human players: ' + str(human_count) + '/' + str(threshold):^48}│")
        if obs_connecting:
            print(f"│{'Connecting to OBS instances...':^48}│")
        print("└" + "─" * 48 + "┘")