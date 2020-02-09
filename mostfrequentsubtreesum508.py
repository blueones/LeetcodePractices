# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.dictR = dict()
        def dfs(node):
            if node:
                subTreeValue = node.val + dfs(node.left) +dfs(node.right)
                if subTreeValue in self.dictR:
                    self.dictR[subTreeValue] += 1
                else:
                    self.dictR[subTreeValue] = 1
                return subTreeValue
            elif node == None:
                return 0
        dfs(root)
        maxFrequency = 0
        for value in self.dictR:
            maxFrequency = max(self.dictR[value],maxFrequency)
        resultL = []
        for value in self.dictR:
            if self.dictR[value] = maxFrequency:
                resultL.append(value)
        return resultL
        

