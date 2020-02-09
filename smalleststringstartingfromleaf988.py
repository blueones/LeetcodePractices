# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root):
        self.answer = "~"
        def dfs(node, stringP):
            if node:
                currentString = stringP + chr(node.val + ord("a")) #quick way of transforming numbers to characters. mark the use of ord() and chr()
                if node.left == None and node.right == None:
                    self.answer = min(self.answer, currentString[::-1])
                dfs(node.left,currentString)
                dfs(node.right, currentString)
        dfs(root,"")
        return self.answer
            