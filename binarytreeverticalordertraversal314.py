# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        verticalDict = dict()
        if root == None:
            return []
        queueList =[(root,0)] #intersting way to mark index. I was stuck here as I don't know how to mark index to each node. 
        minIndex = maxIndex = 0
        while queueList:
            currentNode,index = queueList.pop(0)
            minIndex = min(minIndex,index)
            maxIndex = max(maxIndex, index)
            if index not in verticalDict:
                verticalDict[index] = [currentNode.val]
            elif index in verticalDict:
                verticalDict[index].append(currentNode.val)
            verticalDict.get(index, list()).append(currentNode.val)
            if currentNode.left:
                queueList.append((currentNode.left,index-1))
            if currentNode.right:
                queueList.append((currentNode.right,index+1))
        resultL= [  ]
        for indexN in range(minIndex,maxIndex+1):
            if verticalDict[indexN]:
                resultL.append(verticalDict[indexN])
        return resultL
class Solution1:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        verticalDict = dict()
        if root == None:
            return []
        queueList =[(root,0)] #intersting way to mark index. I was stuck here as I don't know how to mark index to each node. 
        while queueList:
            currentNode,index = queueList.pop(0)
            if index not in verticalDict:
                verticalDict[index] = [currentNode.val]
            elif index in verticalDict:
                verticalDict[index].append(currentNode.val)
            if currentNode.left:
                queueList.append((currentNode.left,index-1))
            if currentNode.right:
                queueList.append((currentNode.right,index+1))
        verticalIndex = sorted(verticalDict.keys())
        resultL = []
        for index in verticalIndex:
            resultL.append(verticalDict[index])
        return resultL
