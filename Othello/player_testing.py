from othello import OthelloEnv
from players import *
import math

game = OthelloEnv()

p1 = ab_ScoreSearch(game)
p2 = ab_ScoreSearch(game)

print(p1.play())