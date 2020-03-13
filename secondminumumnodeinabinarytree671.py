# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = float("inf")
        minV = root.val
        def dfs(node):
            if node!= None:
                if node.val >minV and node.val < self.ans:
                    self.ans = node.val
                elif node.val == minV:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans!= inf else -1
class Solution1:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        #most intuitive recursion.
        def findlarger(node):
            if node.left:
                if node.left.val>node.val :
                    return min(node.left.val,findlarger(node.right)) if min(node.left.val,findlarger(node.right)) != -1 else node.left.val
                elif node.right.val>node.val:
                    return min(node.right.val,findlarger(node.left)) if min(node.right.val,findlarger(node.left)) != -1 else node.right.val
                elif node.left.val== node.val and node.right.val==node.val:
                    return min(findlarger(node.left),findlarger(node.right)) if min(findlarger(node.left),findlarger(node.right))!= -1 else max(findlarger(node.left),findlarger(node.right))
                
            else:
                return -1
        return findlarger(root)