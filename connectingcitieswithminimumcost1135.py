#kurskal
class UnionFind:
    def __init__(self, number):
        # 0 ~ N-1
        self.list = [i for i in range(number)]
        self.weight= [1 for i in range(number)]
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    def find(self, p):
        if self.list[p] != p:
            self.list[p] = self.find(self.list[p])
            return self.list[p]
        return self.list[p]
        # while self.list[p] != p:
        #     self.list[p] = self.list[self.list[p]]
        #     p = self.list[p]
        # return self.list[p]
    def union(self, p,q):
        ancestor_p = self.find(p)
        ancestor_q = self.find(q)
        if ancestor_p != ancestor_q:
            if self.weight[ancestor_p] >= self.weight[ancestor_q]:
                self.list[ancestor_q] = ancestor_p
                self.weight[ancestor_p] += self.weight[ancestor_q]
            else:
                self.list[ancestor_p] = ancestor_q
                self.weight[ancestor_q] += self.weight[ancestor_p]
    
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        #Kruskal
        edges = [(i[2],i[0],i[1]) for i in connections]
        #return minimum cost
        #mark length of paths
        paths = 0
        cost = 0
        union_find = UnionFind(N)
        pq = []
        for edge in edges:
            heapq.heappush(pq, edge)
        while pq and paths< N-1:
            current_edge = heapq.heappop(pq)
            v = current_edge[1]
            w = current_edge[2]
            if union_find.connected((v-1),(w-1)):
                continue
            paths+=1
            cost += current_edge[0]
            union_find.union((v-1),(w-1))
        
        return cost if paths== N-1 else -1
#prim

    
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        #prim
        pq = []
        edges = [[] for i in range(N)]
        paths = [False for i in range(N)]
        path_num = 0
        total_cost = 0
        for connection in connections:
            city1, city2, cost = connection
            
            edges[city1-1].append((cost, city1, city2))
            
            edges[city2-1].append((cost, city1, city2))
            
        paths[connections[0][0]-1] = True
        for neighbor_edge in edges[connections[0][0]-1]:
            heapq.heappush(pq, neighbor_edge)
        
        while pq and path_num < N-1:
            
            current = heapq.heappop(pq)
            v = current[1]
            w = current[2]
            if paths[v-1] and paths[w-1]:
                continue
            else:
                path_num += 1
                total_cost += current[0]
                # print(pq, v, w, paths, current, cost)
                if paths[v-1]:
                    paths[w-1] = True
                    for neighbor_edge in edges[w-1]:
                        heapq.heappush(pq, neighbor_edge)
                else:
                    paths[v-1] = True
                    for neighbor_edge in edges[v-1]:
                        heapq.heappush(pq, neighbor_edge)
                
                
        return total_cost if path_num == N-1 else -1     