import cProfile
from othello import OthelloEnv
from players import *
from play_othello import play_game

game = OthelloEnv()
p1 = ab_ScoreSearch(game)
p2 = RandomPlayer(game)

if __name__ == "__main__":
    cProfile.run('play_game(game,p1,p2)')