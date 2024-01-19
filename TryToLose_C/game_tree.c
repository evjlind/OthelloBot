#include <stdio.h>
#include <stdlib.h>

struct board_node
{
    struct board *board;
    struct board_node* **children;
    int numKids;
    int score;
    int depth;
};

struct board_node* add_child(struct board_node *root, struct board_node *child);
struct board_node* new_node(short board);
void eval_node(struct board_node *node);
int minimax(struct board_node *root);


int main(){
    printf("test");
    short blank_board = 0;
    struct board_node *root_node = new_node(blank_board);
    return 0;
}

struct board_node* new_node(short board)
{
    struct board_node* n = (struct board_node*)malloc(sizeof(struct board_node));
    n->board = board;
    n->children = NULL;
    n->depth = NULL;
    n->numKids = NULL;
    n->score=NULL;
}

struct board_node* add_child(struct board_node *root, struct board_node *child)
{
    if(root==NULL){
        return new_node(root->board);
    }
}

void eval_node(struct board_node *node)
{
    int num_moves;
    int *board[3][3] = node.board;

}