def PlaceQueen(i,board,n):
    if i==n:
        return True
    for j in range(n):
        if isSafe(j,board,i,n):
            board[i][j]=1
            if PlaceQueen(i+1,board,n):
                return True
            board[i][j]=0
    return False

def isSafe(pos,board,row,n):
    r=row                   #we have to take in a variable bcz in other loops row and pos values are
    p = pos                        # required so if we take directly the value will change and can't use
                            # in other loops

    for i in range(n):
        if board[i][p]==1:        # Checking the column
            return False
    while(r>=0 and p <n):
        if board[r][p]==1:      #upper right diagonal
            return False
        r-=1
        p+=1
    po=pos          #we have to take again bcz in upper loop row and pos values are changed
    ro=row
    while (ro >= 0 and po >= 0):
        if board[ro][po] == 1:     # upper left diagonal
            return False
        ro -= 1
        po -= 1
    return True

def nQueen(n,board):
    if PlaceQueen(0,board,n)==True:
        printsol(n,board)
        return
    else:
        print('solution does not exist:::')
        return
def printsol(n,board):
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                print(' Q ',end=' ')
            else:
                print(" _ ",end=' ')
        print()


n=int(input('Dimention::'))
board=[[0 for i in range(n)]for j in range(n)]
nQueen(n,board)