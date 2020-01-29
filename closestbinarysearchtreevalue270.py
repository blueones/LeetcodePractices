# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.left = float("-inf")
        self.right = float("inf")
        def dfs(node):
            if node != None:
                if node.val >= target: # here node.val need to have equal too. otherwise it's going to miss the situation where node.val == target.
                    self.right = min(node.val, self.right)
                    dfs(node.left)
                elif node.val < target:
                    self.left = max(node.val, self.left)
                    dfs(node.right)
        dfs(root)
        return self.left if abs(target - self.left) < abs(target - self.right) else self.right