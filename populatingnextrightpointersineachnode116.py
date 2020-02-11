
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #BFS traversal
        if root == None:
            return None
        queueList = [root]
        while queueList != []:
            n = len(queueList)
            while n > 0:
                currentNode = queueList.pop(0)
                if currentNode.left:
                    queueList.append(currentNode.left)
                if currentNode.right:
                    queueList.append(currentNode.right)
                if n == 1:
                    currentNode.next = None
                else:
                    currentNode.next = queueList[0]
                n -= 1
        return root
            
