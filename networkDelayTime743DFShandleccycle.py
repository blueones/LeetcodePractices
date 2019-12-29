class Solution:
    def networkDelayTime(self, times, N, K):
        #go to first node K, then go to its child nodes, create an array of distance, an array of marked,
        # for every node, check if it's marked, if marked then check if distance is larger, update with smaller distance,
        self.times=times
        self.marked={nodes:False for nodes in range(1,N+1)}
        self.distance={nodes:0 for nodes in range(1,N+1)}
        self.marked[K]=True
        self.distance[K]=0
        self.flag=False
        for travel in times:
            if travel[0]==K:
                self.flag=True
                self.travelNodes(K)
        print("self.marked is ",self.marked)
        if False in self.marked.values() or self.flag==False:
            return -1
        #print(self.distance)
        return max(self.distance.values())
    def travelNodes(self,node):
        for travel in self.times:
            if travel[0]==node:
                if self.marked[travel[1]]==True:
                    if self.distance[travel[1]]>travel[2]+self.distance[travel[0]]:
                        self.distance[travel[1]]=travel[2]+self.distance[travel[0]]
                        self.travelNodes(travel[1])
                        #print("Visited an old node, now self.distance is ",self.distance)
                    continue
                if self.marked[travel[1]]==False:
                    self.marked[travel[1]]=True
                    self.distance[travel[1]]=travel[2]+self.distance[travel[0]]
                    #print("Marked a new node, now self.distance is ",self.distance)
                self.travelNodes(travel[1])
            else:#if it's not a edge with node as the starting point, then keep on looping thru times
                continue
#solution2, create adjacency list graph from list of edges first. then do processing of it. 
    

#solution3, Dijkstra
print(Solution().networkDelayTime())