#include <string.h>
#include <stdbool.h>

int board= 0x0;
int x = 0x0;
int o = 0x0;
int valid_moves;
bool has_won(int board, int player);
bool has_drawn(int board);
int playing(int board);
int score(int board);
bool play = true;
int player = 1;


int main(){
    while (play == true){
    valid_moves = ~(x|o);

    }
    return 0;
}

int playing(int board){
    switch()
}