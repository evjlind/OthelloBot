import numpy as np
import math
from tictactoe import TicTacToe as ttt
from agent import agent

board = ttt.__init__()
turn = 1
selecting = True
while selecting:
    human = input("human play X or O\n")
    if human == 'X':
        human = 1
        break
    elif human == 'O':
        human = -1
        break
    else:
        print("select valid piece\n")
    
ttt.disp_board(board)

while ttt.playing(board):
    if turn == human:
        selecting = True
        while selecting:
            moves = ttt.get_all_moves(board)
            print(moves)
            index = int(input("select index of move\n"))
            if 0 <= index and index <= len(moves):
                board[moves[index][0]][moves[index][1]] = human
                turn = -turn
                selecting = False
            else:
                print("select a valid move\n")
        ttt.disp_board(board)
    else:
        print("Agent move:")
        all_moves = ttt.get_all_moves(board)
        scores = np.empty(len(all_moves))
        for move in range(len(all_moves)):
            scores[move] = agent.score_move(board,all_moves[move],9,turn,-math.inf,math.inf)
        if turn == 1:
            index = np.where(scores == np.max(scores))
        else:
            index = np.where(scores == np.min(scores))
        row = all_moves[index[0][0]][0]
        col = all_moves[index[0][0]][1]
        print((row,col))
        board[row][col] = turn
        turn = -turn
        ttt.disp_board(board)

if ttt.score(board) == human:
    print("Human wins!")
elif ttt.score(board) == -human:
    print("Agent wins")
else:
    print("Draw")