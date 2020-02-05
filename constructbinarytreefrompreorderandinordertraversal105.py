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