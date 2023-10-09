#include <string.h>
#include <stdbool.h>

struct move
{
    int row;
    int col;
};

bool has_won(int board[3][3], int player);
bool has_drawn(int board[3][3]);
int score(board);

struct move* get_all_moves(board);