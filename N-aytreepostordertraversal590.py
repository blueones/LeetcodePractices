
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution1:
    #recursion
    def postorder(self, root: 'Node') -> List[int]:
        #return a list of nodes values
        # when root is None
        if root != None:
            listN=[]
            for children in root.children:
                listN+=self.postorder(children)
            return listN+[root.val]
        elif root == None:
            return []
        
            


class Solution2:
    #iterative
    def postorder(self,root):
        if root == None:
            return []
        stackN = [root]
        resultList= []
        while stackN != []:
            nodeCurrent = stackN.pop(-1)
            resultList.insert(0,nodeCurrent.val)
            for children in nodeCurrent.children:
                if children != None:
                    stackN.append(children)
        return resultList
