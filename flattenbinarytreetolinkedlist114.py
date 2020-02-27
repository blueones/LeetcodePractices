# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatL(node):
            #only need to return the tail.
            if node == None:
                return None
            if node.left == None and node.right == None:
                return node
            nodeR = node.right
            nodeLW = flatL(node.left)
            nodeRW = flatL(node.right)
            
            if nodeLW:
                node.right= node.left
                node.left = None
                nodeLW.right = nodeR
            if nodeRW == None:
                return nodeLW
            return nodeRW

            
        flatL(root)
        
            
            
            
