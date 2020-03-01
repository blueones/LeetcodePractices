# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution1:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatL(node):
            if node == None:
                return None
            returnNode = node
            nodeR = node.right
            nodeL = node.left
            if nodeL:
                leftT = flatL(node.left)
                node.right = node.left
                node.left = None
                returnNode = leftT
            if nodeR:
                rightT = flatL(nodeR)
                if nodeL:
                    leftT.right = nodeR
                returnNode = rightT
            return returnNode
        flatL(root)
        return root           
            
sunnyN = TreeNode(1)
sunnyN.left = TreeNode(2)
sunnyN.right = TreeNode(5)
sunnyN.left.left = TreeNode(3)
sunnyN.left.right = TreeNode(4)          
sunnyN.right.right = TreeNode(6)
class Solution2:
    #from leetcode
    def flattenTree(self,root):
        if not node:
            return None
        if not node.left and not node.right:
            return node 
        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        return rightTail if rightTail else leftTail
    def flatten(self,root):
        self.flattenTree(root)
        

