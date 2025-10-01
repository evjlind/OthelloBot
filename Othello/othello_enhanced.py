"""
Enhanced Othello Game Implementation

This module provides a robust implementation of the Othello (Reversi) game with
comprehensive error handling, input validation, and documentation.

Classes:
    OthelloEnvEnhanced: Enhanced Othello game environment with better error handling
    
Constants:
    BOARD_SIZE: Size of the Othello board (8x8)
    EMPTY, BLACK, WHITE: Piece values for board representation
"""

import numpy as np
from typing import Tuple, List, Optional, Union

# Game constants
BOARD_SIZE = 8
EMPTY = 0
BLACK = 1
WHITE = -1

class InvalidMoveError(Exception):
    """Raised when an invalid move is attempted."""
    pass

class GameOverError(Exception):
    """Raised when attempting to make moves on a completed game."""
    pass

class OthelloEnvEnhanced:
    """
    Enhanced Othello game environment with comprehensive error handling.
    
    This class represents a complete Othello game with proper input validation,
    error handling, and comprehensive game state management.
    
    Attributes:
        board (np.ndarray): 8x8 board representing game state
        num_moves (int): Total number of moves made in the game
        game_over (bool): Whether the game has ended
        current_player (int): Current player (BLACK or WHITE)
    """
    
    metadata = {"name": "othelloEnhanced_v1"}
    
    def __init__(self):
        """Initialize a new Othello game with standard starting position."""
        self.reset()
    
    def reset(self) -> None:
        """
        Reset the game to initial state.
        
        Sets up the standard Othello starting position with 4 pieces
        in the center of the board.
        """
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        
        # Set up initial position
        center = BOARD_SIZE // 2
        self.board[center-1][center-1] = BLACK
        self.board[center-1][center] = WHITE
        self.board[center][center-1] = WHITE
        self.board[center][center] = BLACK
        
        self.num_moves = 0
        self.game_over = False
        self.current_player = BLACK
    
    def is_valid_position(self, row: int, col: int) -> bool:
        """
        Check if the given position is within board boundaries.
        
        Args:
            row (int): Row coordinate
            col (int): Column coordinate
            
        Returns:
            bool: True if position is valid, False otherwise
        """
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE
    
    def get_legal_moves(self, player: int) -> List[Tuple[int, int]]:
        """
        Get all legal moves for the specified player.
        
        Args:
            player (int): Player to get moves for (BLACK or WHITE)
            
        Returns:
            List[Tuple[int, int]]: List of (row, col) tuples representing legal moves
            
        Raises:
            ValueError: If player is not BLACK or WHITE
        """
        if player not in [BLACK, WHITE]:
            raise ValueError(f"Invalid player: {player}. Must be {BLACK} (BLACK) or {WHITE} (WHITE)")
        
        legal_moves = []
        
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == EMPTY and self._is_legal_move(row, col, player):
                    legal_moves.append((row, col))
        
        return legal_moves
    
    def _is_legal_move(self, row: int, col: int, player: int) -> bool:
        """
        Check if a move is legal for the given player.
        
        Args:
            row (int): Row coordinate
            col (int): Column coordinate
            player (int): Player making the move
            
        Returns:
            bool: True if move is legal, False otherwise
        """
        if not self.is_valid_position(row, col) or self.board[row][col] != EMPTY:
            return False
        
        opponent = -player
        
        # Check all 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                     (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            if self._check_direction(row, col, dr, dc, player, opponent):
                return True
        
        return False
    
    def _check_direction(self, row: int, col: int, dr: int, dc: int, 
                        player: int, opponent: int) -> bool:
        """
        Check if a move is legal in a specific direction.
        
        Args:
            row (int): Starting row
            col (int): Starting column
            dr (int): Row direction (-1, 0, or 1)
            dc (int): Column direction (-1, 0, or 1)
            player (int): Current player
            opponent (int): Opponent player
            
        Returns:
            bool: True if move captures pieces in this direction
        """
        r, c = row + dr, col + dc
        has_opponent_between = False
        
        while self.is_valid_position(r, c):
            if self.board[r][c] == opponent:
                has_opponent_between = True
            elif self.board[r][c] == player:
                return has_opponent_between
            else:  # Empty square
                break
            r, c = r + dr, c + dc
        
        return False
    
    def make_move(self, row: int, col: int, player: Optional[int] = None) -> bool:
        """
        Make a move for the specified player.
        
        Args:
            row (int): Row coordinate (or -1 for pass)
            col (int): Column coordinate (or -1 for pass)
            player (int, optional): Player making the move. If None, uses current_player
            
        Returns:
            bool: True if move was successful, False if it was a pass
            
        Raises:
            GameOverError: If the game has already ended
            InvalidMoveError: If the move is invalid
            ValueError: If player is invalid
        """
        if self.game_over:
            raise GameOverError("Cannot make moves on a completed game")
        
        if player is None:
            player = self.current_player
        elif player not in [BLACK, WHITE]:
            raise ValueError(f"Invalid player: {player}. Must be {BLACK} or {WHITE}")
        
        # Handle pass move
        if row == -1 and col == -1:
            self.num_moves += 1
            self._switch_player()
            return False
        
        # Validate move
        if not self.is_valid_position(row, col):
            raise InvalidMoveError(f"Move ({row}, {col}) is outside board boundaries")
        
        if self.board[row][col] != EMPTY:
            raise InvalidMoveError(f"Square ({row}, {col}) is not empty")
        
        if not self._is_legal_move(row, col, player):
            raise InvalidMoveError(f"Move ({row}, {col}) is not legal for player {player}")
        
        # Make the move
        self.board[row][col] = player
        self._flip_pieces(row, col, player)
        self.num_moves += 1
        self._switch_player()
        
        # Check if game is over
        self._update_game_over_status()
        
        return True
    
    def _flip_pieces(self, row: int, col: int, player: int) -> None:
        """
        Flip all pieces captured by the move.
        
        Args:
            row (int): Row of the move
            col (int): Column of the move
            player (int): Player making the move
        """
        opponent = -player
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                     (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            if self._check_direction(row, col, dr, dc, player, opponent):
                self._flip_direction(row, col, dr, dc, player, opponent)
    
    def _flip_direction(self, row: int, col: int, dr: int, dc: int, 
                       player: int, opponent: int) -> None:
        """
        Flip pieces in a specific direction.
        
        Args:
            row (int): Starting row
            col (int): Starting column
            dr (int): Row direction
            dc (int): Column direction
            player (int): Current player
            opponent (int): Opponent player
        """
        r, c = row + dr, col + dc
        
        while self.is_valid_position(r, c) and self.board[r][c] == opponent:
            self.board[r][c] = player
            r, c = r + dr, c + dc
    
    def _switch_player(self) -> None:
        """Switch the current player."""
        self.current_player = -self.current_player
    
    def _update_game_over_status(self) -> None:
        """Update the game over status based on current board state."""
        black_moves = len(self.get_legal_moves(BLACK))
        white_moves = len(self.get_legal_moves(WHITE))
        board_full = np.count_nonzero(self.board == EMPTY) == 0
        
        self.game_over = (black_moves == 0 and white_moves == 0) or board_full
    
    def is_game_over(self) -> bool:
        """
        Check if the game has ended.
        
        Returns:
            bool: True if game is over, False otherwise
        """
        return self.game_over
    
    def get_score(self) -> Tuple[int, int]:
        """
        Get the current score.
        
        Returns:
            Tuple[int, int]: (black_score, white_score)
        """
        black_count = np.count_nonzero(self.board == BLACK)
        white_count = np.count_nonzero(self.board == WHITE)
        return black_count, white_count
    
    def get_winner(self) -> Optional[int]:
        """
        Get the winner of the game.
        
        Returns:
            Optional[int]: BLACK if black wins, WHITE if white wins, 
                          None if game is not over or it's a draw
        """
        if not self.game_over:
            return None
        
        black_score, white_score = self.get_score()
        if black_score > white_score:
            return BLACK
        elif white_score > black_score:
            return WHITE
        else:
            return None  # Draw
    
    def display_board(self, use_symbols: bool = True) -> str:
        """
        Get a string representation of the board.
        
        Args:
            use_symbols (bool): If True, use 'X', 'O', and '_' for display.
                               If False, use numeric values.
                               
        Returns:
            str: String representation of the board
        """
        if use_symbols:
            symbol_map = {EMPTY: '_', BLACK: 'X', WHITE: 'O'}
            board_str = '\n'.join(' '.join(symbol_map[cell] for cell in row) 
                                for row in self.board)
        else:
            board_str = str(self.board)
        
        black_score, white_score = self.get_score()
        header = f"Black (X): {black_score}, White (O): {white_score}\n"
        header += f"Current player: {'Black (X)' if self.current_player == BLACK else 'White (O)'}\n"
        
        return header + board_str
    
    def copy(self) -> 'OthelloEnvEnhanced':
        """
        Create a deep copy of the current game state.
        
        Returns:
            OthelloEnvEnhanced: New instance with identical state
        """
        new_game = OthelloEnvEnhanced()
        new_game.board = self.board.copy()
        new_game.num_moves = self.num_moves
        new_game.game_over = self.game_over
        new_game.current_player = self.current_player
        return new_game


def play_enhanced_game_demo():
    """Demonstration of the enhanced Othello game."""
    game = OthelloEnvEnhanced()
    
    print("Enhanced Othello Game Demo")
    print("=" * 30)
    print(game.display_board())
    
    # Show initial legal moves
    black_moves = game.get_legal_moves(BLACK)
    print(f"\nLegal moves for Black: {black_moves}")
    
    # Make a few moves
    try:
        game.make_move(2, 4)  # Black move
        print(f"\nAfter Black plays (2, 4):")
        print(game.display_board())
        
        white_moves = game.get_legal_moves(WHITE)
        print(f"\nLegal moves for White: {white_moves}")
        
        game.make_move(2, 3)  # White move
        print(f"\nAfter White plays (2, 3):")
        print(game.display_board())
        
    except (InvalidMoveError, GameOverError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    play_enhanced_game_demo()