'''
Is Losing at Tic-Tac-Toe Possible?
Can one player force the other player "Win"?

Based on a random discussion I had with my roommate last year.

X = 1
O = -1
Empty = 0
'''

import numpy as np

board = np.array([[0,0,0],[0,0,0],[0,0,0]])

class TicTacToe():
    def __init__():
        board = np.array([[0,0,0],[0,0,0],[0,0,0]])
        return board

    def has_won(board, player):
        cols = np.sum(board,axis=0)
        rows = np.sum(board, axis=1)
        for i in cols:
            if i == 3*player:
                return True
        for i in rows:
            if i == 3*player:
                return True
        if np.sum(board.diagonal()) == 3*player:
            return True
        elif np.sum(np.fliplr(board).diagonal()) == 3*player:
            return True 
        return False

    def get_all_moves(board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    moves.append((i,j))
        return moves
    
    def game_over(board):
        for i in board:
            for j in i:
                if j == 0:
                    return False
        return True
    
    def has_drawn(board):
        if (not TicTacToe.has_won(board,1)) and (not TicTacToe.has_won(board,-1)):
            for i in board:
                for j in i:
                    if j == 0:
                        return False
            return True
    
    def playing(board):
        if TicTacToe.has_won(board,1):
            return False
        elif TicTacToe.has_won(board,-1):
            return False
        elif TicTacToe.has_drawn(board):
            return False
        elif TicTacToe.game_over(board):
            return False
        else:
            return True
        
    def score(board):
        if TicTacToe.has_won(board, 1):
            return -1
        elif TicTacToe.has_won(board,-1):
            return 1
        elif TicTacToe.has_drawn(board):
            return 0