# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
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
            
class Solution2:
    def levelOrder(self,root):
        if root == None:
            return []
        queueList = [root]
        newqueue = []
        resultL = []
        levelR = []
        while queueList != []:
            
            currentNode = queueList.pop(0)
            levelR.append(currentNode.val)
            if currentNode.left:
                newqueue.append(currentNode.left)
            if currentNode.right:
                newqueue.append(currentNode.right)
            if queueList == []:
                resultL.append(levelR)
                levelR = []
                queueList = newqueue
                newqueue = []
        return resultL




        