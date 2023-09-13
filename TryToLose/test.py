from tictactoe import TicTacToe
import numpy as np

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
        if playing(board):
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
    move = get_best_move(board,player)
    move = move[np.random.randint(0,len(move)-1)]
    board[move[0]][move[1]] = player
    print(move)
    return board


board = TicTacToe.__init__()
