import functools
import numpy as np

class OthelloEnv():
    metadata = {"name": "othelloEnv_v1"}

    def __init__(self):

        self.possible_agents = ["player_"+ str(r) for r in range(2)]
        self.agent_name_mapping = dict(
            zip(self.possible_agents, list(range(len(self.possible_agents))))
        )
        
        board = np.zeros((8,8),dtype=int)
        board[3][3]=1
        board[3][4]=-1
        board[4][3]=-1
        board[4][4]=1

        return board

    def reset(self, board):
        board = np.zeros((8,8),dtype=int)
        board[3][3]=1
        board[3][4]=-1
        board[4][3]=-1
        board[4][4]=1
        winner = False
        return 0

    def disp_board(self):
        pass
    
    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        pass

    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        pass
    
    def _legal_moves(self,board,player):
        coords = [(i,j) for i in range(8) for j in range(8) if board[i][j] == player]
        legal_moves = []
        #player 2 =  black, player 1 = white
        other_p = -player
        for m in coords:
            i=m[0]
            j=m[1]
            n=1
            if (i)<=6:
                if board[i+n][j] == other_p: 
                    while (i+n)<=7:
                        if board[i+n][j] == other_p: 
                            n=n+1
                        elif board[i+n][j] == player:
                            n=999
                        elif board[i+n][j] == 0:
                            legal_moves.append((i+n,j))
                            n=999
            n=1
            if i>=1:
                if board[i-n][j] == other_p: 
                    while (i-n)>=0:
                        if board[i-n][j] == other_p: 
                            n=n+1
                        elif board[i-n][j] == player:
                            n=999
                        elif board[i-n][j] == 0:
                            legal_moves.append((i-n,j))
                            n=999
            n=1
            if j<=6:
                if board[i][j+n] == other_p: 
                    while (j+n)<=7:
                        if board[i][j+n] == other_p: 
                            n=n+1
                        elif board[i][j+n] == player:
                            n=999
                        elif board[i][j+n] == 0:
                            legal_moves.append((i,j+n))
                            n=999
            n=1
            if j>=1:
                if board[i][j-n] == other_p: 
                    while (j-n)>=0:
                        if board[i][j-n] == other_p: 
                            n=n+1
                        elif board[i][j-n] == player:
                            n=999
                        elif board[i][j-n] == 0:
                            legal_moves.append((i,j-n))
                            n=999
            n=1
            if i<=6 and j<=6:
                if board[i+n][j+n] == other_p:
                    while(i+n<=7 and j+n<=7):
                        if board[i+n][j+n] == other_p:
                            n=n+1
                        elif board[i+n][j+n] == player:
                            n=999
                        else:
                            legal_moves.append((i+n,j+n))
                            n=999
            n=1
            if i<=6 and j>=0:
                if board[i+n][j-n] == other_p:
                    while (i+n<=7 and j-n>=0):
                        if board[i+n][j-n] == other_p:
                            n=n+1
                        elif board[i+n][j-n] == player:
                            n=999
                        else:
                            legal_moves.append((i+n,j-n))
                            n=999
            n=1
            if i>=0 and j<=7:
                if board[i-n][j+n] == other_p:
                    while ((i-n)>=0 and (j+n)<=7):
                        if board[i-n][j+n] == other_p:
                            n=n+1
                        elif board[i-n][j+n] == player:
                            n=999
                        else:
                            legal_moves.append((i-n,j+n))
                            n=999
            n=1
            if i>=0 and j>=0:
                if board[i-n][j-n] == other_p:
                    while ((i-n)>=0 and (j-n)>=0):
                        if board[i-n][j-n] == other_p:
                            n=n+1
                        elif board[i-n][j-n] == player:
                            n=999
                        else:
                            legal_moves.append((i-n,j-n))
                            n=999
        if len(legal_moves==0):
            winner = True
        return legal_moves
    
    def make_move(self, move, player):
        pass

    def has_legal_move(self, player, board):
        pass

    def getGameOver(self, board):
        pass
        
    