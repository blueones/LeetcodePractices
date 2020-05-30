"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def traverse(node, visited):
            if node.val not in visited:
        
                current = Node(node.val)
                visited[current.val] = current
                current.neighbors = []
                for neighbor in node.neighbors:
                    cloned_neighbor = traverse(neighbor,visited)
                    current.neighbors.append(cloned_neighbor)
                return current
            else:
                return visited[node.val]
        if node == None:
            return None
        visited = dict()
        return traverse(node, visited)