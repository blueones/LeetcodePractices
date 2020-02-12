# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        #the most intuitive solution
        def recursionsearch(node,val):
            if node.val < val:
                if node.right == None:
                    node.right = TreeNode(val)
                else:
                    recursionsearch(node.right,val)
            elif node.val >val:
                if node.left == None:
                    node.left = TreeNode(val)
                else:
                    recursionsearch(node.left,val)
        recursionsearch(root,val)
        return root