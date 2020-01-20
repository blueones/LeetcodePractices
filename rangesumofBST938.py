# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        #use dfs or bfs to traverse
        self.L = L
        self.R = R
        def dfs(node):
            #calculate sum
            # find ending

            if node == None:
                return 0
            else:
                if node.val>= self.L and node.val <= self.R:
                    return node.val+dfs(node.left)+dfs(node.right)
                return dfs(node.left)+dfs(node.right)
        return dfs(root)
class Solution2:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        #use BFS to traverse
        queueN = []
        queueN.append(root)
        resultInt = 0
        while queueN !=[]:
            node = queueN.pop(0)
            if node.val >= L and node.val <= R:
                resultInt += node.val
            if node.left:
                queueN.append(node.left)
            if node.right:
                queueN.append(node.right)
        return resultInt
