# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if root==None:
            return [[]]
        flagList=list()
        flagList.append(root)
        resultL=list()
        resultL.append([root.val])
        while len(flagList)>0:
            newList=list()
            newListValues=list()
            for i in flagList:
                if i!=None:
                    newList.append(i.left)
                    newList.append(i.right)
                
            for values in newList:
                if values!=None:
                    newListValues.append(values.val)
            if len(newListValues)!=0:
                resultL.append(newListValues)
            flagList=newList
        return resultL
            


        