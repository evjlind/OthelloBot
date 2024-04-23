from othello import OthelloEnv
from players import RandomPlayer
from play_othello import play_game
import pandas as pd

num_games = 1000
p1_wins = 0
p2_wins = 0
draws = 0
score_total = 0
p1_avg_win_score = 0
p2_avg_win_score = 0

game = OthelloEnv()

p1 = RandomPlayer(game)
p2 = RandomPlayer(game)

for i in range(num_games):
    score= play_game(game,p1,p2)
    moves = score[1]
    score = score[0]
    if score[0]>score[1]:
        p1_wins += 1
        p1_avg_win_score += score[0]
    elif score[0]<score[1]:
        p2_wins += 1
        p2_avg_win_score += score[1]
    else:
        draws += 1
    game.reset()

df = pd.DataFrame([{p1_wins},{p2_wins},{draws},{p1_avg_win_score/num_games},{p2_avg_win_score/num_games}])

fname = "randvrand.csv"
df.to_csv(fname,mode='a',index=False,header=False)

print(p1_wins)
print(p2_wins)
print(draws)
print(p1_avg_win_score/num_games)
print(p2_avg_win_score/num_games)