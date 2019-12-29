#solution1, DFS using list of edges.
class Solution:
    def networkDelayTime(self, times, N, K):
        #go to first node K, then go to its child nodes, create an array of distance, an array of marked,
        # for every node, check if it's marked, if marked then check if distance is larger, update with smaller distance,
        self.marked={nodes:False for nodes in range(1,N+1)}
        self.distance={nodes:0 for nodes in range(1,N+1)}
        self.edgeTo={nodes:nodes for nodes in range(1,N+1)}
        self.marked[K]=True
        self.distance[K]=0
        self.flag=False
        for travel in times:
            if travel[0]==K:
                self.flag=True
                self.travelNodes(times,K)
        print("self.marked is ",self.marked)
        if False in self.marked.values() or self.flag==False:
            return -1
        print(self.distance)
        return max(self.distance.values())
    def travelNodes(self,times,node):
        for travel in times:
            if travel[0]==node:
                if self.marked[travel[1]]==True:
                    if self.distance[travel[1]]>travel[2]+self.distance[travel[0]]:
                        self.distance[travel[1]]=travel[2]+self.distance[travel[0]]
                    continue
                if self.marked[travel[1]]==False:
                    self.marked[travel[1]]=True
                    self.distance[travel[1]]=travel[2]+self.distance[travel[0]]
                    self.edgeTo[travel[1]]=travel[0]
                self.travelNodes(times,travel[1])
            else:#if it's not a edge with node as the starting point, then keep on looping thru times
                continue
#solution2, create adjacency list graph from list of edges first. then do processing of it. 
    

#solution3, Dijkstra
print(Solution().networkDelayTime([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]],5,5))