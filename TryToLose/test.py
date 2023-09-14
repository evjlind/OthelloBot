from tictactoe import TicTacToe
import numpy as np

def get_best_move(player, board):
    moves = TicTacToe.get_all_moves(board)
    checking = 0
    good_moves = []
    drawable = False
    while checking < len(moves):
        bufferBoard = board
        currentMove = moves[checking]
        bufferBoard[currentMove[0]][currentMove[1]] = player
        print("checking move: " + str(checking) + " for " + str(player))
        if playing(bufferBoard):
            bufferBoard = make_move(-player,bufferBoard)
        else:
            if TicTacToe.has_won(bufferBoard,-player):
                good_moves.append(currentMove)
                checking = checking + 1
            elif TicTacToe.has_drawn(bufferBoard):
                bufferMove = currentMove
                checking = checking + 1
                drawable = True
            elif drawable:
                checking = checking + 1
            else:
                bufferMove = currentMove
                checking = checking + 1
    if len(good_moves)>0:
        return good_moves
    else:
        return bufferMove

def playing(board):
    if TicTacToe.has_won(board, 1):
        return False
    elif TicTacToe.has_won(board,-1):
        return False
    elif TicTacToe.has_drawn(board):
        return False
    else:
        return True

def make_move(player,board):
    moves = get_best_move(player,board)
    if type(moves) == list:
        move_ind = np.random.randint(0,len(moves)-1)
        move = moves[move_ind]
    else:
        move = moves
    row = move[0]
    col = move[1]
    board[row][col] = player
    return board

board = TicTacToe.__init__()
player = 1
while (playing(board)):
    board = make_move(player,board)
    player = -player