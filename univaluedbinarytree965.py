# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node,value):
            if node == None:
                return True
            if node.val == value:
                return dfs(node.left,value) and dfs(node.right,value)
            else:
                return False
        if root == None:
            return True
        else:
            valueN = root.val
            return dfs(root,valueN)
class Solution2:
    #True recursion. compare if for everynode, node.val =node.left.value=node.right.val
    def isUnivalTree(self,root):
        if root == None:
            return True
        if root.right:
            if root.right.val!= root.val:
                return False
        if root.left:
            if root.left.val!=root.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
class Solution3:
    #BFS
    def isUnivalTree(self,root):
        def bfs(node,valueN):
            queueList = [node]
            while queueList != []:
                currentN = queueList.pop(0)
                if currentN != None:
                    if currentN.val != valueN:
                        return False
                    queueList.append(currentN.left)
                    queueList.append(currentN.right)
            return True
    


        if root == None:
            return True
        return bfs(root,root.val)