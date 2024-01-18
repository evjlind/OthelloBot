#include<cstdint>
#include<string>
#include<iostream>
#include<vector>
#include"othello.h"

using namespace std;

//initialize a board in the starting position
struct board* new_board(){
    uint64_t white = INIT_BOARD_WHITE;
    uint64_t black = INIT_BOARD_BLACK;
    struct board* new_board = new board;
    new_board->white = white;
    new_board->black = black;
    new_board->turn = 0;
    return new_board;
}

//shift all pieces right 1 square
uint64_t shift_r(uint64_t board){
    return (board&R_MASK)>>1;
}

//shift all pieces left 1 square
uint64_t shift_l(uint64_t board){
    return (board&L_MASK)<<1;
}

//shift all pieces down 1 square
uint64_t shift_d(uint64_t board){
    return board>>8;
}

//shift all pieces up 1 square
uint64_t shift_u(uint64_t board){
    return board<<8;
}

//shift all pieces up and right 1 square
uint64_t shift_u_r(uint64_t board){
    return shift_u(shift_r(board));
}

//shift all pieces up and left 1 square
uint64_t shift_u_l(uint64_t board){
    return shift_u(shift_l(board));
}

//shift all pieces down and right 1 square
uint64_t shift_d_r(uint64_t board){
    return shift_d(shift_r(board));
}

//shift all pieces down and left 1 square
uint64_t shift_d_l(uint64_t board){
    return shift_d(shift_l(board));
}

//find the legal moves in a given board position (*board) for a given player (player)
uint64_t generate_moves(struct board *board,int player){
    uint64_t self;
    uint64_t op;
    if (player==1){
        self = board->black;
        op = board->white;
    }
    else{
        self = board->white;
        op = board->black;
    }
    uint64_t moves = 0;
    uint64_t open = ~(self|op);
    uint64_t captured;
    
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

//
struct board* make_move(uint64_t move, struct board *board, uint64_t legalMoves){
    int turn = board->turn;
    uint64_t self, op;
    uint64_t captured;
    uint64_t overlap = move&legalMoves;
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
        for (int i=0;i<5;i++){
            captured |= shift_u(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_d(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_r(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_r(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_l(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_l(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_u_r(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u_r(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_u_l(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u_l(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_d_r(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d_r(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_d_l(move)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d_l(captured)&op;
        }
        self |= captured;
        op &= ~captured;


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
        cout << "\n\nInvalid Move\n\n";
        return NULL;
    }
}

bool game_over(struct board *board, bool black_pass, bool white_pass){
    return (board->white|board->black == FULL)|| (board->white == 0 || board->black == 0) || (black_pass&white_pass);
}

void print_board(struct board *board, bool withMoves){
    string show = "  A B C D E F G H\n1 ";
    uint64_t white = board->white;
    uint64_t black = board->black;
    int turn = board->turn;
    uint64_t moves;
    char row_char[5]; // a little cumbersome, might change in future
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
            show+="x ";
        }
        else if ((white>>i & 1)>0){
            show+="W ";
        }
        else if ((black>>i & 1)>0){
            show+="B ";
        }
        
        else{
            show+="_ ";
        }
        if (i%8 == 0 && i>1){
            std::sprintf(row_char,"\n%d",row);
            show+=row_char;
            row++;
        }
    }
    cout << show;
}

uint64_t coord_to_move(string move){
    return 0x0;
}

string move_to_coord(uint64_t coord){
    return "A1";
}

vector<int> get_move_indicies(uint64_t moves){
    vector<int> move_indicies;
    vector<int>::iterator it;
    it = move_indicies.begin();
    int index;
    while (moves>0){
        index = std::countl_zero(moves);
        cout << index << endl;
        moves >> index+1;
    }
    return move_indicies;
}