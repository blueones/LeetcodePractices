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
                self.maxSum = max(leftS+ rightS +node.val,self.maxSum, node.val, node.val+leftS, node.val+rightS)
                return max(0,leftS+node.val,rightS+node.val,node.val)
            else:
                return 0
        dfs(root)
        return self.maxSum
class Solution2:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")
        def helper(node):
            if node:
                left_gain = max(0, helper(node.left)) #important
                right_gain = max(0, helper(node.right))
                self.max_sum = (self.max_sum, node.val+left_gain+right_gain)
                return max(node.val+ left_gain, node.val+right_gain)
            else:
                return 0
        helper(root)
        return self.max_sum
class Solution1:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathSum = float("-inf")
        def helper(node):
            #input -- node
            #output largest in this subtree where the root is involved
            # and largest in the subtree where the root is not involved
            if node.left == None and node.right == None:
                self.maxPathSum = max(self.maxPathSum, node.val)
                return node.val
            else:
                left_max_sum = right_max_sum = 0
                if node.left:
                    left_max_sum = helper(node.left)
                if node.right:
                    right_max_sum = helper(node.right)
                max_all = max(node.val + left_max_sum, node.val+right_max_sum, node.val)
                self.maxPathSum = max(self.maxPathSum, max_all, node.val+left_max_sum+right_max_sum)
                return max_all
    
        
        helper(root)
        return self.maxPathSum