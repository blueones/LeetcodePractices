# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        elif root!=None:
            leftN=root.left
            rightN=root.right
            depthL=self.Depth(leftN)
            depthR=self.Depth(rightN)
            if abs(depthL-depthR)<=1:
                if self.isBalanced(leftN) and self.isBalanced(rightN):
                    return True
            else:
                return False
    def Depth(self,root:):
        if root==None:
            return 0
        elif root!=None:
            depth=1
            leftN=root.left
            rightN=root.right
            depth=depth+max(self.Depth(leftN),self.Depth(rightN))
            return depth

