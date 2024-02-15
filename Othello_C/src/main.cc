#include"othello.h"
#include"player.h"
#include<iostream>
#include<vector>
#include<fstream>

using namespace std;
Game* play_game(Player *player1, Player *player2);

int main(){
    Player *player1 = Random();
    Player *player2 = Random();
    Game *test = play_game(player1, player2);
    printf("game over");
    // cout << test->winner << endl;
    int b_score = score_player(test->board->black);
    int w_score = score_player(test->board->white);
    printf("Black: %d, White %d",b_score,w_score);
    return 0;
}

Game* play_game(Player *player1, Player *player2){
    Game *game;
    Board *board = new_board();
    Move *move;
    Move *passMove;
    // string p_string = "Pass";
    // passMove->m_name = p_string;
    // passMove->src_col = 9;
    // passMove->src_row = 9;
    // printf("vect init");
    vector<Move*> legalMoves;
    int i = 0;
    while (i<10){
        cout << endl << board->turn << endl;
        print_board(board,true);
        uint64_t moves = generate_moves(board);
        legalMoves = get_move_indicies(moves);
        if ((board->turn % 2) == 0){
            if (legalMoves.size()>0){
                move = player1->choose_move(board,legalMoves);
                board = make_move(move,board,moves);
                game->move_hist.push_back(move);
            }
            else{
                board = player1->pass_turn(board);
                game->move_hist.push_back(passMove);
            }
        }
        else {
            if (legalMoves.size()>0){
                move = player2->choose_move(board,legalMoves);
                board = make_move(move,board,moves);
                game->move_hist.push_back(move);
            }
            else{
                board = player2->pass_turn(board);
                game->move_hist.push_back(passMove);
            }
        }
        
        // if (game_over(board)){
        //     break;
        // }
        i++;
    }
    game->board = board;
    print_board(game->board,false);
    return game;
}