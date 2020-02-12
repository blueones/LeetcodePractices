
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution1:
    def maxDepth(self, root: 'Node') -> int:
        #use BFS to calculate levels of a tree
        if root == None:
            return 0
        queueList = [root]
        newqueueList = []
        level = 0
        while queueList != []:
            currentNode = queueList.pop(0)
            
            for child in currentNode.children:
                newqueueList.append(child)
            if queueList == []:
                queueList = newqueueList
                newqueueList = []
                level += 1
        return level
class Solution2:
    def maxDepth(self, root: 'Node') -> int:
        #use DFS to calculate levels of a tree
        def dfs(head):
            if head == None:
                return 0
            childlevel = 0
            for child in head.children:
                childlevel = max(childlevel,dfs(child))
            return childlevel+1
        if root == None:
            return 0
        return dfs(root)

class Solution3:
    def maxDepth(self,root):
        #iterative method of doing this
        if root:
            stackList = [(root,1)]
        else:
            return 0
        depth = 0
        while stackList != []:
            currentNode, currentLevel = stackList.pop(-1)
            depth = max(depth,currentLevel)
            for child in currentNode.children:
                stackList.append((child, currentLevel+1))
        return depth


sunnyNode = Node(1)
sunnyNode.children=Node(3)
sunnyNode.children=Node(2)
sunnyNode.children=Node(4)