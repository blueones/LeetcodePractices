# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dictOfNodes = {}
        minX = maxX = 0
        minY = maxY = 0
        if root:
            queueNode = [(root,0,0)]
            while queueNode:
                currentNode,currentMarkX, currentMarkY = queueNode.pop(0)
                minX = min(minX, currentMarkX)
                maxX = max(maxX, currentMarkX)
                minY = min(minY, currentMarkY)
                maxY = max(maxY, currentMarkY)
                if (currentMarkX,currentMarkY) in dictOfNodes:
                        dictOfNodes[(currentMarkX,currentMarkY)].append(currentNode.val)
                        dictOfNodes[(currentMarkX,currentMarkY)].sort()
                else:
                    dictOfNodes[(currentMarkX,currentMarkY)]=[currentNode.val]
                if currentNode.left:
                    queueNode.append((currentNode.left,currentMarkX-1,currentMarkY-1))
                if currentNode.right:
                    queueNode.append((currentNode.right,currentMarkX+1,currentMarkY-1))
            resultL = []
            for x in range(minX, maxX+1):
                listX = []
                for y in range(maxY,minY-1, -1):
                    if (x,y) in dictOfNodes:
                        toadd = dictOfNodes[(x,y)]
                        listX.extend(toadd)
                resultL.append(listX)
            return resultL


            

