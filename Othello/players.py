import random
import numpy as np
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


class SearchFunctions():
    def minimax(old_board,depth,a,b,player,eval_function):
        valid_moves = OthelloEnv.legal_moves(old_board,player)
        if depth == 0 or game.getGameOver():
            return eval_function(game)
        if player == 1:
            value = -math.inf
            for move in valid_moves:
                child = game.board.copy()
                child.make_move(move,player)
                n_score = SearchFunctions.minimax(child,depth-1,a,b,-player)
                if type(n_score) is tuple:
                    n_score = n_score[0]-n_score[1]
                value = max(value,n_score)
                if value > b:
                    break
        else:
            value = math.inf
            for move in valid_moves:
                child = game.board.copy()
                child.make_move(move,player)
                n_score = SearchFunctions.minimax(child,depth-1,a,b,-player)
                if type(n_score) is tuple:
                    n_score = n_score[0]-n_score[1]
                value = max(value,n_score)
                if value < a:
                    break
            return value

class TestPlayer():
    def __init__(self,game,max_depth,order):
        self.game = game
        self.max_depth = max_depth
        self.player = order

    @decoratorTimer(2,'test')
    def play(self):
        board = self.game.board
        moves = OthelloEnv.legal_moves(board,self.player)
        num_moves = abs(np.sum(moves))
        scores = np.zeros_like(board)
        if num_moves == 0:
            return (-1,-1)
        p = np.where(moves == self.player)
        for i in range(num_moves):
            board_temp = OthelloEnv.make_move(board,(p[0][i],p[1][i]),self.player)
            n_score = SearchFunctions.minimax(board_temp,self.max_depth,-math.inf,math.inf,self.player)
            if n_score == 0:
                n_score = 1
            scores[p[0][i]][p[1][i]] = n_score
        scores = scores.flatten()
        scores = scores[scores.astype(bool)]
        if self.player == 1:
            fin_score = -65
        else:
            fin_score = 65
        for i in range(num_moves):
            if self.player == 1:
                if scores[i] >= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
            else:
                if scores[i] <= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
        return move

class RandomPlayer():
    def __init__(self,game,order):
        self.game = game
        self.player = order

    def play(self):
        p = np.where(self.game.legal_moves(self.player) == self.player)
        num_moves = abs(np.sum(self.game.moves))
        if num_moves == 0:
            return (-1,-1)
        move_ind = random.randint(0,num_moves-1)
        move = (p[0][move_ind],p[1][move_ind])
        return move

class ab_ScoreSearch():
    def __init__(self,game,depth_max,order):
        self.game = game
        self.max_depth = depth_max
        self.player = order

    @decoratorTimer(2,'ab_scoreSearch')
    def play(self):
        internal_game = OthelloEnv()
        num_moves = np.count_nonzero(self.game.legal_moves(self.player))
        board = self.game.board.copy()
        scores = np.zeros_like(board)
        if num_moves == 0:
            return (-1,-1)
        p = np.where(self.game.legal_moves(self.player) == self.player)
        for i in range(num_moves):
            internal_game.board[p[0][i]][p[1][i]] = self.player
            scores[p[0][i]][p[1][i]] = ab_ScoreSearch.alpha_beta_score(self,internal_game,self.max_depth,-math.inf,math.inf,self.player)
            internal_game.board[p[0][i]][p[1][i]] = 0
        scores = scores.flatten()
        scores = scores[scores.astype(bool)]
        if self.player == 1:
            fin_score = -65
        else:
            fin_score = 65
        for i in range(len(scores)):
            if self.player == 1:
                if scores[i] >= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
            else:
                if scores[i] <= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
        return move
    
    def alpha_beta_score(self,game,depth,a,b,player):
        valid_moves = game.legal_moves(player)
        if depth == 0 or game.getGameOver():
            piece_score = game.score_board()
            return piece_score[0]-piece_score[1]
        if player == 1:
            value = -math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,player)
                n_score = ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player)
                if type(n_score) is tuple:
                    n_score = n_score[0]-n_score[1]
                value = max(value,n_score)
                if value > b:
                    break
            return value
        else:
            value = math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,player)
                n_score = ab_ScoreSearch.alpha_beta_score(self,child,depth-1,a,b,-player)
                if type(n_score) is tuple:
                    n_score = n_score[0]-n_score[1]
                value = min(value,n_score)
                if value < a:
                    break
                return value
            
class minMobility(): #tries to minimize opponent's moves
    def __init__(self,game,order):
        self.game = game
        self.internal_game = OthelloEnv()
        self.player = order

    @decoratorTimer(2,'minMobility')
    def play(self,game):
        num_moves = abs(np.sum(game.moves))
        board = game.board.copy()
        scores = np.zeros_like(board)
        if num_moves == 0:
            return (-1,-1)
        p = np.where(game.moves == self.player)
        for i in range(num_moves):
            self.internal_game.board[p[0][i]][p[1][i]] = self.player
            n_score = minMobility.mobility_score(self,self.internal_game,6,-math.inf,math.inf,self.player)
            if n_score == 0:
                n_score = 1
            scores[p[0][i]][p[1][i]] = n_score
        scores = scores.flatten()
        scores = scores[scores.astype(bool)]
        print("mobility for ", str(self.player))
        print(scores)
        print('\n')
        if self.player == 1:
            fin_score = -65
        else:
            fin_score = 65
        if num_moves == 0:
            return (-1,-1)
        for i in range(num_moves):
            if self.player == 1:
                if scores[i] >= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
            else:
                if scores[i] <= fin_score:
                    fin_score = scores[i]
                    move = (p[0][i],p[1][i])
        return move
        
    def mobility_score(self,game,depth,a,b,player):
        valid_moves = game.legal_moves(player)
        if depth == 0 or game.getGameOver():
            return np.count_nonzero(valid_moves)
        if self.player == 1:
            value = -math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,self.player)
                value = max(value,minMobility.mobility_score(self,child,depth-1,a,b,-player))
                if value > b:
                    break
            return value
        else:
            value = math.inf
            for move in valid_moves:
                child = OthelloEnv()
                child.board = game.board.copy()
                child.make_move(move,self.player)
                value = min(value,minMobility.mobility_score(self,child,depth-1,a,b,-player))
                if value < a:
                    break
                return value


##
class HeuristicPlayer():
    def __init__(self,game,order):
        self.game = game
        self.player = order
        self.static_weights = np.array(([4,-3,2,2,2,2,-3,4],[-3,-4,-1,-1,-1,-1,-4,-3],[2,-1,1,0,0,1,-1,2],[2,-1,0,1,1,0,-1,2],[2,-1,0,1,1,0,-1,2],[2,-1,1,0,0,1,-1,2],[-3,-4,-1,-1,-1,-1,-4,-3],[4,-3,2,2,2,2,-3,4]))

class NegScout():
    def __init__(self,game):
        self.game = game

class HandMade():
    def __init__(self,game):
        self.game = game
        #bitboards (hex)
        self.x_squares = 0x42000000004200
        self.a_squares = 0x2400810000810024
        self.b_sqaures = 0x1800008181000018
        self.c_squares = 0x4281000000008142
        self.corners = 0x8100000000000081

    def np_to_hex(board):
        pass

    def play(self, game):
        valid_moves = game.legal_moves(self.player)
        

    def get_best(self,game):
        pass

    def combine(self,moves):
        moves = HandMade.np_to_hex(moves)


    def bias_x(self,game,player):
        pass

    def bias_a(self,game,player):
        pass

    def bias_b(self,game,player):
        pass

    def bias_c(self,game,player):
        pass
    

class symmLR():
    def __init__(self,game):
        self.game = game
    
    @decoratorTimer(2,'symm_LR')
    def play(self,game,player):
        pass

    def evaluate_symmetry(game):
        pass

# symmetric player, player based on other game (hex? ie try to make route from one side of board to another)
# longest road player? snake player? alphabetical player (use standard coords of othello board to rank)
# lexicographical player?