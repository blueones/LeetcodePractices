
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
            
class Solution1:
    def connect(self,root):
        # this algorithm is from Leetcode solutions solution2. brilliant solution.
        # leftmost = root
        # while (leftmost.left != null)
        # {
        #     head = leftmost
        # while (head.next != null)
        #     {
        #         1) Establish Connection 1
        #         2) Establish Connection 2 using next pointers
        #         head = head.next
        #     }
        # leftmost = leftmost.left
        # }
        if root == None:
            return None
        leftmost = root
        
        while leftmost.left != None: # while leftmost!= None: is wrong. becuase we are always taking care of next level's business. so we are done at the last level.
            flag = leftmost
            while flag!= None:
                if flag.next != None:
                    flag.right.next = flag.next.left
                flag.left.next = flag.right
                flag = flag.next
            leftmost = leftmost.left
        return root