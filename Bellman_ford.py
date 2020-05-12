class Graph:
    def __init__(self,v):
        self.v=v
        self.g=[]
    def edgeadder(self,u,v,w):
        self.g.append([u,v,w])

    def printres(self,dist):
        for i in range(self.v):
            print('{} to {} is {}'.format(src,i,dist[i]))

    def Bellman_ford(self,src):
        dist=[9999]*self.v      # i consider 9999 as infynity
        dist[src]=0

        for i in range(self.v - 1):
            for u,v,w in self.g:
                if dist[u]+ w < dist[v] and dist[u]!=9999:
                    dist[v]=dist[u]+w

        self.printres(dist)



graph = Graph(5)  # 5 is total number of vertices

graph.edgeadder(0, 1, -1)
graph.edgeadder(0, 2, 4)
graph.edgeadder(1, 2, 3)
graph.edgeadder(1, 3, 2)        #static input taken as i'm tooooo lazy :)
graph.edgeadder(1, 4, 2)
graph.edgeadder(3, 2, 5)        # format of input is edgeadder is a method to add edge
graph.edgeadder(3, 1, 1)        # edgeadder(starting vertex, ending vertex ,weight)
graph.edgeadder(4, 3, -3)

src=int(input("source:"))

graph.Bellman_ford(src)


'''
Note this algo will not work if there exists a negative edge cycle
so the negative edge cycle means 
a cycle whose all edge sum is negative
'''