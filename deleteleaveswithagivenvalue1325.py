# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root, target):
        if root == None:
            return None
        if root.left:
            root.left = self.removeLeafNodes(root.left,target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None:
            if root.val == target:
                return None
        return root
sunnyNode = TreeNode(1)
sunnyNode.left = TreeNode(2)
sunnyNode.right = TreeNode(3)
sunnyNode.left.left = TreeNode(4)
sunnyNode.right.left = TreeNode(5)
sunnyNode.right.right = TreeNode(6)
Solution().removeLeafNodes(sunnyNode,2)
class Solution:
    #wrong answer. comment is on line 36. 
    def removeLeafNodes(self,root,target):
        if root.left:
            self.removeLeafNodes(root.left,target)
        if root.right:
            self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None:
            if root.val == target:
                root = None # this is not actually changing the value of the current Node. It's just declaring that root = None now.
        return root