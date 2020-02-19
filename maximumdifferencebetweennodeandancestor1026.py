# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        #intuitive solution
        self.maxD = 0
        def dfs(node, parentList):
            for parent in parentList:
                diff = abs(parent.val - node.val)
                self.maxD = max(self.maxD, diff)
            if node.left:
                dfs(node.left, parentList+[node])
            if node.right:
                dfs(node.right, parentList+[node])
        dfs(root, [])
        return self.maxD
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        #improved solution. improved space. 
        self.maxD = 0
        self.parentList = []
        def dfs(node):
            for parent in self.parentList:
                diff = abs(parent.val - node.val)
                self.maxD = max(self.maxD, diff)
            if node.left:
                self.parentList.append(node)
                dfs(node.left)
                self.parentList.pop(-1) #backtracking. 
            if node.right:
                self.parentList.append(node)
                dfs(node.right)
                self.parentList.pop(-1) #backtracking
        dfs(root)
        return self.maxD
class Solution:
    def maxAncestorDiff(self,root)
    #mark the largest and smallest bumped into. then do a final abs().
        if root == None:
            return 0
        self.maxD = 0
        def dfs(node, maxN, minN):
            if node.val < minN:
                self.maxD = max(self.maxD,(maxN - node.val))
                minN = node.val
            elif node.val > maxN:
                self.maxD = max(self.maxD,(node.val - minN))
                maxN = node.val
            if node.left:
                dfs(node.left,maxN,minN)
            if node.right:
                dfs(node.right,maxN,minN)
        dfs(root,root.val,root.val)
        return self.maxD

