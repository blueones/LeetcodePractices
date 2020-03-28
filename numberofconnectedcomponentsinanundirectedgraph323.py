class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dict_adjacency_list = {node:[] for node in range(n)}
        visited = [False] * n
        componentsCount= 0
        if n == 0:
            return 0
        for edge in edges:
            dict_adjacency_list[edge[0]]+=[edge[1]]
            dict_adjacency_list[edge[1]]+=[edge[0]]
        def dfsHelper(node,visited):
            #dfs traverse children of nodes
            if visited[node]:
                return
            visited[node]= True
            for neighbor in dict_adjacency_list[node]:
                dfsHelper(neighbor,visited)
            # return visited
        for node in range(n):
            if visited[node]:
                continue
            componentsCount+=1
            # visited = dfsHelper(node,visited) #visited here is passed into the helper function, helper function is updating the list. but it's not creating a new list. so no need to return visited in line 18
        return componentsCount
         
