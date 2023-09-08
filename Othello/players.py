import numpy as np

class RandomPlayer():
    def __init__(self,game):
        self.game = game
        
    def play(self,board):
        legal_moves = self.game._legalMoves()
        a = legal_moves[np.random.randint(len(legal_moves))-1]
        return a