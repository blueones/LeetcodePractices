# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.maxedge = 0
        def dfs(node):
            #return the longer path out of right and left.
            
            if node:
                leftL = dfs(node.left)
                rightL = dfs(node.right)
                leftCurrentL = rightCurrentL = 0 # only after node is equal to left or right, the currentlength gets increase. otherwise, it's 0. 
                if node.right and node.val == node.right.val:
                    rightCurrentL = 1 + rightL
                if node.left and node.val == node.left.val:
                    leftCurrentL = 1 + leftL
                self.maxedge = max(self.maxedge,rightCurrentL+leftCurrentL)
                return max(rightCurrentL,leftCurrentL)
            else:
                return 0
        dfs(root)
        return self.maxedge


SunnyNode = TreeNode(8)
SunnyNode.left = TreeNode(9)
SunnyNode.right = TreeNode(9)                