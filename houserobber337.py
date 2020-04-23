# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfsRob(root)[0],self.dfsRob(root)[1])
    def dfsRob(self,root):
        #return[userootmax,nouserootmax]
        if root==None:
            rootMax=0
            rootlessMax=0
        if root!=None:
            rootleftMax,rootleftlessMax=self.dfsRob(root.left)
            rootrightMax,rootrightlessMax=self.dfsRob(root.right)
            rootMax=root.val+rootleftlessMax+rootrightlessMax
            rootlessMax=max(rootleftMax,rootleftlessMax)+max(rootrightMax,rootrightlessMax)
        return [rootMax,rootlessMax]