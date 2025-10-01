import unittest
import numpy as np
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Othello'))

from othello import OthelloEnv


class TestOthelloGame(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game for each test"""
        self.game = OthelloEnv()
    
    def test_initialization(self):
        """Test that the game initializes correctly"""
        # Check board dimensions
        self.assertEqual(self.game.board.shape, (8, 8))
        
        # Check initial piece placement
        self.assertEqual(self.game.board[3][3], 1)  # Black
        self.assertEqual(self.game.board[3][4], -1)  # White
        self.assertEqual(self.game.board[4][3], -1)  # White
        self.assertEqual(self.game.board[4][4], 1)  # Black
        
        # Check that other squares are empty
        self.assertEqual(np.sum(self.game.board == 0), 60)  # 64 - 4 initial pieces
        
        # Check initial state
        self.assertEqual(self.game.num_moves, 0)
        self.assertEqual(self.game.moves.shape, (8, 8))
    
    def test_reset(self):
        """Test that reset properly resets the game state"""
        # Make some moves first
        self.game.num_moves = 10
        self.game.board[0][0] = 1
        
        # Reset the game
        self.game.reset()
        
        # Check that it's back to initial state
        self.assertEqual(self.game.num_moves, 0)
        self.assertEqual(self.game.board[3][3], 1)
        self.assertEqual(self.game.board[3][4], -1)
        self.assertEqual(self.game.board[4][3], -1)
        self.assertEqual(self.game.board[4][4], 1)
        self.assertEqual(self.game.board[0][0], 0)
    
    def test_initial_legal_moves(self):
        """Test that initial legal moves are correct"""
        # Black player (1) should have 4 legal moves initially
        black_moves = self.game._legal_moves(1)
        legal_positions = np.where(black_moves == 1)
        
        # Expected initial moves for black given initial board setup in code
        expected_moves = [(2, 4), (3, 5), (4, 2), (5, 3)]
        actual_moves = list(zip(legal_positions[0], legal_positions[1]))
        
        self.assertEqual(len(actual_moves), 4)
        for move in expected_moves:
            self.assertIn(move, actual_moves)
        
        # White player (-1) should also have 4 legal moves initially
        white_moves = self.game._legal_moves(-1)
        legal_positions = np.where(white_moves == -1)
        
        expected_moves = [(2, 3), (3, 2), (4, 5), (5, 4)]
        actual_moves = list(zip(legal_positions[0], legal_positions[1]))
        
        self.assertEqual(len(actual_moves), 4)
        for move in expected_moves:
            self.assertIn(move, actual_moves)
    
    def test_make_move_basic(self):
        """Test basic move making and piece flipping"""
        # Black makes first move
        move = (2, 3)
        self.game.make_move(move, 1)
        
        # Check that the piece was placed
        self.assertEqual(self.game.board[2][3], 1)
        
        # Check that the white piece at (3,3) was flipped to black
        self.assertEqual(self.game.board[3][3], 1)
        
        # Check move counter
        self.assertEqual(self.game.num_moves, 1)
    
    def test_make_move_multiple_directions(self):
        """Test move that flips pieces in multiple directions"""
        # Set up a specific board state
        self.game.board = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, -1, -1, 0, 0, 0],
            [0, 0, -1, 1, -1, 0, 0, 0],
            [0, 0, -1, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        
        # Black plays at (2, 5) which should flip pieces horizontally
        self.game.make_move((2, 5), 1)
        
        # Check the move was made
        self.assertEqual(self.game.board[2][5], 1)
        
        # Check that pieces were flipped
        self.assertEqual(self.game.board[2][4], 1)
        self.assertEqual(self.game.board[2][3], 1)
    
    def test_pass_move(self):
        """Test that pass moves are handled correctly"""
        initial_num_moves = self.game.num_moves
        self.game.make_move((-1, -1), 1)
        
        # Move counter should still increment for pass moves
        self.assertEqual(self.game.num_moves, initial_num_moves + 1)
        
        # Board should remain unchanged
        self.assertEqual(self.game.board[3][3], 1)
        self.assertEqual(self.game.board[3][4], -1)
        self.assertEqual(self.game.board[4][3], -1)
        self.assertEqual(self.game.board[4][4], 1)
    
    def test_score_board(self):
        """Test board scoring"""
        # Initial score should be 2-2
        black_score, white_score = self.game.score_board()
        self.assertEqual(black_score, 2)
        self.assertEqual(white_score, 2)
        
        # Add some pieces and test again
        self.game.board[0][0] = 1
        self.game.board[0][1] = -1
        
        black_score, white_score = self.game.score_board()
        self.assertEqual(black_score, 3)
        self.assertEqual(white_score, 3)
    
    def test_game_over_detection(self):
        """Test game over detection"""
        # Initial state should not be game over
        self.assertFalse(self.game.getGameOver())
        
        # Create a board with no legal moves for either player
        self.game.board = np.ones((8, 8))  # All black pieces
        self.assertTrue(self.game.getGameOver())
    
    def test_edge_cases(self):
        """Test various edge cases"""
        # Test moves at board edges
        self.game.board = np.zeros((8, 8))
        self.game.board[0][0] = 1
        self.game.board[0][1] = -1
        self.game.board[0][2] = 0
        
        # This should be a legal move for black
        legal_moves = self.game._legal_moves(1)
        self.assertEqual(legal_moves[0][2], 1)
    
    def test_no_legal_moves(self):
        """Test behavior when a player has no legal moves"""
        # Create a board where black has no legal moves
        self.game.board = np.zeros((8, 8))
        self.game.board[3][3] = -1
        self.game.board[3][4] = -1
        self.game.board[4][3] = -1
        self.game.board[4][4] = -1
        
        # Black should have no legal moves
        legal_moves = self.game._legal_moves(1)
        self.assertEqual(np.sum(legal_moves), 0)
    
    def test_bounds_checking(self):
        """Test that bounds checking works properly"""
        # This shouldn't crash even with edge pieces
        self.game.board[7][7] = 1
        legal_moves = self.game._legal_moves(1)
        # Should not crash and should return valid array
        self.assertEqual(legal_moves.shape, (8, 8))


class TestOthelloGameFlow(unittest.TestCase):
    """Test complete game scenarios"""
    
    def test_complete_game_flow(self):
        """Test a simple complete game"""
        game = OthelloEnv()
        
        # Play a few moves
        moves_sequence = [
            ((2, 3), 1),   # Black
            ((2, 4), -1),  # White
            ((2, 5), 1),   # Black
        ]
        
        for move, player in moves_sequence:
            game.make_move(move, player)
        
        # Game should still be ongoing
        self.assertFalse(game.getGameOver())
        
        # Scores should be reasonable
        black_score, white_score = game.score_board()
        self.assertGreater(black_score + white_score, 4)  # More than initial 4 pieces


if __name__ == '__main__':
    # Create tests directory if it doesn't exist
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    
    unittest.main()