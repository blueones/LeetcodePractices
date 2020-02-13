# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.NodeIndex = 0
        def dfs(in_left, in_right):
            #in_left: beginning of inorder elements left to construct subtree
            #in_right: end of inorder elements left to construct subtree
            if in_left == in_right:
                return None
            node = TreeNode(preorder[self.NodeIndex])
            self.NodeIndex += 1
            node.left = dfs(in_left, inorder.index(node.val))
            node.right = dfs(inorder.index(node.val)+1, in_right)
            return node
        return dfs(0, len(inorder))
class Solution1:
    def buildTree(self,preorder, inorder):
        # think hard about how preorder and inorder is being created. consider left and right as a big chunk of things.
        #  (left chunk) root (right chunk) inorder
        #  root (left chunk) (right chunk) preorder
        #  this solution use the location of root in inorder, to find out the length of left chunk and so the length of right chunk. 
        #  then recurse. 
        # when recurse, used left open right close to be able to catch everyone. 
        self.preorder = preorder
        self.inorder = inorder
        def build(preB, preE, inB, inE):
            if preB == preE: # this is only to screen out when input preorder is []
                return None
            currentV = self.preorder[preB]
            node = TreeNode(currentV)
            if preB + 1 == preE:
                return node # because when pre + 1 == preE, we already just return node. we are done recursing.
            indexNin = self.inorder.index(currentV)
            node.left = build(preB+1, preB+ indexNin- inB+1, inB, indexNin )
            node.right = build(preB + indexNin - inB +1, preE, indexNin+1, inE)
            return node
        lenL = len(preorder)
        return build(0, lenL, 0, lenL)

