# OthelloBot - AI Othello Players

A comprehensive collection of AI players for the game of Othello (Reversi), featuring reinforcement learning, traditional game algorithms, and engine-based approaches.

## Project Overview

This project implements various AI strategies for playing Othello:

- **RandomPlayer**: Baseline player that makes random legal moves
- **ab_ScoreSearch**: Alpha-beta pruning with position evaluation
- **HandMade**: Position-based evaluation with strategic weights
- **Enhanced Game Engine**: Robust game implementation with error handling

## Quick Start

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Basic Usage

```python
from Othello.othello import OthelloEnv
from Othello.players import RandomPlayer, ab_ScoreSearch
from Othello.play_othello import play_game

# Create a game and players
game = OthelloEnv()
player1 = ab_ScoreSearch(game)
player2 = RandomPlayer(game)

# Play a game
score, moves = play_game(game, player1, player2)
print(f"Final score: {score}")
print(f"Total moves: {len(moves)}")
```

### Running Tournaments

```python
from Othello.tournament import run_tournament, print_tournament_results
from Othello.players import ab_ScoreSearch, RandomPlayer

# Run a tournament
results = run_tournament(ab_ScoreSearch, RandomPlayer, num_games=100)
print_tournament_results(results)
```

## Project Structure

```
OthelloBot/
├── Othello/                    # Main game package
│   ├── othello.py             # Core game engine
│   ├── othello_enhanced.py    # Enhanced game with error handling
│   ├── players.py             # AI player implementations
│   ├── play_othello.py        # Game orchestration
│   ├── tournament.py          # Tournament management
│   ├── render.py              # Game visualization
│   └── game_viewer.py         # Game replay functionality
├── tests/                     # Test suite
│   ├── test_othello_game.py   # Game logic tests
│   ├── test_players.py        # Player behavior tests
│   └── test_game_flow.py      # Integration tests
├── Othello_C/                 # C++ implementation (experimental)
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

## Game Rules

Othello is played on an 8x8 board with two players (Black and White):

1. **Initial Setup**: 4 pieces in the center (2 black, 2 white in alternating pattern)
2. **Gameplay**: Players alternate turns placing pieces
3. **Capturing**: A move must flank opponent pieces, which then flip to your color
4. **Legal Moves**: You must make a capturing move if possible, otherwise pass
5. **Game End**: When neither player can move or board is full
6. **Winner**: Player with the most pieces wins

## AI Players

### RandomPlayer
- **Strategy**: Random selection from legal moves, baseline for comparison/testing

### ab_ScoreSearch
- **Strategy**: Alpha-beta pruning for current piece count (known to be sub-optimal)

### HandMade (WIP)
- **Strategy**: Position-based evaluation with strategic weights


## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Or run individual test files
python tests/test_othello_game.py
python tests/test_players.py
python tests/test_game_flow.py
```

### Test Coverage

- Game initialization and reset
- Legal move detection
- Move execution and piece flipping  
- Game termination conditions
- Player decision making
- Tournament management
- Edge cases and error handling

## Future Improvements

- Machine learning players (neural networks)
- Monte Carlo Tree Search implementation
- Opening book and endgame databases
- GUI interface for human play
- Multi-threaded tournament evaluation
- Advanced position evaluation functions
- Rating system for tournaments to estimate player strength relative to each other (Elo ratings, TrueSkill)