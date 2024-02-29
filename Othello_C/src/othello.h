#ifndef _OTHELLO_H
#define _OTHELLO_H

#include<cstdint>
#include<string>
#include<vector>

#define INIT_BOARD_BLACK 0x810000000ULL
#define INIT_BOARD_WHITE 0x1008000000ULL
#define R_MASK 0xfefefefefefefefeULL
#define L_MASK 0x7f7f7f7f7f7f7f7fULL
#define FULL 0xffffffffffffffffULL

using namespace std;

struct Board{
    int turn;
    uint64_t white;
    uint64_t black;
    uint64_t moves;
};

struct Move{
    int src_row = 0, src_col = 0;
    string m_name;
    uint64_t m_value;
};
struct Game{
    int winner;
    vector<Move*> move_hist;
    Board *board;
};

struct Match{
    vector<Game> game_hist;
    int w_wins;
    int b_wins;
    int draws;
};


Board* new_board();
Move* init_move();
Game* init_game();
uint64_t shift_r(uint64_t board);
uint64_t shift_l(uint64_t board);
uint64_t shift_u(uint64_t board);
uint64_t shift_d(uint64_t board);
uint64_t shift_u_r(uint64_t board);
uint64_t shift_u_l(uint64_t board);
uint64_t shift_d_r(uint64_t board);
uint64_t shift_d_l(uint64_t board);
uint64_t generate_moves(Board *board);
Board* make_move(Move *move, Board *board, uint64_t legalMoves);
bool game_over(Board *board);
void print_board(Board *board, bool withMoves);
string move_to_coord(Move *move);
Move* coord_to_move(string move);
uint64_t coord_to_int(Move *move);
vector<Move*> get_move_indicies(uint64_t moves);
void disp_move_vect(vector<Move> moves);
int score_player(uint64_t board);

#endif