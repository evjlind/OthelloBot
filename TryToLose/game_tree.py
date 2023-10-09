from tictactoe import TicTacToe
import math
board = TicTacToe.__init__()
def minimax(turn,depth):
    if turn == 1:
        best = [-1,-1,-math.inf]
    else:
        best = [-1,-1,math.inf]
    if not TicTacToe.playing(board): #defines leaf node
        return [-1,-1,TicTacToe.score(board)]
    moves = TicTacToe.get_all_moves(board)
    for i in range(len(moves)):
        board[moves[i][0]][moves[i][1]] = turn
        score = minimax(-turn,depth+1)
        board[moves[i][0]][moves[i][1]] = 0
        score[0] = moves[i][0]
        score[1] = moves[i][1]
    if turn == 1:
        if score[2] > best[2]:
            best = score
    else:
        if score[2] < best[2]:
            best = score
    return best

board = TicTacToe.__init__()

human = int(input("human play 1 or -1"))
playing = 1

while TicTacToe.playing(board):
    if human == playing:
        result = minimax(human,1)
        print(result)
        row = (input('move row'))
        col = (input('move col'))
        board[int(row)][int(col)] = human
        playing = -int(playing)
    else:
        result = minimax(-human,0)
        # ai_move = moves[choice]
        # board[ai_move[0]][ai_move[1]] = -human
        board[result[0]][result[1]] = playing
        playing = -playing
        print('ai move')
        print(result)
        print(board)
        print('\n')