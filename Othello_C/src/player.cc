
#include "player.h"

struct RandomPlayer : public Player {
    Move* choose_move(Board *board, vector<Move*> legalMoves) override {
        int chosen = rand() % legalMoves.size();
        return legalMoves[chosen];
    }
    
};

Player* Random(){
    return new RandomPlayer;
};