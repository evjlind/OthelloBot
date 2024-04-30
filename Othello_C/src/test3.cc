#include"othello.h"
#include"player.h"
#include<iostream>
#include<vector>
#include<fstream>

using namespace std;
Game* play_game(Player *player1, Player *player2,unordered_map<string,uint64_t> lookups);

int main(){
    Player *player1 = Minimax();
    Player *player2 = Random();
    unordered_map<string,uint64_t> lookup_map = build_move_lookup();
    Game *test = play_game(player1, player2, lookup_map);
    printf("game over");
    // cout << test->winner << endl;
    int b_score = score_player(test->board->black);
    int w_score = score_player(test->board->white);
    printf("Black: %d, White %d\n",b_score,w_score);
    print_board(test->board,false);
    // for (int i=0;i<test->move_hist.size();i++){
    //     cout << test->move_hist[i]->m_name << endl;
    // }
    return 0;
}

Game* play_game(Player *player1, Player *player2, unordered_map<string,uint64_t> lookups){
    Game *game = init_game();
    Board *board = game->board;
    Move *move = init_move();
    Move *passMove = init_move();
    vector<Move*> legalMoves;
    int j = 0;
    while (game_over(board,game->move_hist) == false){
        cout << endl << "Turn: " << board->turn+1 << endl;
        print_board(board,true);
        uint64_t moves = generate_moves(board);
        legalMoves = get_move_indicies(moves,lookups);
        if ((board->turn % 2) == 0){
            if (legalMoves.size()>0){
                move = player1->choose_move(board,legalMoves);
                cout << move->m_name << endl;
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
                cout << move->m_name << endl;
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