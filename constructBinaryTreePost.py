class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

SunnyTree = TreeNode(1)
SunnyTree.left = TreeNode(5)
SunnyTree.left.right = TreeNode(7)
SunnyTree.left.left = TreeNode(6)
SunnyTree.right = TreeNode(3)
SunnyTree.right.left = TreeNode(9)
SunnyTree.right.right = TreeNode(2)
SunnyTree.right.right.right = TreeNode(8)

# 15673928
# 65719328
# 67598231
class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder)==1:
            return TreeNode(inorder[-1])
        elif len(inorder)==0:
            return None
        elif len(inorder)>1:
            rootNum=postorder[-1]
            root=TreeNode(postorder[-1])
            splitLInorder=inorder[:inorder.index(rootNum)]
            splitRInorder=inorder[inorder.index(rootNum)+1:]
            splitLPostorder=postorder[:inorder.index(rootNum)]
            splitRPostorder=postorder[inorder.index(rootNum):-1]
            root.left=self.buildTree(splitLInorder,splitLPostorder)
            root.right=self.buildTree(splitRInorder,splitRPostorder)
            return root
            