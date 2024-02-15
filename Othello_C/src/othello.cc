#include<cstdint>
#include<string>
#include<iostream>
#include<vector>
#include<cmath>
#include<iterator>
#include<bitset>
#include"othello.h"

using namespace std;

//initialize a board in the starting position
Board* new_board(){
    uint64_t white = INIT_BOARD_WHITE;
    uint64_t black = INIT_BOARD_BLACK;
    Board* new_board = new Board;
    new_board->white = white;
    new_board->black = black;
    new_board->turn = 0;
    return new_board;
}

Move* init_move(){
    Move* move = new Move;
    int row = 0, col = 0;
    string name = "X#";
    uint64_t value = 0;
    move->m_value = value;
    move->m_name = name;
    move->src_col = col;
    move->src_row = row;
    return move;
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

//find the legal moves in a given board position (*board) for the player whose turn it is
uint64_t generate_moves(Board *board){
    uint64_t self;
    uint64_t op;
    int player = (board->turn)%2;
    if (player==0){
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
Board* make_move(Move *move, Board *board, uint64_t legalMoves){
    uint64_t expressedMove = move->m_value;
    int turn = board->turn;
    uint64_t self, op;
    uint64_t captured;
    uint64_t overlap = expressedMove&legalMoves;
    if (turn % 2 == 0){
        self = board->black;
        op = board->white;
    }
    else{
        self = board->white;
        op = board->black;
    }

    if (overlap>0){
        self |= expressedMove;
        captured = shift_u(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_d(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_r(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_r(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_l(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_l(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_u_r(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u_r(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_u_l(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_u_l(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_d_r(expressedMove)&op;
        for (int i=0;i<5;i++){
            captured |= shift_d_r(captured)&op;
        }
        self |= captured;
        op &= ~captured;

        captured = shift_d_l(expressedMove)&op;
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

bool game_over(Board *board){
    bool no_moves;
    uint64_t m1;
    m1 = generate_moves(board);
    if (m1 == 0){
        board->turn++;
        m1 = generate_moves(board);
        board->turn--;
        if (m1 == 0){
            no_moves = true;
            printf("gg");
        }
    }
    return ((board->white)|(board->black) == FULL) || (no_moves);
}

void print_board(Board *board, bool withMoves){
    string show = "  A B C D E F G H\n1 ";
    uint64_t white = board->white;
    uint64_t black = board->black;
    int turn = board->turn;
    uint64_t moves;
    char row_char[5]; // a little cumbersome, might change in future
    int row = 2;
    
    if (withMoves == true){
        moves = generate_moves(board);
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
            std::sprintf(row_char,"\n%d ",row);
            show+=row_char;
            row++;
        }
    }
    cout << show << endl;
}

//Not sure if these two will be needed
Move* coord_to_move(string coord){
    Move *move;
    return move;
}

string move_to_coord(Move move){
    return "A1";
}

vector<Move*> get_move_indicies(uint64_t moves){
    uint64_t m = moves;
    uint64_t val = 0x8000000000000000;
    vector<Move*> move_indicies;
    Move *temp = init_move();
    string n_string = "";
    int index, real_row;
    int real_ind=0;
    char col_to_letter[8] = {'A','B','C','D','E','F','G','H'};
    while (m>0){
        index = countl_zero(m);
        m = m << index+1;
        real_ind += index+1;
        real_row = ceil(real_ind / 8)+1; // 3
        real_row--;
        temp->src_row = real_row;  // 2
        temp->src_col = (real_ind % 8)-1;
        n_string += col_to_letter[temp->src_col];
        n_string += real_row+'0';
        temp->m_name = n_string;
        temp->m_value = val>>(real_row)*8>>(real_ind % 8)-1;
        n_string = ""; 

        move_indicies.push_back(temp);
    }
    return move_indicies;
}

uint64_t coord_to_int(Move *move){
    uint64_t value;
    int col,row;
    col = move->src_col;
    row = move->src_row;
    return 0;
}

void disp_move_vect(vector<Move> moves){
    int length = moves.size();
    for (int i=0;i<length;i++){
        cout << moves[i].m_name << endl;
    }
}

int score_player(uint64_t v){
    bitset<64> d (v);
    return d.count();
}