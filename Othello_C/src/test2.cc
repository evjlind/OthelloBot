#include"othello.h"
#include"player.h"
#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

int main(){
    uint64_t arb_moves = 4611967630860353536;
    vector<Move *> move_list;
    unordered_map<string,uint64_t> lookup_map = build_move_lookup();
    move_list = get_move_indicies(arb_moves,lookup_map);
    for (int i=0;i<move_list.size();i++){
        cout << move_list[i]->src_col << " " << move_list[i]->src_row << " " << move_list[i]->m_name << endl;
    }
    return 0;
}