#ifndef _PLAYER_H
#define _PLAYER_H
#include "othello.h"

struct Player{
    virtual Move choose_move(Board *board, uint64_t legalMoves){
        Move move;
        return move;
    }

    virtual ~Player() {};
};

Player *Random();

#endif