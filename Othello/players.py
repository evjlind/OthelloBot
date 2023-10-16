import random
import numpy as np
from othello import OthelloEnv
import math

class RandomPlayer():
    def __init__(self,game):
        self.game = game

    def play(self,game,player):
        p = np.where(game.moves == player)
        num_moves = abs(np.sum(game.moves))
        if num_moves == 0:
            return (-1,-1)
        move_ind = random.randint(0,num_moves-1)
        move = (p[0][move_ind],p[1][move_ind])
        return move

class ab_ScoreSearch():
    def __init__(self,game):
        self.game = game

    def play(self,game,player):
        internal_game = OthelloEnv()
        num_moves = abs(np.sum(game.moves))
        board = game.board.copy()
        scores = np.zeros_like(board)
        if num_moves == 0:
            return (-1,-1)
        p = np.where(game.moves == player)
        for i in range(num_moves):
            internal_game.board[p[0][i]][p[1][i]] = player
            scores[p[0][i]][p[1][i]] = ab_ScoreSearch.alpha_beta_score(self,internal_game,5,-math.inf,math.inf,player)
            internal_game.board[p[0][i]][p[1][i]] = 0
        print(scores)
        scores = scores.flatten()
        scores = scores[scores.astype(bool)]
        print(scores)
        if player == 1:
            fin_score = -65
        else:
            fin_score = 65
        if num_moves == 0:
            return (-1,-1)
        for i in range(num_moves):
            if player == 1:
                if scores[i] >= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
            else:
                if scores[i] <= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
        return move
        
    def alpha_beta_score(self,game,depth,a,b,player):
        valid_moves = game._legal_moves(player)
        if depth == 0 or game.getGameOver():
            return game.score_board()
        if player == 1:
            value = -math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,player)
                value = max(value,ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player))
                if value > b:
                    break
            return value
        else:
            value = math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,player)
                value = min(value,ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player))
                if value < a:
                    break
                return value
            

class ab_Mobility():
    def __init__(self,game):
        self.game = game

    def play(self,game,player):
        internal_game = OthelloEnv()
        num_moves = abs(np.sum(game.moves))
        board = game.board.copy()
        scores = np.zeros_like(board)
        if num_moves == 0:
            return (-1,-1)
        p = np.where(game.moves == player)
        for i in range(num_moves):
            internal_game.board[p[0][i]][p[1][i]] = player
            scores[p[0][i]][p[1][i]] = ab_ScoreSearch.alpha_beta_score(self,internal_game,5,-math.inf,math.inf,player)
            internal_game.board[p[0][i]][p[1][i]] = 0
        scores = scores.flatten()
        if player == 1:
            fin_score = -65
        else:
            fin_score = 65
        if num_moves == 0:
            return (-1,-1)
        for i in range(num_moves):
            if player == 1:
                if scores[i] >= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
            else:
                if scores[i] <= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
        return move
        
    def alpha_beta_score(self,game,depth,a,b,player):
        valid_moves = game._legal_moves(player)
        if depth == 0 or game.getGameOver():
            return game._legal_moves(player)
        if player == 1:
            value = -math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,player)
                value = max(value,ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player))
                if value > b:
                    break
            return value
        else:
            value = math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,player)
                value = min(value,ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player))
                if value < a:
                    break
                return value


class NegScout():
    def __init__(self,game):
        self.game = game
# symmetric player, player based on other game (hex? ie try to make route from one side of board to another)
# longest road player? snake player? alphabetical player (use standard coords of othello board to rank)
# lexicographical player?