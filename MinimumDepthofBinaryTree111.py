# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        elif root!=None:
            leftN=root.left
            rightN=root.right
            if leftN!=None and rightN!=None:
                dep=1
                dep=dep+min(self.minDepth(leftN),self.minDepth(rightN))
                return dep
            elif leftN==None and rightN==None:
                return 1
            else:
                if leftN==None:
                    dep=1
                    dep=dep+self.minDepth(rightN)
                elif rightN==None:
                    dep=1
                    dep=dep+self.minDepth(leftN)
                return dep
