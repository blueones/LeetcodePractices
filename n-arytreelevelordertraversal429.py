
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        queueList = [root]
        newLevelQueue = []
        finalresultL = []
        resultL = []
        if root == None:
            return []
        while queueList:
            
            currentNode = queueList.pop(0)
            resultL.append(currentNode.val)
            for child in currentNode.children:
                newLevelQueue.append(child)
            if queueList == []:
                queueList = newLevelQueue
                newLevelQueue = []
                finalresultL.append(resultL)
                resultL = []
        return finalresultL
class Solution2:
    #andy's solution
    def levelOrder(self,root):
        if root == None:
            return []
        queueList = [root]
        finalResult = []
        while queueList:
            numberinlevel = len(queueList) #to mark current level's nodes. when done dealing with currentnode(in while numberinlevel >0 ), carry on with the next while loop
            resultListLevel = []
            while numberinlevel > 0:
                currentNode = queueList.pop(0)
                resultListLevel.append(currentNode.val)
                for child in currentNode.children:
                    queueList.append(child)
                numberinlevel -= 1
            finalResult.append(resultListLevel)
        return finalResult

                

            
        