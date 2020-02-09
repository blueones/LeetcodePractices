
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        stackList = [root]
        resultL = []
        while stackList:
            currentNode = stackList.pop(-1)
            resultL.append(currentNode.val)
            stackList.extend(currentNode.children[::-1])# append the children from right to left. 
        return resultL
