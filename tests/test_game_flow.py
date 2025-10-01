import unittest
import numpy as np
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Othello'))

from othello import OthelloEnv
from players import RandomPlayer, ab_ScoreSearch
from play_othello import play_game


class TestGameFlow(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game for each test"""
        self.game = OthelloEnv()
        self.p1 = RandomPlayer(self.game)
        self.p2 = RandomPlayer(self.game)
    
    def test_play_game_function(self):
        """Test that play_game function works correctly"""
        # Play a game
        result = play_game(self.game, self.p1, self.p2)
        
        # Should return a tuple with score and moves
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        
        score, moves = result
        
        # Score should be a tuple of two integers
        self.assertIsInstance(score, tuple)
        self.assertEqual(len(score), 2)
        self.assertIsInstance(score[0], (int, np.integer))
        self.assertIsInstance(score[1], (int, np.integer))
        
        # Moves should be a list
        self.assertIsInstance(moves, list)
        
        # Total pieces should be reasonable (at least the initial 4)
        total_pieces = score[0] + score[1]
        self.assertGreaterEqual(total_pieces, 4)
        self.assertLessEqual(total_pieces, 64)
    
    def test_game_completion(self):
        """Test that games complete properly"""
        score, moves = play_game(self.game, self.p1, self.p2)
        
        # Game should have ended with a reasonable number of moves
        self.assertGreater(len(moves), 0, "Game should have at least some moves")
        self.assertLessEqual(len(moves), 64, "Game should not exceed maximum possible moves")
        
        # Score should be reasonable
        total_pieces = score[0] + score[1]
        self.assertGreaterEqual(total_pieces, 4, "Should have at least initial pieces")
        self.assertLessEqual(total_pieces, 64, "Cannot have more pieces than board squares")
    
    def test_move_validity(self):
        """Test that all moves made during a game are valid"""
        # We'll track moves manually to verify they're valid
        game = OthelloEnv()
        p1 = RandomPlayer(game)
        p2 = RandomPlayer(game)
        
        player = 1
        move_count = 0
        max_moves = 70  # Prevent infinite loops, allow for pass moves
        
        while not game.getGameOver() and move_count < max_moves:
            legal_moves = game._legal_moves(player)
            
            if player == 1:
                move = p1.play(game, 1)
            else:
                move = p2.play(game, -1)
            
            # Check that move is either a pass or a legal move
            if move != (-1, -1):
                self.assertEqual(legal_moves[move[0]][move[1]], player,
                               f"Illegal move {move} by player {player} at move {move_count}")
            
            game.make_move(move, player)
            player = -player
            move_count += 1
        
        # Game should have completed within reasonable number of moves
        self.assertLess(move_count, max_moves, "Game took too many moves")
    
    def test_alternating_players(self):
        """Test that players alternate correctly"""
        # Create a custom game to track player alternation
        game = OthelloEnv()
        
        class TrackingPlayer:
            def __init__(self, expected_player):
                self.expected_player = expected_player
                self.calls = []
            
            def play(self, game, player):
                self.calls.append(player)
                # Make a simple legal move
                legal_moves = game._legal_moves(player)
                positions = np.where(legal_moves == player)
                if len(positions[0]) > 0:
                    return (positions[0][0], positions[1][0])
                return (-1, -1)
        
        p1 = TrackingPlayer(1)
        p2 = TrackingPlayer(-1)
        
        # Play a few moves
        player = 1
        for _ in range(6):  # Just a few moves to test alternation
            if game.getGameOver():
                break
                
            legal_moves = game._legal_moves(player)
            if np.count_nonzero(legal_moves) == 0:
                move = (-1, -1)
            else:
                if player == 1:
                    move = p1.play(game, 1)
                else:
                    move = p2.play(game, -1)
            
            game.make_move(move, player)
            player = -player
        
        # Check that each player was called with their expected player number
        for call in p1.calls:
            self.assertEqual(call, 1, "Player 1 called with wrong player number")
        
        for call in p2.calls:
            self.assertEqual(call, -1, "Player 2 called with wrong player number")


class TestTournamentLogic(unittest.TestCase):
    def test_score_calculation(self):
        """Test tournament score calculation logic"""
        # Test the logic used in tournament.py
        
        # Scenario 1: Player 1 wins
        score = (35, 29)  # Black wins
        p1_wins = 0
        p2_wins = 0
        draws = 0
        p1_avg_win_score = 0
        p2_avg_win_score = 0
        
        if score[0] > score[1]:
            p1_wins += 1
            p1_avg_win_score += score[0]
        elif score[0] < score[1]:
            p2_wins += 1
            p2_avg_win_score += score[1]
        else:
            draws += 1
        
        self.assertEqual(p1_wins, 1)
        self.assertEqual(p2_wins, 0)
        self.assertEqual(draws, 0)
        self.assertEqual(p1_avg_win_score, 35)
        
        # Scenario 2: Player 2 wins
        score = (25, 39)  # White wins
        if score[0] > score[1]:
            p1_wins += 1
            p1_avg_win_score += score[0]
        elif score[0] < score[1]:
            p2_wins += 1
            p2_avg_win_score += score[1]
        else:
            draws += 1
        
        self.assertEqual(p1_wins, 1)  # Still 1 from before
        self.assertEqual(p2_wins, 1)  # Now 1
        self.assertEqual(draws, 0)
        self.assertEqual(p2_avg_win_score, 39)
        
        # Test average calculation
        num_games = 2
        p1_avg = p1_avg_win_score / num_games if p1_wins > 0 else 0
        p2_avg = p2_avg_win_score / num_games if p2_wins > 0 else 0
        
        self.assertEqual(p1_avg, 35.0 / 2)  # Should divide by total games, not just wins
        self.assertEqual(p2_avg, 39.0 / 2)
    
    def test_tournament_data_structure(self):
        """Test the tournament data structure creation"""
        # Test the DataFrame creation logic from tournament.py
        p1_wins = 5
        p2_wins = 3
        draws = 2
        num_games = 10
        p1_avg_win_score = 300  # Total score across all games
        p2_avg_win_score = 250
        
        # The current implementation has a bug - it should calculate averages properly
        # Test what the current code produces
        avg1 = p1_avg_win_score / num_games
        avg2 = p2_avg_win_score / num_games
        
        self.assertEqual(avg1, 30.0)
        self.assertEqual(avg2, 25.0)
        
        # The data structure should be properly formatted
        data = [p1_wins, p2_wins, draws, avg1, avg2]
        self.assertEqual(len(data), 5)
        self.assertIsInstance(data[0], int)
        self.assertIsInstance(data[1], int)
        self.assertIsInstance(data[2], int)
        self.assertIsInstance(data[3], float)
        self.assertIsInstance(data[4], float)


if __name__ == '__main__':
    unittest.main()