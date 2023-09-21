from tictactoe import TicTacToe

def minimax(board,turn,depth):
    if not TicTacToe.playing(board): #defines leaf node
        print('leaf')
        print(board)
        print(TicTacToe.score(board))
        return TicTacToe.score(board)
    moves = TicTacToe.get_all_moves(board)
    new_boards = []
    for i in range((len(moves))):
        bufferBoard = board
        bufferBoard[moves[i][0]][moves[i][1]] = turn
        new_boards.append(bufferBoard)
    print(moves)
    bufferBoard = board
    if turn == 1:
        score = -2
        for i in range(len(new_boards)):
            score = max(score,minimax(new_boards[i],-turn,depth+1))
    else:
        score = 2
        for i in range(len(new_boards)):
            score = min(score,minimax(new_boards[i],-turn,depth+1))
            bufferBoard = board
    if depth == 0:    
        return score

board = TicTacToe.__init__()

human = int(input("human play 1 or -1"))
playing = 1
depth = 0
while TicTacToe.playing(board):
    if human == playing:
        row = (input('move row'))
        col = (input('move col'))
        board[int(row)][int(col)] = human
        playing = -int(playing)
        print(board)
    else:
        moves = TicTacToe.get_all_moves(board)
        choice = minimax(board,-human,depth)
        ai_move = moves[choice]
        board[ai_move[0]][ai_move[1]] = -human
        playing = -playing
        print(board)
print(TicTacToe.score(board))