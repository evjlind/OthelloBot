#include<stdio.h>
#include<stdbool.h>
#include<string.h>
#include<stdlib.h>
#include "othello.h"

// could represent a board as 128 bit binary sequence but doing this for now
struct board* new_board(){
    unsigned long long white = INIT_BOARD_WHITE;
    unsigned long long black = INIT_BOARD_BLACK;
    struct board* new_board = (struct board*)malloc(sizeof(struct board));
    new_board->white = white;
    new_board->black = black;
    new_board->turn = 0;
    return new_board;
}
unsigned long long shift_r(unsigned long long board){
    return (board&R_MASK)>>1;
}

unsigned long long shift_l(unsigned long long board){
    return (board&L_MASK)<<1;
}

unsigned long long shift_d(unsigned long long board){
    return board>>8;
}

unsigned long long shift_u(unsigned long long board){
    return board<<8;
}

unsigned long long shift_u_r(unsigned long long board){
    return shift_u(shift_r(board));
}

unsigned long long shift_u_l(unsigned long long board){
    return shift_u(shift_l(board));
}

unsigned long long shift_d_r(unsigned long long board){
    return shift_d(shift_r(board));
}

unsigned long long shift_d_l(unsigned long long board){
    return shift_d(shift_l(board));
}

unsigned long long generate_moves(struct board *board,int player){
    unsigned long long self;
    unsigned long long op;
    if (player==1){
        self = board->black;
        op = board->white;
    }
    else{
        self = board->white;
        op = board->black;
    }
    unsigned long long moves = 0;
    unsigned long long open = ~(self|op);
    unsigned long long captured;
    
    //up
    captured = shift_u(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_u(captured)&op;
    }
    moves |= shift_u(captured) & open;

    //down
    captured = shift_d(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_d(captured)&op;
    }
    moves |= shift_d(captured) & open;
    
    //right
    captured = shift_r(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_r(captured)&op;
    }
    moves |= shift_r(captured) & open;

    //left
    captured = shift_l(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_l(captured)&op;
    }
    moves |= shift_l(captured) & open;

    //up + r
    captured = shift_u_r(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_u_r(captured)&op;
    }
    moves |= shift_u_r(captured) & open;
    
    //up + l
    captured = shift_u_l(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_u_l(captured)&op;
    }
    moves |= shift_u_l(captured) & open;
    
    //down + r
    captured = shift_d_r(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_d_r(captured)&op;
    }
    moves |= shift_d_r(captured) & open;

    //down + l
    captured = shift_d_l(self)&op;
    for (int i=0; i<5;i++){
        captured |= shift_d_l(captured)&op;
    }
    moves |= shift_d_l(captured) & open;

    return moves;
}

struct board* make_move(unsigned long long move, struct board *board, unsigned long long legalMoves){
    int turn = board->turn;
    unsigned long long self, op;
    unsigned long long captured;
    unsigned long long overlap = move&legalMoves;
    if (turn % 2 == 0){
        self = board->black;
        op = board->white;
    }
    else{
        self = board->white;
        op = board->black;
    }

    if (overlap>0){
        self |= move;
        captured = shift_u(move)&op;
        printf("\n%llu",self);
        printf("\n%llu\n",op);
        for (int i=0;i<5;i++){
            captured |= shift_u(captured)&op;
        }
        // if (shift_u(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        captured = shift_d(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d(captured)&op;
        }
        // if (shift_d(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        captured = shift_r(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_r(captured)&op;
        }
        // if (shift_r(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        captured = shift_l(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_l(captured)&op;
        }
        // if (shift_l(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }


        captured = shift_u_r(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u_r(captured)&op;
        }
        // if (shift_u_r(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        captured = shift_u_l(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u_l(captured)&op;
        }
        // if (shift_u_l(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        captured = shift_d_r(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d_r(captured)&op;
        }
        // if (shift_d_r(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        captured = shift_d_l(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d_l(captured)&op;
        }
        // if (shift_d_l(captured)&self!=0){
        self |= captured;
        op &= ~captured;
        // }

        if (turn % 2 == 0){
            board->black = self;
            board->white = op;
        }
        else{
            board->white = self;
            board->black = op;
        }
        turn++;
        board->turn = turn;

        return board;
    }
    else{
        printf("\n\nInvalid Move\n\n");
        return NULL;
    }
}

bool game_over(struct board *board, bool black_pass, bool white_pass){
    return (board->white|board->black == FULL)|| (board->white == 0 || board->black == 0) || (black_pass&white_pass);
}

void print_board(struct board *board, bool withMoves){
    char show[1024] = "  A B C D E F G H\n1 ";
    unsigned long long white = board->white;
    unsigned long long black = board->black;
    int turn = board->turn;
    char w[5] = "W ";
    char b[5] = "B ";
    char none[5] = "_ ";
    char move[5] = "x ";
    unsigned long long moves;
    char *specialSpace = malloc(25);
    char buffer[10];
    int row = 2;
    if (withMoves == true){
        if (turn%2==0){
            moves = generate_moves(board,1);
        }
        else{
            moves = generate_moves(board,-1);
        }
    }
    for (int i=63;i>=0;i--){
        if (withMoves == true && (moves>>i&1)>0){
            strcat(show,move);
        }
        else if ((white>>i & 1)>0){
            strcat(show,w);
        }
        else if ((black>>i & 1)>0){
            strcat(show,b);
        }
        
        else{
            strcat(show,none);
        }
        if (i%8 == 0 && i>1){
            sprintf(buffer,"\n%d ",row);
            strcat(show,buffer);
            row++;
        }
    }
    printf("%s",show);
}

unsigned long long coord_to_move(char move[5]){
    return 0x0;
}