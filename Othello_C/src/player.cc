#include "player.h"

struct RandomPlayer : public Player {
    Move choose_move(Board *board, uint64_t legalMoves) override {
        int move_ind;
        vector<Move> moves;
        moves = get_move_indicies(legalMoves);
        int chosen = rand() % moves.size();
        return moves[chosen];
    }
    
    RandomPlayer();
};