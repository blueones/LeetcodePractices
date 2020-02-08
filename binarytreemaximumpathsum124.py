# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        if root == None:
            return 0
        def dfs(node):
            if node:
                leftS = dfs(node.left)
                rightS = dfs(node.right)
                self.maxSum = max(leftS+ rightS +node.val,self.maxSum)
                return max(0,leftS+node.val,rightS+node.val)
            else:
                return 0
        dfs(root)
        return self.maxSum