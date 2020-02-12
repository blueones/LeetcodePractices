# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        elif root!=None:
            depth=1
            leftN=root.left
            rightN=root.right
            depth=depth+max(self.maxDepth(leftN),self.maxDepth(rightN))
            return depth
class Solution:
    def maxDepth(self,root):
        if root == None:
            return 0
        def dfs(node, lengthP):
            if node == None:
                return lengthP
            else:
                return max(dfs(node.left, lengthP + 1),dfs(node.right, lengthP +1)) 
        return dfs(root,0)