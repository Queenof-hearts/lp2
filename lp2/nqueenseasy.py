N=4
def printboard(board):
    for i in range(N):
        for j in range(N):
            print('Q'if board[i][j]==1 else '.',end=' ')
        print()
    print()

def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True

def SolvenQutil(board,col):
    if col>=N:
        printboard(board)
        return 
    
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col]=1
            SolvenQutil(board,col+1)   
            board[i][col]=0

def SolvenQ():
    board=[[0,0,0,0]for i in range(N)]
    SolvenQutil(board,0)

SolvenQ()