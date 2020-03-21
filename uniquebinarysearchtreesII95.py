# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def createTrees(start,end):
            resultL =[]
            if start > end:
                return [None]
            for i in range(start, end+1):
                rootILeftList = createTrees(start,i-1)
                rootIRightList = createTrees(i+1,end)
                for rootL in rootILeftList:
                    for rootR in rootIRightList:
                        newRoot = TreeNode(i)
                        # newRoot.left = rootL if rootL == None else TreeNode(rootL.val)
                        # newRoot.right = rootR if rootR == None else TreeNode(rootR.val)
                        newRoot.left = rootL 
                        newRoot.right = rootR
                        resultL.append(newRoot)
            return resultL
        if n == 0:
            return []
        return createTrees(1, n)
