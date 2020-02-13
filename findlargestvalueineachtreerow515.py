# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # BFS
        resultL = []
        if root == None:
            return resultL
        queueList = [root]
        
        while queueList:
            numberL = len(queueList)
            maxN = float("-inf")
            while numberL >0:
                currentN = queueList.pop(0)
                maxN = max(maxN, currentN.val)
                if currentN.left:
                    queueList.append(currentN.left)
                if currentN.right:
                    queueList.append(currentN.right)
                numberL -= 1
            resultL.append(maxN)
        return resultL