# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #recursion method
        self.resultL = []
        if root == None:
            return self.resultL
        def dfs(node):
            if node.left:
                dfs(node.left)
            self.resultL.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return self.resultL
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #iterative method
        if root == None:
            return []
        stackList = []
        resultL = []
        while True:
            if root:
                stackList.append(root)
                root = root.left
            elif stackList:
                currentN = stackList.pop(-1)
                resultL.append(currentN.val)
                root = currentN.right
            else:
                break
        return resultL
                
