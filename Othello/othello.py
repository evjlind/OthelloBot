import numpy as np

class OthelloEnv():
    metadata = {"name": "othelloEnv_v1"}

    def __init__(self):

        self.board = np.zeros((8,8),dtype=int)
        self.board[3][3]=1
        self.board[3][4]=-1
        self.board[4][3]=-1
        self.board[4][4]=1
        self.moves = np.zeros_like(self.board)

    def reset(self):
        self.board = np.zeros((8,8),dtype=int)
        self.board[3][3]=1
        self.board[3][4]=-1
        self.board[4][3]=-1
        self.board[4][4]=1

    def _legal_moves(self,player):
        board = self.board
        coords = [(i,j) for i in range(8) for j in range(8) if board[i][j] == player]
        legal_moves = np.zeros_like(self.board)
        #player 2 =  black, player 1 = white
        other_p = -player
        for m in coords:
            i=m[0]
            j=m[1]
            n=1
            if (i)<=6:
                if board[i+n][j] == other_p: 
                    while (i+n)<=7:
                        if board[i+n][j] == other_p: 
                            n=n+1
                        elif board[i+n][j] == player:
                            n=999
                        elif board[i+n][j] == 0:
                            # legal_moves.append((i+n,j))
                            legal_moves[i+n][j] = player
                            n=999
            n=1
            if i>=1:
                if board[i-n][j] == other_p: 
                    while (i-n)>=0:
                        if board[i-n][j] == other_p: 
                            n=n+1
                        elif board[i-n][j] == player:
                            n=999
                        elif board[i-n][j] == 0:
                            # legal_moves.append((i-n,j))
                            legal_moves[i-n][j] = player
                            n=999
            n=1
            if j<=6:
                if board[i][j+n] == other_p: 
                    while (j+n)<=7:
                        if board[i][j+n] == other_p: 
                            n=n+1
                        elif board[i][j+n] == player:
                            n=999
                        elif board[i][j+n] == 0:
                            # legal_moves.append((i,j+n))
                            legal_moves[i][j+n] = player
                            n=999
            n=1
            if j>=1:
                if board[i][j-n] == other_p: 
                    while (j-n)>=0:
                        if board[i][j-n] == other_p: 
                            n=n+1
                        elif board[i][j-n] == player:
                            n=999
                        elif board[i][j-n] == 0:
                            # legal_moves.append((i,j-n))
                            legal_moves[i][j-n] = player
                            n=999
            n=1
            if i<=6 and j<=6:
                if board[i+n][j+n] == other_p:
                    while(i+n<=7 and j+n<=7):
                        if board[i+n][j+n] == other_p:
                            n=n+1
                        elif board[i+n][j+n] == player:
                            n=999
                        else:
                            # legal_moves.append((i+n,j+n))
                            legal_moves[i+n][j+n] = player
                            n=999
            n=1
            if i<=6 and j>=0:
                if board[i+n][j-n] == other_p:
                    while (i+n<=7 and j-n>=0):
                        if board[i+n][j-n] == other_p:
                            n=n+1
                        elif board[i+n][j-n] == player:
                            n=999
                        else:
                            # legal_moves.append((i+n,j-n))
                            legal_moves[i+n][j-n] = player
                            n=999
            n=1
            if i>=0 and j<=6:
                if board[i-n][j+n] == other_p:
                    while ((i-n)>=0 and (j+n)<=7):
                        if board[i-n][j+n] == other_p:
                            n=n+1
                        elif board[i-n][j+n] == player:
                            n=999
                        else:
                            # legal_moves.append((i-n,j+n))
                            legal_moves[i-n][j+n] = player
                            n=999
            n=1
            if i>=0 and j>=0:
                if board[i-n][j-n] == other_p:
                    while ((i-n)>=0 and (j-n)>=0):
                        if board[i-n][j-n] == other_p:
                            n=n+1
                        elif board[i-n][j-n] == player:
                            n=999
                        else:
                            # legal_moves.append((i-n,j-n))
                            legal_moves[i-n][j-n] = player
                            n=999
        return legal_moves
    
    def make_move(self, move, player):
        if move == (-1,-1):
            return None
        i = move[0]
        j = move[1]
        n=1
        if i<=6:   
            if self.board[i+n][j] == -player: 
                while (i+n)<=7:
                    if self.board[i+n][j] == -player: 
                        self.board[i+n][j] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if i>=1:
            if self.board[i-n][j] == -player: 
                while (i-n)>=0:
                    if self.board[i-n][j] == -player: 
                        self.board[i-n][j] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if j<=6:
            if self.board[i][j+n] == -player: 
                while (j+n)<=7:
                    if self.board[i][j+n] == -player: 
                        self.board[i][j+n] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if j>=1:
            if self.board[i][j-n] == -player: 
                while (j-n)>=0:
                    if self.board[i][j-n] == -player: 
                        self.board[i][j-n] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if i<=6 and j<=6:
            if self.board[i+n][j+n] == -player:
                while(i+n<=7 and j+n<=7):
                    if self.board[i+n][j+n] == -player:
                        self.board[i+n][j+n] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if i<=6 and j>=0:
            if self.board[i+n][j-n] == -player:
                while (i+n<=7 and j-n>=0):
                    if self.board[i+n][j-n] == -player:
                        self.board[i+n][j-n] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if i>=0 and j<=6:
            if self.board[i-n][j+n] == -player:
                while ((i-n)>=0 and (j+n)<=7):
                    if self.board[i-n][j+n] == -player:
                        self.board[i-n][j+n] = player
                        n=n+1
                    else:
                        n=999
        n=1
        if i>=0 and j>=0:
            if self.board[i-n][j-n] == -player:
                while ((i-n)>=0 and (j-n)>=0):
                    if self.board[i-n][j-n] == -player:
                        self.board[i-n][j-n] = player
                        n=n+1
                    else:
                        n=999
        self.board[i][j] = player


#interesting idea for searching board but doesn't work for anything yet
        # hori = self.board[i,:]
        # vert = self.board[:,j]
        # k = j-i
        # m = 7-j-i
        # diag1 = np.diag(self.board,k)
        # diag2 = np.diag(np.fliplr(self.board),m)

        # hori = OthelloEnv.flip_pieces(hori)
        # vert = OthelloEnv.flip_pieces(vert)
        # diag1 = OthelloEnv.flip_pieces(diag1)
        # diag2 = OthelloEnv.flip_pieces(diag2)

        # def flip_pieces(vector,player):
        #   player_loc = np.where(vector == player)
        #   opp_loc = np.where(vector == -player)
        #   if 


    def has_legal_move(self,player):
        moves = OthelloEnv._legal_moves(self,player)
        if abs(np.sum(moves))>0:
            return True
        else:
            return False
    
    def score_board(self):
        score = np.sum(self.board)
        return score

    def getGameOver(self):
        if OthelloEnv.has_legal_move(self,1) or  OthelloEnv.has_legal_move(self,-1):
            return False
        else:
            return True
        
    def disp_board(self):
        disp = np.empty_like(self.board,dtype=str)
        n = np.where(self.moves != 0)
        rows = n[0]
        cols = n[1]
        move_no = np.linspace(1,len(rows),len(rows))
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i][j] == 0:
                    found = False
                    for k in range(len(rows)):
                        if (i,j) == (rows[k],cols[k]):
                            disp[i][j] = str(move_no[k])
                            found = True
                    if not found:
                        disp[i][j] = '_'
                if self.board[i][j] == 1:
                    disp[i][j] = 'X'
                if self.board[i][j] == -1:
                    disp[i][j] = 'O'
        print(disp)