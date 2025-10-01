"""
Othello Game Package

This package provides a complete implementation of the Othello (Reversi) game
with various AI players and tournament functionality.

Main Components:
    - OthelloEnv: Core game engine
    - Various AI players (RandomPlayer, ab_ScoreSearch, HandMade)
    - Tournament management system
    - Comprehensive test suite
"""

from .othello import OthelloEnv
from .players import RandomPlayer, ab_ScoreSearch, HandMade
from .play_othello import play_game
from .tournament import run_tournament, print_tournament_results

__version__ = "1.0.0"
__all__ = [
    "OthelloEnv",
    "RandomPlayer", 
    "ab_ScoreSearch",
    "HandMade",
    "play_game",
    "run_tournament",
    "print_tournament_results"
]