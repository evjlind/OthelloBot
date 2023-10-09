import numpy as np
import math
from tictactoe import TicTacToe as ttt
from agent import agent

board = ttt.__init__()
turn = 1

human = int(input("human play 1 or -1"))

print(board)

while ttt.playing(board):
    if turn == human:
        row = int(input("human move row"))
        col = int(input("human move col"))
        board[row][col] = human
        turn = -turn
        print(board)
    else:
        all_moves = ttt.get_all_moves(board)
        scores = np.empty(len(all_moves))
        for move in range(len(all_moves)):
            print(all_moves[move])
            scores[move] =  agent.score_move(board,all_moves[move],10,turn,-math.inf,math.inf)
        print(scores)
        if turn == 1:
            index = np.where(scores == np.max(scores))
        else:
            index = np.where(scores == np.min(scores))
        board[all_moves[index[0][0]][0]][all_moves[index[0][0]][1]] = turn
        turn = -turn
        print(board)