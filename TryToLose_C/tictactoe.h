#include <string.h>
#include<bool.h>

struct board 
{
    int board[3][3];
    int depth;
};

struct move
{
    int row;
    int col;
};

bool has_won(board,player);
bool has_drawn(board)
int score(board);

struct move[] get_all_moves(board);