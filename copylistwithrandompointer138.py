
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #copy one by one, stop when for a node, the next is null
        def buildNode(node,index):
            copyNode=Node(node.val)
            copyNode.next=

        if head==None:
            return None
        else:
            copyNode=Node(head.val)
            copyNode.random=self.copyRandomList(head.random)
            copyNode.next=self.copyRandomList(head.next)
            return copyNode
        