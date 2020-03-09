class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        self.flowers = [1,2,3,4]
        self.graphGarden = {n:[] for n in range(1,N+1, 1)}
        self.marked = {n:0 for n in range(1,N+1,1)}
        for path in paths:
            self.graphGarden[path[0]].append(path[1])
            self.graphGarden[path[1]].append(path[0])
        print(self.graphGarden)
        def DFS(node, flowers):
            for neighbor in self.graphGarden[node]:
                print("neighbor", neighbor, "flowers",flowers)
                if self.marked[neighbor]!= 0 and self.marked[neighbor]!= self.marked[node]:
                    continue
                self.marked[neighbor] = flowers.pop(-1)
                flowers.append(self.marked[node])
                DFS(neighbor, flowers.copy())
                flowers.pop(-1)
                flowers.append(self.marked[neighbor])
        for i in range(1,N+1):
            if self.marked[i] == 0:
                self.marked[i] = self.flowers.pop(-1)
                DFS(i, self.flowers.copy())
                
        return self.marked.values()