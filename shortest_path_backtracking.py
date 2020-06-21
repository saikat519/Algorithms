import numpy as np
def min_distance(arr,i,j,m,n):
       row=len(arr)
       col=len(arr[2])
       vis=np.zeros((row,col),dtype=bool)
       return min_dist(arr,i,j,m,n,vis)
def isvalid(arr,i,j,vis):
       row = len(arr)
       col = len(arr[2])
       return i>=0 and i<row and j>=0 and j<col and arr[i][j]==1 and vis[i][j]==False

def min_dist(arr,i,j,m,n,vis):
       if not isvalid(arr,i,j,vis):
              return 9998999
       if m==i and n==j:
              return 0
       vis[i][j]=True
       top=min_dist(arr,i-1,j,m,n,vis)+1
       bottom=min_dist(arr,i+1,j,m,n,vis)+1
       left=min_dist(arr,i,j-1,m,n,vis)+1
       right=min_dist(arr,i,j+1,m,n,vis)+1

       vis[i][j]=False             # while Backtracking mark visited node as unvisited
                                   # Bcz we never follow the path again which is already visited
                                   # if one path is shorter then the path should be unvisited to check
       return min(top,bottom,left,right)

arr = [[1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 0, 0],
       [1, 0, 1, 1, 1, 1, 1, 1],
       [1, 0, 1, 1, 0, 0, 1, 0],
       [1, 1, 1, 0, 1, 0, 1, 0],
       [1, 1, 1, 1, 1, 1, 0, 0],
       [1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 0, 1, 1]]

final_result=min_distance(arr,0,0,7,7)

if final_result>999999:
       print("No path possible:")
else:
       print('Min distance is:{}'.format(final_result))