# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        #DFS, recursion. 
        self.answer = 0
        def dfs(node):
            currentL = currentR = currentB = True
            if node:
                if node.left:
                    if node.left.val!= node.val:
                        currentL = False
                if node.right:
                    if node.right.val != node.val:
                        currentR = False
                currentB = currentL and currentR
                leftB = dfs(node.left)
                rightB = dfs(node.right)
            
                if leftB and rightB and currentB:
                    self.answer += 1
            return currentB
        dfs(root)
        return self.answer
sunnyNode = TreeNode(5)
sunnyNode.left = TreeNode(1)
sunnyNode.right = TreeNode(5)
sunnyNode.left.left = TreeNode(5)
sunnyNode.left.right = TreeNode(5)
sunnyNode.right.right = TreeNode(5)

print(Solution().countUnivalSubtrees(sunnyNode))