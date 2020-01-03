# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        #BFS to get nodes from each layer
        #save into a list of list
        #then get the last of each layer
        if root==None:
            return []
        layerNodes=[]
        #create list to store nodes in each layer.
        listofList=[]
        resultL=[]
        layerNodes.append(root)
        listofList.append(layerNodes[-1].val)
        
        while layerNodes:
            newLayer=[]
            print(listofList)
            while layerNodes:
                node=layerNodes.pop(0)
                if node.left:
                    #print(node.left.val)
                    newLayer.append(node.left)
                if node.right:
                    #print(node.right.val)
                    newLayer.append(node.right)
            if newLayer==[]:
                #print(listofList)
                break
            layerNodes=newLayer
            listofList.append(layerNodes[-1].val)
        return listofList

SunnyNode=TreeNode(1)      
SunnyNode.left=TreeNode(2)
SunnyNode.right=TreeNode(3)  
SunnyNode.left.left=TreeNode(4)
SunnyNode.left.right=TreeNode(5)
SunnyNode.right.left=TreeNode(6)  
SunnyNode.right.right=TreeNode(7)  

print(Solution().rightSideView(SunnyNode))
