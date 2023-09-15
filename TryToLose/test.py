from tictactoe import TicTacToe
import numpy as np
import time

def minimax(board):
    if not TicTacToe.playing(board):
        return score(board)
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
        scores.append(minimax(bufferBoard))
        bufferBoard[i[0]][i[1]] = 0
    return max(scores) if player == 1 else min(scores)


def score(board):
    if TicTacToe.has_won(board, 1):
        return -1
    elif TicTacToe.has_won(board,-1):
        return 1
    elif TicTacToe.has_drawn(board):
        return 0

board = TicTacToe.__init__()


result = minimax(board)
playing = 1
while TicTacToe.playing(board):
    human = input("human play 1 or -1")
    if human == playing:
        row = int(input('move row'))
        col = int(input('move col'))
        board[row][col] = human
    else:
        moves = TicTacToe.get_all_moves(board)
        choice = minimax(board)
        moves[choice.index(c)]