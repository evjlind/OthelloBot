#include<cstdint>
#include<string>
#include<iostream>
#include<unordered_map>
#include<fstream>
#include<iostream>

int main(){
    uint64_t val = 0x8000000000000000;
    std::unordered_map<std::string,uint64_t> u;
    char col[8] = {'A','B','C','D','E','F','G','H'};
    char row[8] = {'1','2','3','4','5','6','7','8'};
    std::string temp = "";
    for (int i=0;i<8;i++){
        for (int j=0;j<8;j++){
            temp += col[j];
            temp += row[i];
            u.insert({temp,val});
            std::cout << temp << '\n';
            val = val >> 1;
            temp = "";
        }
    }
    return 0;
}

