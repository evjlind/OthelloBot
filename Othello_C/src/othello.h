#include<cstdint>
#include<string>
#include<vector>
#define INIT_BOARD_BLACK 0x810000000ULL
#define INIT_BOARD_WHITE 0x1008000000ULL
#define R_MASK 0xfefefefefefefefeULL
#define L_MASK 0x7f7f7f7f7f7f7f7fULL
#define FULL 0xffffffffffffffffULL

using namespace std;

struct board{
    int turn;
    uint64_t white;
    uint64_t black;
    uint64_t moves;
};

struct game{
    int winner;
    char moves[512];
};

struct Move{
    int src_row = 0, src_col = 0;
    string m_name;
};

struct game* play_game(int player1,int player2);
struct board* new_board();
uint64_t shift_r(uint64_t board);
uint64_t shift_l(uint64_t board);
uint64_t shift_u(uint64_t board);
uint64_t shift_d(uint64_t board);
uint64_t shift_u_r(uint64_t board);
uint64_t shift_u_l(uint64_t board);
uint64_t shift_d_r(uint64_t board);
uint64_t shift_d_l(uint64_t board);
uint64_t generate_moves(struct board *board,int player);
struct board* make_move(uint64_t move, struct board *board, uint64_t legalMoves);
bool game_over(struct board *board, bool black_pass, bool white_pass);
void print_board(struct board *board, bool withMoves);
string move_to_coord(Move move);
Move coord_to_move(string move);
vector<Move> get_move_indicies(uint64_t moves);