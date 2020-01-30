# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        #use N to mark. 
        queueList = [root]
        resultList = []
        while queueList != []:
            num = n = len(queueList)
            listLevel = 0
            while n > 0:
                currentNode = queueList.pop(0)
                listLevel += currentNode.val
                if currentNode.left:
                    queueList.append(currentNode.left)
                if currentNode.right:
                    queueList.append(currentNode.right)
                n -= 1
            resultList.append(listLevel/num)
        return resultList
class Solution1:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        #use N to mark. 
        queueList = [root]
        resultList = []
        while queueList != []:
            n = len(queueList)
            sum1 = 0
            for item in queueList:
                sum1 += item.val
            ave = sum1/n
            resultList.append(ave)
            while n > 0:
                currentNode = queueList.pop(0)
                if currentNode.left:
                    queueList.append(currentNode.left)
                if currentNode.right:
                    queueList.append(currentNode.right)
                n -= 1    
        return resultList
class Solution2:
    def averageOfLevels(self,root):
        queueList = [root]
        newQueue = []
        sumLevel = 0
        sumN = 0
        resultL = []
        while queueList != []:
            currentNode = queueList.pop(0)
            sumLevel += currentNode.val
            sumN += 1
            if currentNode.left:
                newQueue.append(currentNode.left)
            if currentNode.right:
                newQueue.append(currentNode.right)
            if queueList == []:
                queueList = newQueue
                newQueue = []
                resultL.append(sumLevel/sumN)
                sumLevel = sumN = 0
        return resultL
                