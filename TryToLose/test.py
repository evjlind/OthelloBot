from tictactoe import TicTacToe
import numpy as np
import time

def minimax(board,maximizing):
    if not TicTacToe.playing(board):
        return TicTacToe.score(board)
    if np.sum(board) == 0:
        player = 1
    else:
        player = -1
    scores = []
    moves = []
    bufferBoard = board
    moves = TicTacToe.get_all_moves(board)
    for i in moves:
        bufferBoard[i[0]][i[1]] = player
        scores.append(minimax(bufferBoard,-maximizing))
        bufferBoard[i[0]][i[1]] = 0
    return scores.index(min(scores)) if maximizing == 1 else max(scores)

board = TicTacToe.__init__()

print(board)
human = int(input("human play 1 or -1"))
playing = 1
while TicTacToe.playing(board):
    if human == playing:
        row = (input('move row'))
        col = (input('move col'))
        board[int(row)][int(col)] = human
        playing = -int(playing)
        print(board)
    else:
        print('ai move')
        moves = TicTacToe.get_all_moves(board)
        choice = minimax(board,-human)
        ai_move = moves[choice]
        board[ai_move[0]][ai_move[1]] = -human
        playing = -playing
        print(board)
print(TicTacToe.score(board))