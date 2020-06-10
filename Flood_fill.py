m=8         # size of graph (m,n)
n=8

def flood_fill(row,col,g,prevC,newC):

    visited=[]

    if row<0 or row>=m:
        return
    if col<0 or col>=n:
        return
    if g[row][col]!=prevC:
        return

    g[row][col]=newC
    visited.append([row,col])
    neighbours=nei_ghbour(g,row,col)

    for neighbour in neighbours:
        if neighbour not in visited:
            flood_fill(neighbour[0],neighbour[1],g,prevC,newC)

def nei_ghbour(g,r,c):
    return [[r,c+1],[r,c-1],[r+1,c-1],[r+1,c],[r+1,c+1],[r-1,c],[r-1,c+1],[r-1,c-1]]





print('input:')
g = [[1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 1, 1, 0, 1, 1],
       [1, 2, 2, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 2, 2, 0],
       [1, 1, 1, 1, 1, 2, 1, 1],
       [1, 1, 1, 1, 1, 2, 2, 1]]
for i in range(m):
    for j in range(n):
        print(g[i][j],end=' ')
    print()

x=4         # starting index (x,y) where the calculation starts
y=4

prevC=g[x][y]
newC=3

flood_fill(x,y,g,prevC,newC)

print('Result:')
for i in range(m):
    for j in range(n):
        print(g[i][j],end=' ')
    print()