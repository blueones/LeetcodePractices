class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #BFS traversal. copied from 116. since even though the tree is not perfect. BFS doesn't mind. what a good solution haha. 
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
    def connect(self, root):
        #great solution to connect all nodes with a pseudo node. 
        head = root
        while head:
            connectNode = Node(0)
            leadNode = connectNode
            node = head
            while node:
                if node.left:
                    connectNode.next = node.left
                    connectNode = node.left
                if node.right:
                    connectNode.next = node.right
                    connectNode = node.right
                node = node.next
            if leadNode
            head = leadNode.next
        return root

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_nodes = []
            while level_size > 0:
                current_node = queue.popleft()
                level_nodes.append(current_node)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                level_size -= 1
            for index in range(len(level_nodes)-1):
                level_nodes[index].next = level_nodes[index+1]
        return root
                
                