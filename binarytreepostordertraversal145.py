# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #recursion method
        self.resultL = []
        if root == None:
            return self.resultL
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.resultL.append(node.val)
        dfs(root)
        return self.resultL
class Solution1:
    def postorderTraversal(self,root):
        #iterative solution
        if root == None:
            return []
        stack1 = [root]
        stack2 = []
        resultL = []
        while stack1 != []:
            currentNode = stack1.pop(-1)
            stack2.append(currentNode)
            if currentNode.left:
                stack1.append(currentNode.left)
            if currentNode.right:
                stack1.append(currentNode.right)
        while stack2:
            resultL.append(stack2.pop(-1).val)
        return resultL

