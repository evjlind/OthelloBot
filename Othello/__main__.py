import cProfile
from othello import OthelloEnv
from players import *
from play_othello import play_game

game = OthelloEnv()
p1 = ab_ScoreSearch(game,3,1)
p2 = RandomPlayer(game,-1)

if __name__ == "__main__":
    cProfile.run('play_game(game,p1,p2)')