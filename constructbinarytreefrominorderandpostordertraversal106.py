# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        def build(inB, inE, postB, postE):
            if inB > inE:
                return None
            currentV = self.postorder[postE]
            node = TreeNode(currentV)
            if postB == postE:
                return node
            indexIn = self.inorder.index(currentV)
            node.left = build(inB,indexIn-1,postB, postB + indexIn- inB - 1)
            import pdb; pdb.set_trace()
            node.right = build(indexIn+1, inE,postB + indexIn- inB, postE - 1)
            return node
        lenI = len(inorder)
        return build(0, lenI-1, 0, lenI-1)
Solution().buildTree([9,3,15,20,7],[9,15,7,20,3])