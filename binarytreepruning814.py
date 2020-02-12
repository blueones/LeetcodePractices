# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        #wrong. 
        def prune(node, pre):
                current = leftN = rightN = False
                if node:
                    if node.val == 1:
                        current = True
                    leftN = prune(node.left,node)
                    rightN = prune(node.right,node)
                if (current or leftN or rightN) == False:
                    pre.next = None # there is no next attribute. so you can't use this solution. it has to look at left and right.
                return current or leftN or rightN
        prune(root, None)
        return root
class Solution1:
    def pruneTree(self,root):
        def prune(node):
            currentN = leftB = rightB = False
            if node:
                if node.val == 1:
                    currentN = True
                leftB = prune(node.left)
                rightB = prune(node.right)
                if leftB == False:
                    node.left = None
                if rightB == False:
                    node.right = None
            return currentN or leftB or rightB
        prune(root)
        return root
sunnyNode = TreeNode(1)
sunnyNode.right = TreeNode(0)
sunnyNode.right.left = TreeNode(0)
sunnyNode.right.right = TreeNode(1)
Solution().pruneTree(sunnyNode)
