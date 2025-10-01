from players import *
from othello import OthelloEnv
import math
import numpy as np
import time

def decoratorTimer(decimal,func):
    def decoratorFunc(f):
        def wrap(*args,**kwargs):
            time1 = time.monotonic()
            result = f(*args,**kwargs)
            time2 = time.monotonic()
            print('{:s} {:s} function took {:.{}f} ms'.format(func,f.__name__, ((time2-time1)*1000.0), decimal ))
            return result
        return wrap
    return decoratorFunc

def play_game(game,p1,p2):
    player = 1
    moves = []
    consecutive_passes = 0
    max_moves = 64  # Maximum possible moves in Othello
    
    while not game.getGameOver() and len(moves) < max_moves:
        # Check for legal moves
        legal_moves = game._legal_moves(player)
        has_legal_moves = np.count_nonzero(legal_moves) > 0
        
        if has_legal_moves:
            if player == 1:
                move = p1.play(game, 1)
            else:
                move = p2.play(game, -1)
            consecutive_passes = 0
        else:
            # Player must pass
            move = (-1, -1)
            consecutive_passes += 1
            
        # If both players pass consecutively, game is over
        if consecutive_passes >= 2:
            break
            
        game.make_move(move, player)
        moves.append(move)
        player = -player
        
    score = game.score_board()
    return score, moves
# Example usage (uncomment to run):
# if __name__ == "__main__":
#     start = time.time()
#     game = OthelloEnv()
#     p1 = RandomPlayer(game)
#     p2 = RandomPlayer(game)
#     score, moves = play_game(game, p1, p2)
#     print(f"Final score: {score}")
#     print(f"Total moves: {len(moves)}")
#     end = time.time()
#     print(f"Execution time: {end-start:.3f}s")
