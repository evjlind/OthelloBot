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
    for (int i=0;i<test->move_hist.size();i++){
        cout << endl << test->move_hist[i]->m_name;
    }
    return 0;
}

Game* play_game(Player *player1, Player *player2){
    Game *game = init_game();
    Board *board = game->board;
    Move *move = init_move();
    Move *passMove = init_move();
    vector<Move*> legalMoves;
    int j = 0;
    while (j<64){
        cout << endl << "Turn: " << board->turn+1 << endl;
        print_board(board,true);
        uint64_t moves = generate_moves(board);
        legalMoves = get_move_indicies(moves);
        if ((board->turn % 2) == 0){
            if (legalMoves.size()>0){
                move = player1->choose_move(board,legalMoves);
                cout << move->m_name << endl << move->m_value;
                board = make_move(move,board,moves);
                game->move_hist.push_back(move);
            }
            else{
                board = player1->pass_turn(board);
                game->move_hist.push_back(passMove);
                cout << "pass" << endl;
            }
        }
        else {
            if (legalMoves.size()>0){
                move = player2->choose_move(board,legalMoves);
                cout << move->m_name << endl << move->m_value;
                board = make_move(move,board,moves);
                game->move_hist.push_back(move);
            }
            else{
                board = player2->pass_turn(board);
                game->move_hist.push_back(passMove);
                cout << "pass" << endl;
            }
        }
        
        // if (game_over(board)){
        //     break;
        // }
        j++;
    }
    game->board = board;
    return game;
}