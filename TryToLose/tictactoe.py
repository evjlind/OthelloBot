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
        diag1 = 0
        diag2 = 0
        for i in range(3):
            diag1 = board[i][i]+diag1
            diag2 = board[i][2-i]+diag2
            if diag1 == 3*player or diag2 == 3*player:
                return True
        return False
    
    def has_drawn(board):
        for i in board:
            for j in i:
                if j == 0:
                    return False
        return True

    def get_all_moves(board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    moves.append((i,j))
        return moves
    
def playing(board):
    if TicTacToe.has_won(board, 1):
        return False
    elif TicTacToe.has_won(board,-1):
        return False
    elif TicTacToe.has_drawn(board):
        return False
    else:
        return True
    
def get_best_move(board, player):
    if TicTacToe.has_won(board,player):
        return -player # we "win" so its bad
    elif TicTacToe.has_won(board,-player):
        return player # we "lost" so its good
    elif TicTacToe.has_drawn(board):
        return 0
    moves = TicTacToe.get_all_moves(board)
    checking = 0
    bufferMove = []
    good_moves = []
    while checking < len(moves):
        #print(board)
        currentMove = moves[checking]
        board[currentMove[0]][currentMove[1]] = player
        #print((player, " finding move for"))
        if TicTacToe.playing(board):
            make_move(-player,board)
        else:
            if TicTacToe.has_won(board,player):
                pass
            elif TicTacToe.has_won(board,-player):
                good_moves.append(currentMove)
            else:
                bufferMove = currentMove
    if len(good_moves)!=0:
        return good_moves
    else:
        return bufferMove

def make_move(player,board):
    move = get_best_move(board,player)
    move = move[np.random.randint(0,len(move)-1)]
    board[move[0]][move[1]] = player
    print(move)
    return board


player = 1
#currently creates infinite loop somewhere outside this while
while (playing(board)):
    board = make_move(player,board)
    #print((player, " made move"))
    player = -player
