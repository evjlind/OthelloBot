import functools

import gymnasium as gym
import numpy as np
from gymnasium.spaces import box, discrete
from gymnasium.utils import EzPickle

from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers

class CustomEnvironment(AECEnv):
    metadata = {
        "name": "custom_environment_v0",
    }


    def __init__(self):
        global board, winner
        self.possible_agents = ["player_"+ str(r) for r in range(2)]
        self.agent_name_mapping = dict(
            zip(self.possible_agents, list(range(len(self.possible_agents))))
        )
        
        self.action_spaces = box(low=0,high=7,shape=(8,8), dtype=np.float32)
        board = np.zeros((8,8),dtype=int)
        board[3][3]=1
        board[3][4]=2
        board[4][3]=2
        board[4][4]=1
        winner = False

    def reset(self, seed=None, options=None):
        global board, legal_moves, winner
        board = np.zeros((8,8),dtype=int)
        board[3][3]=1
        board[3][4]=2
        board[4][3]=2
        board[4][4]=1
        legal_moves = []
        winner = False
        return 0

    def step(self, actions, player):
        global board
        board[actions[0],actions[1]] = player
        return 0

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]
    
    def _legal_moves(self,player):
        global board, winner
        coords = [(i,j) for i in range(8) for j in range(8) if board[i][j] == player]
        legal_moves = []
        #player 2 =  black, player 1 = white
        other_p = 1 if player == 2 else 2
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