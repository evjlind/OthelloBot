#include<iostream>
#include<vector>
#include"othello.h"

using namespace std;

int main(){
    // clock_t tic = clock();
    uint64_t moves;
    Board *board = new_board();
    print_board(board,true);
    moves = generate_moves(board,1);
    vector<Move> move_vect = get_move_indicies(moves);
    // clock_t toc = clock();

    return 0;
}