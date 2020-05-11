class Graph():
    def __init__(self,v,g):
        self.v = v
        self.g = g

    def dijkstra(self,src):

        dist=[9999]*self.v
        mst=[False]*self.v
        dist[src]=0

        for cout in range(self.v-1):

            u = self.mindist(dist, mst)
            mst[u] = True
            for v in range(self.v):
                if self.g[u][v]!=0 and mst[v] == False and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]

        self.printres(dist)


    def printres(self,dist):
        for node in range(self.v):
            print('{} to {} is {}\n'.format(src,node,dist[node]))

    def mindist(self, dist, mst):
        min=9999

        for v in range(self.v):
            if dist[v] < min and mst[v] == False:
                min = dist[v]
                min_index = v

        return min_index



v=int(input("Enter no. of vertex::"))
g=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0] ]
'''
for i in range(v):
    a=[]
    for j in range(v):      
        a.append(int(input('{} to {} weight::'.format(i,j))))       # incase of dynamic input
    g.append(a)
'''
graph=Graph(v,g)
src=int(input("source:"))
graph.dijkstra(src)
