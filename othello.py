import functools

import gymnasium as gym
import numpy as np
from gymnasium.spaces import box, discrete
from gymnasium.utils import EzPickle

from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers

def env(render_mode=None):
    internal_render_mode = render_mode if render_mode != "ansi" else "human"
    env = raw_env(render_mode=internal_render_mode)
    # This wrapper is only for environments which print results to the terminal
    if render_mode == "ansi":
        env = wrappers.CaptureStdoutWrapper(env)
    # this wrapper helps error handling for discrete action spaces
    env = wrappers.AssertOutOfBoundsWrapper(env)
    # Provides a wide vareity of helpful user errors
    # Strongly recommended
    env = wrappers.OrderEnforcingWrapper(env)
    return env

def raw_env(render_mode=None):
    """
    To support the AEC API, the raw_env() function just uses the from_parallel
    function to convert from a ParallelEnv to an AEC env
    """
    env = OthelloEnv(render_mode=render_mode)
    return env


class OthelloEnv(AECEnv):
    metadata = {"render_modes": ["human"], "name": "othelloEnv_v1"}

    def __init__(self,render_mode=None):
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

        self.render_mode = render_mode
        return board

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
    
    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        return self.observation_spaces[agent]

    @functools.lru_cache(maxsize=None)
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