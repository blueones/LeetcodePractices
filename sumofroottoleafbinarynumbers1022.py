# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(node, parentSum):
            if node:
                currentSum = node.val + parentSum * 2
                if node.left == None and node.right == None:
                    self.sum += currentSum
                if node.left:
                    dfs(node.left, currentSum)
                if node.right:
                    dfs(node.right,currentSum)

        dfs(root, 0)
        return self.sum
            
class Solution2:
    def sumRootToLeaf(self,root,val = 0):
        #not using a class variable to store sum but to carry it in the recursion
        if root == None:
            return 0
        else:
            value = root.val + val*2
            if root.left == None and root.right == None:
                return value
            return self.sumRootToLeaf(root.left,root.val)+ self.sumRootToLeaf(root.right,root.val)
