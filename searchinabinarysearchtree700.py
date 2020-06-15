# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        else:
            if root.val > val:
                return self.searchBST(root.left,val)
            elif root.val < val:
                return self.searchBST(root.right,val)
            else:
                return root
class Solution1:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root != None:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
        return None