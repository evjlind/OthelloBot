#include<iostream>
#include<vector>
#include"othello.h"
#include"player.h"

using namespace std;

int main(){
    // clock_t tic = clock();
    Board *board = new_board();
    print_board(board,true);
    uint64_t moves = generate_moves(board,1);
    vector<Move> move_vect = get_move_indicies(moves);
    disp_move_vect(move_vect);
    // clock_t toc = clock();

    return 0;
}