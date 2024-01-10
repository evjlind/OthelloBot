#include<stdio.h>
#include<stdbool.h>
#include<string.h>
#include<stdlib.h>
#include"othello.h"
#include"players.h"

int main(){
    struct board *board = new_board();
    print_board(board,true);
}