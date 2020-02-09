# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #preorder traversal recursion with a class variable
        self.resultL = []
        if root == None:
            return self.resultL
        
        def dfs(node):
            if node:
                self.resultL.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.resultL

class Solution1:
    def preorderTraversal(self,root):
        #iterative solution
        if root == None:
            return []
        stackL = [root]
        resultL = []
        while stackL != []:
            currentNode = stackL.pop(-1)
            resultL.append(currentNode.val)
            if currentNode.right:
                stackL.append(currentNode.right)
            if currentNode.left:
                stackL.append(currentNode.left)
        return resultL