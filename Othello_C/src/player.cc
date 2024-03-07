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

struct HumanPlayer : public Player {
    Move* choose_move(Board *board, vector<Move*> legalMoves) override {
        string input_move;
        uint64_t move_val;
        while(1){
        cout << "Choose a move:" << endl;
        cin >> input_move;
        for (int i=0;i<legalMoves.size();i++){
            if (input_move == legalMoves[i]->m_name){
                return legalMoves[i];
            }
        }
        cout << "Illegal Move" << endl;
    }
}};

Player* Random(){
    return new RandomPlayer;
};

Player* Human(){
    return new HumanPlayer;
};

