def knightTour(n):
    arr=[[-1 for i in range(n)]for j in range(n)]
    movX=[2, 1, -1, -2, -2, -1, 1, 2]
    movY=[1, 2, 2, 1, -1, -2, -2, -1]
    arr[0][0]=0
    if knightMove(arr, 0, 0, movX, movY, 1):
        printsol(arr, n)
        return
    else:
        print("solution does not exists:")
        return


def printsol(arr,n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def knightMove(arr,currX,currY,X,Y,pos):
    n=len(arr)

    if(pos==n*n):
        return True
    for i in range(8):
        nextX=currX + X[i]          # we have to loop for m times bcz knight can move maximum 8 ways in any size of board
        nextY=currY + Y[i]
        if issafe(arr,n,nextX,nextY):
            arr[nextX][nextY] = pos
            if knightMove(arr,nextX,nextY,X,Y,pos+1):
                return True
            # BackTracking Part
            arr[nextX][nextY] = -1
    return False



def issafe(arr,n,nextX,nextY):
    if nextX<n and nextX>=0 and nextY<n and nextY>=0 and arr[nextX][nextY]==-1:
        return True
    return False

n=int(input('Dimention:'))
knightTour(n)


'''
output shows the steps  a knight move from step number 0 to step (n X n)
'''