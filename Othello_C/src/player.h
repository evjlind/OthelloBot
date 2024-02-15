
#ifndef _PLAYER_H
#define _PLAYER_H
#include "othello.h"

struct Player{
    virtual Move* choose_move(Board *board, vector<Move*> legalMoves){
        Move *move;
        return move;
    }

    Board* pass_turn(Board *board){
        int turn = board->turn;
        turn++;
        board->turn = turn;
        return board;
    }

    virtual ~Player() {};
};

Player *Random();

#endif