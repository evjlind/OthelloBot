from othello import OthelloEnv
from players import *
# import math

game = OthelloEnv()

# p1 = ab_ScoreSearch(game)
# p2 = ab_ScoreSearch(game)

# print(p1.play(game,1))

p1_int, p2_int = HandMade.board_to_ints(game.board)

print(p1_int)
print(hex(p1_int))