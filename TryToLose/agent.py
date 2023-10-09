from tictactoe import TicTacToe
import numpy as np
import math

class agent():
    def score_move(board,move,depth,turn,a,b):
        next_board = agent.make_move(board,move,turn)
        score = agent.alpha_beta(next_board,depth-1,a,b,-turn)
        return score

    def make_move(board,move,turn):
        new_board = board.copy()
        new_board[move[0]][move[1]] = turn
        return new_board
    
    def alpha_beta(board,depth,a,b,turn):
        valid_moves = TicTacToe.get_all_moves(board)
        if depth == 0 or (not TicTacToe.playing(board)):
            return TicTacToe.score(board)
        if turn == 1:
            value = -math.inf
            for move in valid_moves:
                child = agent.make_move(board,move,turn)
                value = max(value,agent.alpha_beta(child,depth-1,a,b,-turn))
                if value > b:
                    break
            return value
        else:
            value = math.inf
            for move in valid_moves:
                child = agent.make_move(board,move,turn)
                value = min(value,agent.alpha_beta(child,depth-1,a,b,-turn))
                if value < a:
                    break
            return value