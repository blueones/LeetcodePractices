from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dict_network = defaultdict(set)
        current_network = defaultdict(set)
        for connection in connections:
            u,v = connection[0],connection[1]
            dict_network[u].add(v)
            dict_network[v].add(u)
            current_network[u].add(v)
        def traverse(node, connection_set,current_net):
            count = 0
            if node not in self.visited:
                self.visited.add(node)
                if node in connection_set:
                    for neighbor in connection_set[node]:
                        if neighbor not in self.visited:
                           
                            if node in current_net and neighbor in current_net[node] :

                                count += 1
                            count += traverse(neighbor, connection_set, current_net)
            return count
        self.visited = set()
        return traverse(0, dict_network,current_network)
            