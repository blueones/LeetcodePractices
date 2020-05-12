from collections import deque
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leafSequence(root):
            
            if root.left == None and root.right == None:
                return str(root.val)+"-"
            left = right = ""
            if root.left:
                left = leafSequence(root.left)
            if root.right:
                right = leafSequence(root.right)
            return left+right
            
        if leafSequence(root1) == leafSequence(root2):
            return True
        return False