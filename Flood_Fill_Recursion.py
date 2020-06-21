def floodfill(arr,r,c,oldC,newC):
       row =len(arr)-1
       col =len(arr[0])-1
       if r>row or r<0 or c>col or c<0:
              return
       if arr[r][c] != oldC:
              return
       arr[r][c]=newC
       floodfill(arr,r+1,c,oldC,newC)
       floodfill(arr,r-1,c,oldC,newC)            # bcz it every node has 4 neighbour
       floodfill(arr,r,c+1,oldC,newC)
       floodfill(arr,r,c-1,oldC,newC)

arr = [[1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 0, 1, 1, 1, 0, 0],
       [1, 0, 0, 1, 1, 0, 1, 1],
       [1, 2, 2, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 2, 2, 0],
       [1, 1, 1, 0, 1, 2, 1, 1],
       [1, 1, 0, 1, 1, 2, 2, 1],
       [1, 0, 1, 1, 1, 2, 2, 1]]
floodfill(arr,3,0,1,4)
# printing solution
for i in range(len(arr)):
       print(arr[i])
