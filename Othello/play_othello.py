from players import *
from othello import OthelloEnv
import math
import numpy as np

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

game = OthelloEnv()
p1 = ab_Mobility(game)
p2 = ab_ScoreSearch(game)
scores = np.zeros_like(game.board)
game.moves = OthelloEnv._legal_moves(game,1)
score,moves = play_game(game,p1,p2)
print(score)
print(moves)