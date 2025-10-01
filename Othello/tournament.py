from othello import OthelloEnv
from players import RandomPlayer, ab_ScoreSearch
from play_othello import play_game
import pandas as pd
import numpy as np

def run_tournament(player1_class, player2_class, num_games=100, verbose=True):
    """Run a tournament between two player classes"""
    
    # Initialize statistics
    p1_wins = 0
    p2_wins = 0
    draws = 0
    p1_total_score = 0
    p2_total_score = 0
    
    game_results = []
    
    for i in range(num_games):
        # Create fresh game and players for each match
        game = OthelloEnv()
        p1 = player1_class(game)
        p2 = player2_class(game)
        
        # Play the game
        result = play_game(game, p1, p2)
        score, moves = result
        
        # Record results
        p1_score, p2_score = score
        p1_total_score += p1_score
        p2_total_score += p2_score
        
        if p1_score > p2_score:
            p1_wins += 1
        elif p2_score > p1_score:
            p2_wins += 1
        else:
            draws += 1
        
        game_results.append({
            'game': i + 1,
            'p1_score': p1_score,
            'p2_score': p2_score,
            'winner': 'P1' if p1_score > p2_score else 'P2' if p2_score > p1_score else 'Draw',
            'total_moves': len(moves)
        })
        
        if verbose and (i + 1) % 10 == 0:
            print(f"Completed {i + 1}/{num_games} games")
    
    # Calculate statistics
    p1_win_rate = p1_wins / num_games * 100
    p2_win_rate = p2_wins / num_games * 100
    draw_rate = draws / num_games * 100
    
    p1_avg_score = p1_total_score / num_games
    p2_avg_score = p2_total_score / num_games
    
    # Only calculate win averages if there were wins
    p1_avg_win_score = sum(r['p1_score'] for r in game_results if r['winner'] == 'P1') / p1_wins if p1_wins > 0 else 0
    p2_avg_win_score = sum(r['p2_score'] for r in game_results if r['winner'] == 'P2') / p2_wins if p2_wins > 0 else 0
    
    results = {
        'p1_wins': p1_wins,
        'p2_wins': p2_wins,
        'draws': draws,
        'p1_win_rate': p1_win_rate,
        'p2_win_rate': p2_win_rate,
        'draw_rate': draw_rate,
        'p1_avg_score': p1_avg_score,
        'p2_avg_score': p2_avg_score,
        'p1_avg_win_score': p1_avg_win_score,
        'p2_avg_win_score': p2_avg_win_score,
        'game_results': game_results
    }
    
    return results

def print_tournament_results(results):
    """Print formatted tournament results"""
    print("\n" + "="*50)
    print("TOURNAMENT RESULTS")
    print("="*50)
    print(f"Player 1 wins: {results['p1_wins']} ({results['p1_win_rate']:.1f}%)")
    print(f"Player 2 wins: {results['p2_wins']} ({results['p2_win_rate']:.1f}%)")
    print(f"Draws: {results['draws']} ({results['draw_rate']:.1f}%)")
    print(f"\nAverage scores:")
    print(f"Player 1: {results['p1_avg_score']:.1f}")
    print(f"Player 2: {results['p2_avg_score']:.1f}")
    print(f"\nAverage winning scores:")
    print(f"Player 1: {results['p1_avg_win_score']:.1f}")
    print(f"Player 2: {results['p2_avg_win_score']:.1f}")

def save_tournament_results(results, filename):
    """Save tournament results to CSV"""
    df = pd.DataFrame(results['game_results'])
    df.to_csv(filename, index=False)
    print(f"\nDetailed results saved to {filename}")

# Example tournament run
if __name__ == "__main__":
    print("Running tournament: ab_ScoreSearch vs RandomPlayer")
    results = run_tournament(ab_ScoreSearch, RandomPlayer, num_games=20, verbose=True)
    print_tournament_results(results)
    save_tournament_results(results, "tournament_results.csv")
