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

    def legal_moves(board,player):
        coords = [(i,j) for i in range(8) for j in range(8) if board[i][j] == player]
        legal_moves = np.zeros_like(board)
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
    
    def make_move(board, move, player):
        if move == (-1,-1):
            return None
        i = move[0]
        j = move[1]
        n=1
        if i<=6:   
            if board[i+n][j] == -player: 
                flipped = np.zeros_like(board)
                while (i+n)<=7:
                    if board[i+n][j] == -player:
                        flipped[i+n][j] = player
                        n=n+1
                    elif board[i+n][j] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
            
        n=1
        if i>=1:
            if board[i-n][j] == -player: 
                flipped = np.zeros_like(board)
                while (i-n)>=0:
                    if board[i-n][j] == -player: 
                        flipped[i-n][j] = player
                        n=n+1
                    elif board[i-n][j] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
            
        n=1
        if j<=6:
            if board[i][j+n] == -player: 
                flipped = np.zeros_like(board)
                while (j+n)<=7:
                    if board[i][j+n] == -player: 
                        flipped[i][j+n] = player
                        n=n+1
                    elif board[i][j+n] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
            
        n=1
        if j>=1:
            if board[i][j-n] == -player: 
                flipped = np.zeros_like(board)
                while (j-n)>=0:
                    if board[i][j-n] == -player: 
                        flipped[i][j-n] = player
                        n=n+1
                    elif board[i][j-n] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
        n=1
        if i<=6 and j<=6:
            if board[i+n][j+n] == -player:
                flipped = np.zeros_like(board)
                while(i+n<=7 and j+n<=7):
                    if board[i+n][j+n] == -player:
                        flipped[i+n][j+n] = player
                        n=n+1
                    elif board[i+n][j+n] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
        n=1
        if i<=6 and j>=0:
            if board[i+n][j-n] == -player:
                flipped = np.zeros_like(board)
                while (i+n<=7 and j-n>=0):
                    if board[i+n][j-n] == -player:
                        flipped[i+n][j-n] = player
                        n=n+1
                    elif board[i+n][j-n] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
        n=1
        if i>=0 and j<=6:
            if board[i-n][j+n] == -player:
                flipped = np.zeros_like(board)
                while ((i-n)>=0 and (j+n)<=7):
                    if board[i-n][j+n] == -player:
                        flipped[i-n][j+n] = player
                        n=n+1
                    elif board[i-n][j+n] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
        n=1
        if i>=0 and j>=0:
            if board[i-n][j-n] == -player:
                flipped = np.zeros_like(board)
                while ((i-n)>=0 and (j-n)>=0):
                    if board[i-n][j-n] == -player:
                        flipped[i-n][j-n] = player
                        n=n+1
                    elif board[i-n][j-n] == player:
                        test = np.where(flipped==player)
                        for p in range(int(len(test[0]))):
                            board[test[0][p]][test[1][p]] = player
                        break
                    else:
                        n=999
        # board = flipped
        board[i][j] = player
        return board

    def has_legal_move(self,player):
        moves = OthelloEnv.legal_moves(self,player)
        if abs(np.sum(moves))>0:
            return True
        else:
            return False
    
    def score_board(self):
        black_score = len(np.where(self.board==1)[0])
        white_score = len(np.where(self.board==-1)[0])
        return (black_score,white_score)

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