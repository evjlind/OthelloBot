#include"othello.h"
#include"player.h"
#include"random_player.h"

using namespace std;

int main(){
    // clock_t tic = clock();
    struct board *board = new_board();
    print_board(board,true);
    // clock_t toc = clock();
    // struct board *new_board;
    // printf("\nElapsed %f seconds\n",(double)(toc-tic)/CLOCKS_PER_SEC);
    // unsigned long long move = 0x2000000000ULL;
    // unsigned long long legalMoves = generate_moves(board,1);
    // // printf("\n%llu\n",legalMoves);
    // // printf("%llu\n",move);
    // new_board = make_move(move,board,legalMoves);
    // if (new_board != NULL){
    //     board = new_board;
    // }
    // print_board(board,true);
    return 0;
}