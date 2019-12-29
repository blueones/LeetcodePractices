class Solution1:
    def networkDelayTime(self,times,N,K):
        #to create a list of adjacency nodes to represent this graph.
        self.graph=Graph(N)
        self.marked={node:False for node in range(1,N+1)}
        self.distancetoK={node:0 for node in range(1,N+1)}
        for edge in times:
            self.graph.addEdge(edge[0],[edge[1],edge[2]])
        if self.graph.adjL[K]==[]:
            return -1
        else:
            self.marked[K]=True
            self.travelDFS(K)
        if False in self.marked.values():
            return -1
        return max(self.distancetoK.values())

        
    def travelDFS(self,node):
        for edge in self.graph.adjL[node]:
            if self.marked[edge[0]]==True:
                if self.distancetoK[edge[0]]>self.distancetoK[node]+edge[1]:
                    self.distancetoK[edge[0]]=self.distancetoK[node]+edge[1]
                    self.travelDFS(edge[0])
                continue
            elif self.marked[edge[0]]==False:
                self.marked[edge[0]]=True
                self.distancetoK[edge[0]]=self.distancetoK[node]+edge[1]
                self.travelDFS(edge[0])
class Solution2:
    def networkDelayTime(self,times,N,K):
        #to create a list of adjacency nodes to represent this graph.
        self.graph=Graph(N)
        self.marked={node:False for node in range(1,N+1)}
        self.distancetoK={node:0 for node in range(1,N+1)}
        for edge in times:
            self.graph.addEdge(edge[0],[edge[1],edge[2]])
        if self.graph.adjL[K]==[]:
            return -1
        else:
            self.marked[K]=True
            self.travelBFS(K)
        if False in self.marked.values():
            return -1
        return max(self.distancetoK.values())

        
    def travelBFS(self,node):
        queueBFS=list()
        queueBFS.append(node)
        while queueBFS!=[]:
            currentNode=queueBFS.pop(0)
            for kid in self.graph.adjL[currentNode]:
                if self.marked[kid[0]]==True:
                    if self.distancetoK[kid[0]]>self.distancetoK[currentNode]+kid[1]:
                        self.distancetoK[kid[0]]=self.distancetoK[currentNode]+kid[1]
                        queueBFS.append(kid[0])
                elif self.marked[kid[0]]==False:
                    self.marked[kid[0]]=True
                    self.distancetoK[kid[0]]=self.distancetoK[currentNode]+kid[1]
                    queueBFS.append(kid[0])
            
class Graph:
    def __init__(self,N):
        self.adjL={i:[] for i in range(1,N+1)}
        self.node=N
    def addEdge(self,v,w):
        self.adjL[v].append(w)

print(Solution2().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))