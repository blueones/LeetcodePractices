
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #since for each node, there are two pointers pointing at different nodes, 
        # we could view this issue as a graph.
        # for each node, see if it's in the visited list, if it is
        self.visited={}
        def copy(head):
            if head == None:
                return None
            if head in self.visited:
                return self.visited[head] 
            else:
                copyN = Node(head.val)
                self.visited[head]=copyN
                copyN.next = copy(head.next)
                copyN.random = copy(head.random)
            return copyN
        if head == None:
            return None
        return copy(head)

        
        


            



        