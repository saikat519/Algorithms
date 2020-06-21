def printsol(sol,n):
    print('The Rat should Go in this way:')
    for i in range(n):
        print(sol[i])
def isvalid(maze,x,y,n):
    return x>=0 and x<n and y>=0 and y<n and maze[x][y]==1

def rat_in_maze(maze,n):
    sol=[[0 for j in range(n)]for i in range(n)]
    if solve_maze(maze,0,0,sol,n)==False:
        print("solution doesn't exists:::")
    else:
        printsol(sol,n)
def solve_maze(maze,x,y,sol,n):
    if x==n-1 and y==n-1 and maze[x][y]==1:
        sol[x][y]=1
        return True
    if isvalid(maze,x,y,n)==True:

        if solve_maze(maze,x+1,y,sol,n)==True:
            sol[x][y] = 1
            return True
        if solve_maze(maze,x,y+1,sol,n)==True:
            sol[x][y] = 1
            return True
        return False

maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
rat_in_maze(maze,4)