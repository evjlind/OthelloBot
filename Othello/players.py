import random
import numpy as np
from numpy import inf
from othello import OthelloEnv
import math
import time

def decoratorTimer(decimal,func):
    def decoratorFunc(f):
        def wrap(*args,**kwargs):
            time1 = time.monotonic()
            result = f(*args,**kwargs)
            time2 = time.monotonic()
            print('{:s} {:s} function took {:.{}f} ms'.format(func,f.__name__, ((time2-time1)*1000.0), decimal ))
            return result
        return wrap
    return decoratorFunc

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


    # @decoratorTimer(2,'ab_scoreSearch')
    def play(self,game,player):
        internal_game = OthelloEnv()
        legal_moves = game._legal_moves(player)
        num_moves = np.count_nonzero(legal_moves)
        internal_game.board = game.board.copy()
        scores = np.zeros(num_moves)
        legal_move_locations = np.where(legal_moves==player)
        actual_locations = []
        for i in range(num_moves):
            actual_locations.append((legal_move_locations[0][i],legal_move_locations[1][i]))
        if player == 1:
            fin_score = -65
        else:
            fin_score = 65
        if num_moves == 0:
            return (-1,-1)
        for i in range(num_moves):
            internal_game.make_move(actual_locations[i],player)
            evaluation = ab_ScoreSearch.alpha_beta_score(self,internal_game,3,-inf,inf,-player)
            scores[i] = evaluation
            internal_game.board = game.board.copy()
        scores[np.isneginf(scores)] = fin_score
        scores[np.isinf(scores)] = fin_score
        if num_moves == 0:
            return (-1,-1)
        # print(scores)
        for i in range(num_moves):
            if player == 1:
                if scores[i] >= fin_score:
                    fin_score = scores[i]
                    move = actual_locations[i]
            else:
                if scores[i] <= fin_score:
                    fin_score = scores[i]
                    move = actual_locations[i]
        return move
        
    def alpha_beta_score(self,game,depth,a,b,player):
        if depth == 0 or game.getGameOver():
            total_score = game.score_board()
            return total_score[0]-total_score[1]
        valid_moves = game._legal_moves(player)
        legal_move_locations = np.where(valid_moves==player)
        num_moves = np.count_nonzero(valid_moves)
        actual_locations = []
        for i in range(num_moves):
            actual_locations.append((legal_move_locations[0][i],legal_move_locations[1][i]))
        if player == 1:
            value = -inf
            for i in range(num_moves):
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(actual_locations[i],player)
                n_score = ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player)
                if type(n_score) is tuple:
                    n_score = n_score[0]-n_score[1]
                value = max(value,n_score)
                if value > b:
                    break
            return value
        else:
            value = inf
            for i in range(num_moves):
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(actual_locations[i],player)
                n_score = ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player)
                if type(n_score) is tuple:
                    n_score = n_score[0]-n_score[1]
                value = min(value,n_score)
                if value < a:
                    break
            return value
            

# class minMobility(): #tries to minimize opponent's moves, interesting because not zero-sum
#     def __init__(self,game):
#         self.game = game
#         self.internal_game = OthelloEnv()

#     @decoratorTimer(2,'minMobility')
#     def play(self,game,player):
#         num_moves = abs(np.sum(game.moves))
#         board = game.board.copy()
#         scores = np.zeros_like(board)
#         if num_moves == 0:
#             return (-1,-1)
#         p = np.where(game.moves == player)
#         for i in range(num_moves):
#             self.internal_game.board[p[0][i]][p[1][i]] = player
#             n_score = minMobility.mobility_score(self,self.internal_game,6,-inf,inf,player)
#             if n_score == 0:
#                 n_score = 1
#             scores[p[0][i]][p[1][i]] = n_score
#         scores = scores.flatten()
#         scores = scores[scores.astype(bool)]
#         print("mobility for ", str(player))
#         print(scores)
#         print('\n')
#         if player == 1:
#             fin_score = -65
#         else:
#             fin_score = 65
#         if num_moves == 0:
#             return (-1,-1)
#         for i in range(num_moves):
#             if player == 1:
#                 if scores[i] >= fin_score:
#                     fin_score = scores[i]
#                     move = (p[0][i],p[1][i])
#             else:
#                 if scores[i] <= fin_score:
#                     fin_score = scores[i]
#                     move = (p[0][i],p[1][i])
#         return move
        
#     def mobility_score(self,game,depth,a,b,player):
#         valid_moves = game._legal_moves(player)
#         if depth == 0 or game.getGameOver():
#             return np.count_nonzero(valid_moves)
#         if player == 1:
#             value = -inf
#             for move in valid_moves:
#                 child = OthelloEnv()
#                 child.board = game.board.copy()
#                 child.make_move(move,player)
#                 value = max(value,minMobility.mobility_score(self,child,depth-1,a,b,-player))
#                 if value > b:
#                     break
#             return value
#         else:
#             value = inf
#             for move in valid_moves:
#                 child = OthelloEnv()
#                 child.board = game.board.copy()
#                 child.make_move(move,player)
#                 value = min(value,minMobility.mobility_score(self,child,depth-1,a,b,-player))
#                 if value < a:
#                     break
#                 return value

# class NegScout():
#     def __init__(self,game):
#         self.game = game

class HandMade():
    def __init__(self,game):
        self.game = game
        #bitboards (hex)
        self.x_squares = 0x42000000004200
        self.a_squares = 0x2400810000810024
        self.b_sqaures = 0x1800008181000018
        self.c_squares = 0x4281000000008142
        self.corners = 0x8100000000000081

    # find a better definition for an endgame
    def is_endgame(self,game):
        if game.num_moves>49:
            return True
        else:
            return False

    def board_to_ints(board):
        n_board = board.flatten()
        p1_value = 0
        p2_value = 0
        for i in range(len(n_board)):
            if n_board[i] == 1:
               p1_value += (64-i)**2
            if n_board[i] == -1:
               p2_value += (64-i)**2
        return p1_value,p2_value
        
    # might not end up using this 
    def hex_to_np(hex_value):
        bin_value = bin(hex_value)
        pass

    def play(self, game, player):
        valid_moves = game._legal_moves(player)
        

    def bias_x(self,game,player):
        pass

    def bias_a(self,game,player):
        pass

    def bias_b(self,game,player):
        pass

    def bias_c(self,game,player):
        pass
    
    def evaluate(self,game,player):
        pass

# class symmLR():
#     def __init__(self,game):
#         self.game = game
    
#     @decoratorTimer(2,'symm_LR')
#     def play(self,game,player):
#         pass

#     def evaluate_symmetry(game):
#         pass

# # symmetric player, player based on other game (hex? ie try to make route from one side of board to another)
# # longest road player? snake player? alphabetical player (use standard coords of othello board to rank)
# # lexicographical player?

