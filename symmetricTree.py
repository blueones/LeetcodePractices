# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#method 1, iterator stack. everytime compare p and q, if mirrored, then shove p.left, q.right, p.right, q.left into a stack, keep comparing two.. 
#None Nodes can also be shoved. just have to compare.
import Queue as queue

class Solution1:
    def isSymmetric(self,root):
        if not root:
            return True
        stackNodes=queue.Queue()
        nodeL=root.left
        nodeR=root.right
        stackNodes.put(nodeL)
        stackNodes.put(nodeR)
        while(not stackNodes.empty()):
            rightN=stackNodes.get()
            leftN=stackNodes.get()
            if not rightN and not leftN:
                continue
            elif not rightN or not leftN:
                return False
            elif rightN.val!=leftN.val:
                return False
            elif rightN.val==leftN.val:
                stackNodes.put(rightN.right)
                stackNodes.put(leftN.left)
                stackNodes.put(rightN.left)
                stackNodes.put(leftN.right)

        return True






#method 2, DFS compare, compare p.left, q.right, p.right, q.left. keep on going down. 

class Solution2:
    def isSymmetric(self, root):
        if not root:
            return True
        rootL=root.left
        rootR=root.right
        return self.checkLR(rootL,rootR)
        
    def checkLR(self,leftN,rightN):
        rootL=leftN
        rootR=rightN
        if not rootL and not rootR:
            return True
        elif not rootL or not rootR:
            return False
        elif rootL.val!=rootR.val:
            return False
        elif rootL.val==rootR.val:
            return self.checkLR(rootL.left,rootR.right) and self.checkLR(rootL.right,rootR.left)




#method3, for each line, see if line of values are symmetrical. 






'''
# class Solution:
#     def isSymmetric(self, root):
#         curLayer = [root]
#         while len(curLayer)>0:
#             print("This Layer is")
                
#             nextLayer = []
#             for i in curLayer:
#                 if i:
#                     nextLayer.append(i.left)
#                     nextLayer.append(i.right)
#             for a in range(len(nextLayer)):
#                 if nextLayer[a] is None and nextLayer[len(nextLayer)-1-a] is None:
#                     continue
#                 if nextLayer[a] is None or nextLayer[len(nextLayer)-1-a] is None:
#                     return False
#                 if nextLayer[a].val!=nextLayer[len(nextLayer)-1-a].val:
#                     return False
#                 else:
#                     continue
#             curLayer = nextLayer
#         return True


class Solution:
    def checkNextLevel(self,listofNodes):
        returnL=list()
        
        for i in listofNodes:
            if i!=None:
                if i.left!=None:
                    returnL.append(i.left)
                else: returnL.append(None)
                if i.right!=None:
                    returnL.append(i.right)
                else:returnL.append(None)
            
        return returnL

    def checktwoNodes(self,listofNodesL,listofNodesR):
        #get left and right nodesList's children lists
        
        leftnodeslist=self.checkNextLevel(listofNodesL)
        
        rightnodeslist=self.checkNextLevel(listofNodesR)
        
        if len(leftnodeslist)==0 and len(rightnodeslist)==0:
            return True
        elif len(leftnodeslist)!=len(rightnodeslist):
            return False
        elif len(leftnodeslist)==len(rightnodeslist):
            lengthofChildren=len(leftnodeslist)
            #compare left children list and right children list
            for i in range(lengthofChildren):
                if leftnodeslist[i]==None and rightnodeslist[lengthofChildren-i-1]==None:
                    continue

                elif leftnodeslist[i]==None or rightnodeslist[lengthofChildren-i-1]==None:
                    return False
                elif leftnodeslist[i].val==rightnodeslist[lengthofChildren-i-1].val:
                    
                    continue
                elif leftnodeslist[i].val!=rightnodeslist[lengthofChildren-i-1].val:
                    return False
            
            return self.checktwoNodes(leftnodeslist,rightnodeslist)
























        # for a in range(len(listofNodesL)):
        #     nodeL = listofNodesL[a]
        #     nodeR = listofNodesR[len(listofNodesR)-1-a]

        #     # Check is both None
        #     if nodeL is None and nodeR is None:
        #         continue

        #     # One is None
        #     if (nodeL is None and nodeR is not None) or (nodeL is not None and nodeR is None):
        #         return False
            
        #     # Check Two Value
        #     if nodeL.val == nodeR.val:
        #         continue
            
        #     if nodeL.val != nodeR.val:
        #         return False
        
        # newlistofNodesL=self.checkNextLevel(listofNodesL)
        # newlistofNodesR=self.checkNextLevel(listofNodesR)
        # if len(newlistofNodesL)==0 and len(newlistofNodesR)==0:
        #     return True
        # return self.checktwoNodes(newlistofNodesL,newlistofNodesR)
    def isSymmetric(self, root):
        if root==None:
            return True
        else:
            leftNewRoot=[root.left]
            rightNewRoot=[root.right]
            if root.left==None and root.left==None:
                return self.checktwoNodes(leftNewRoot,rightNewRoot)

            elif root.left==None or root.right==None:
                return False
            elif root.left.val!=root.right.val:
                return False
        
        return self.checktwoNodes(leftNewRoot,rightNewRoot)
        
 '''       
        
noderoot=TreeNode(1)
nodel1=noderoot.left=TreeNode(2)
noder1=noderoot.right=TreeNode(2)
nodel2l=nodel1.left=TreeNode(3)
nodel2r=nodel1.right=TreeNode(4)
noder1l=noder1.left=TreeNode(4)
noder1r=noder1.right=TreeNode(3)

print(Solution1().isSymmetric(noderoot))
