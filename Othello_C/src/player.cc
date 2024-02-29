
#include"player.h"
#include<cstdlib>
#include<iostream>
#include<random>


struct RandomPlayer : public Player {
    mt19937_64 gen{random_device()()};
    uniform_real_distribution<double> dis{0,64};
    Move* choose_move(Board *board, vector<Move*> legalMoves) override {
        int random = dis(gen);
        int chosen = random % legalMoves.size();
        return legalMoves[chosen];
    }
    
};

Player* Random(){
    return new RandomPlayer;
};