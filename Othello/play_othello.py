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
    while not OthelloEnv.getGameOver(game):
        game.moves = OthelloEnv._legal_moves(game,player)
        if player == 1:
            move = p1.play(game,1)
        else:
            move = p2.play(game,-1)
        #print(move)
        game.make_move(move,player)
        moves.append(move)
        player = -player
    score = game.score_board()
    #print(score)
    game.disp_board()
    game.reset()
    return score, moves
start = time.time()
game = OthelloEnv()
# p1 = RandomPlayer(game)
# p2 = RandomPlayer(game)
# scores = np.zeros_like(game.board)
# score,moves = play_game(game,p1,p2)
# print(score)
# print(moves)
print(game.board)

end = time.time()
print("Execution time: {}".format(end-start))