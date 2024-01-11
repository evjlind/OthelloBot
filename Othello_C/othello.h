#include<stdio.h>
#include<stdbool.h>
#include<string.h>
#include<stdlib.h>
#define INIT_BOARD_BLACK 0x810000000ULL
#define INIT_BOARD_WHITE 0x1008000000ULL
#define R_MASK 0xfefefefefefefefeULL
#define L_MASK 0x7f7f7f7f7f7f7f7fULL
#define FULL 0xffffffffffffffffULL

struct board{
    int turn;
    unsigned long long white;
    unsigned long long black;
};

struct board* new_board();
unsigned long long shift_r(unsigned long long board);
unsigned long long shift_l(unsigned long long board);
unsigned long long shift_u(unsigned long long board);
unsigned long long shift_d(unsigned long long board);
unsigned long long shift_u_r(unsigned long long board);
unsigned long long shift_u_l(unsigned long long board);
unsigned long long shift_d_r(unsigned long long board);
unsigned long long shift_d_l(unsigned long long board);
unsigned long long generate_moves(struct board *board,int player);
struct board* make_move(unsigned long long move, struct board *board, unsigned long long legalMoves);
bool game_over(struct board *board, bool black_pass, bool white_pass);
void print_board(struct board *board, bool withMoves);
unsigned long long coord_to_move(char move[5]);