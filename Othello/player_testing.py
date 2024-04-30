from othello import OthelloEnv
from players import *
import math

game = OthelloEnv()

p1 = ab_ScoreSearch(game,4,1)
p2 = ab_ScoreSearch(game,4,-1)

print(p1.play())