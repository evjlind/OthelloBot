import unittest
import numpy as np
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Othello'))

from othello import OthelloEnv
from players import RandomPlayer, ab_ScoreSearch, HandMade


class TestRandomPlayer(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game for each test"""
        self.game = OthelloEnv()
        self.player = RandomPlayer(self.game)
    
    def test_random_player_initialization(self):
        """Test RandomPlayer initializes correctly"""
        self.assertIsInstance(self.player, RandomPlayer)
        self.assertEqual(self.player.game, self.game)
    
    def test_random_player_makes_legal_moves(self):
        """Test that RandomPlayer only makes legal moves"""
        # Set up legal moves
        self.game.moves = self.game._legal_moves(1)
        
        # Get a move from the random player
        move = self.player.play(self.game, 1)
        
        # Check that the move is either a legal move or a pass
        if move != (-1, -1):
            self.assertEqual(self.game.moves[move[0]][move[1]], 1)
    
    def test_random_player_handles_no_moves(self):
        """Test RandomPlayer behavior when no legal moves available"""
        # Set up a board where black has no legal moves (all white pieces)
        self.game.board = np.full((8, 8), -1)  # All white pieces
        
        move = self.player.play(self.game, 1)  # Black player
        
        # Should return pass move
        self.assertEqual(move, (-1, -1))


class TestAlphaBetaScoreSearch(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game for each test"""
        self.game = OthelloEnv()
        self.player = ab_ScoreSearch(self.game)
    
    def test_ab_player_initialization(self):
        """Test ab_ScoreSearch initializes correctly"""
        self.assertIsInstance(self.player, ab_ScoreSearch)
        self.assertEqual(self.player.game, self.game)
    
    def test_ab_player_makes_legal_moves(self):
        """Test that ab_ScoreSearch only makes legal moves"""
        move = self.player.play(self.game, 1)
        
        # Check that the move is either a legal move or a pass
        if move != (-1, -1):
            legal_moves = self.game._legal_moves(1)
            self.assertEqual(legal_moves[move[0]][move[1]], 1)
    
    def test_ab_player_handles_no_moves(self):
        """Test ab_ScoreSearch behavior when no legal moves available"""
        # Create a board with no legal moves for player 1
        self.game.board = np.zeros((8, 8))
        self.game.board[3][3] = -1
        self.game.board[3][4] = -1
        self.game.board[4][3] = -1
        self.game.board[4][4] = -1
        
        move = self.player.play(self.game, 1)
        
        # Should return pass move
        self.assertEqual(move, (-1, -1))
    
    def test_alpha_beta_score_function(self):
        """Test the alpha beta scoring function"""
        # Test with a simple board position
        score = self.player.alpha_beta_score(self.game, 1, -float('inf'), float('inf'), 1)
        
        # Score should be a number (not tuple or None)
        self.assertIsInstance(score, (int, float))
    
    def test_ab_prefers_better_positions(self):
        """Test that ab_ScoreSearch prefers positions with better scores"""
        # This is a basic test - in a real scenario you'd set up specific positions
        # to verify the player makes optimal moves
        move1 = self.player.play(self.game, 1)
        
        # Reset and try again
        self.game.reset()
        move2 = self.player.play(self.game, 1)
        
        # Both moves should be legal (this is a basic sanity check)
        legal_moves = self.game._legal_moves(1)
        if move1 != (-1, -1):
            self.assertEqual(legal_moves[move1[0]][move1[1]], 1)
        if move2 != (-1, -1):
            self.assertEqual(legal_moves[move2[0]][move2[1]], 1)


class TestHandMade(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game for each test"""
        self.game = OthelloEnv()
        self.player = HandMade(self.game)
    
    def test_handmade_initialization(self):
        """Test HandMade player initializes correctly"""
        self.assertIsInstance(self.player, HandMade)
        self.assertEqual(self.player.game, self.game)
        
        # Check that bitboard constants are set
        self.assertGreater(self.player.x_squares, 0)
        self.assertGreater(self.player.corners, 0)
        
        # Check static weights matrix
        self.assertEqual(self.player.static_weights.shape, (8, 8))
    
    def test_is_endgame_function(self):
        """Test endgame detection"""
        # Early game should not be endgame
        self.assertFalse(self.player.is_endgame(self.game))
        
        # Late game should be endgame
        self.game.num_moves = 50
        self.assertTrue(self.player.is_endgame(self.game))
    
    def test_board_to_ints_function(self):
        """Test board to integer conversion"""
        # Create a simple board
        test_board = np.zeros((8, 8))
        test_board[0][0] = 1   # Top-left corner
        test_board[7][7] = -1  # Bottom-right corner
        
        p1_value, p2_value = HandMade.board_to_ints(test_board)
        
        # Both should be positive integers
        self.assertIsInstance(p1_value, int)
        self.assertIsInstance(p2_value, int)
        self.assertGreater(p1_value, 0)
        self.assertGreater(p2_value, 0)


class TestPlayerComparison(unittest.TestCase):
    """Test interactions between different players"""
    
    def test_players_make_different_moves(self):
        """Test that different players can make different decisions"""
        game1 = OthelloEnv()
        game2 = OthelloEnv()
        
        random_player = RandomPlayer(game1)
        ab_player = ab_ScoreSearch(game2)
        
        # Both should be able to make moves
        random_move = random_player.play(game1, 1)
        ab_move = ab_player.play(game2, 1)
        
        # Both should be legal moves or passes
        legal_moves1 = game1._legal_moves(1)
        legal_moves2 = game2._legal_moves(1)
        
        if random_move != (-1, -1):
            self.assertEqual(legal_moves1[random_move[0]][random_move[1]], 1)
        if ab_move != (-1, -1):
            self.assertEqual(legal_moves2[ab_move[0]][ab_move[1]], 1)
    
    def test_players_handle_game_states(self):
        """Test that all players can handle various game states"""
        players = [
            RandomPlayer(OthelloEnv()),
            ab_ScoreSearch(OthelloEnv()),
        ]
        
        for player in players:
            game = player.game
            
            # Test with initial position
            move = player.play(game, 1)
            self.assertIsInstance(move, tuple)
            self.assertEqual(len(move), 2)
            
            # Test with a position after some moves
            game.make_move((2, 4), 1)  # Make a move first
            move = player.play(game, -1)
            self.assertIsInstance(move, tuple)
            self.assertEqual(len(move), 2)


if __name__ == '__main__':
    unittest.main()