# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if root!=None:
            right=self.invertTree(root.right)
            left=self.invertTree(root.left)
            root.left=right
            root.right=left
        return root
class Solution2:
    def invertTree(self, root):
        if root!=None:
            #same idea but wrong answer
            #root.left=self.invertTree(root.right)
            #root.right=self.invertTree(root.left)
            node=root.left
            root.left=self.invertTree(root.right)
            root.right=self.invertTree(node)
        return root        
SunnyTree = TreeNode(10)
SunnyTree.left = TreeNode(5)
SunnyTree.right = TreeNode(15)
SunnyTree.right.left=TreeNode(6)
SunnyTree.right.right=TreeNode(20)
Solution().invertTree(SunnyTree)
print(SunnyTree.left.right.val)