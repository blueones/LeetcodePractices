# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        return self.sumP(root,0,sum,[])
    def sumP(self,root,CurrentS,sum,listN):
        if root==None:
            CurrentS=0
            return []
        if root!=None:
            listC=[root.val]
            CurrentS+=root.val
            listN+=listC
            listS=list()
            if root.left==None and root.right==None:
                if CurrentS==sum:
                    listS.append(listN)
            leftN=root.left
            listNleft=listN.copy()
            rightN=root.right
            listNright=listN.copy()
            leftsumP=list()
            rightsumP=list()
            if leftN:
                leftsumP=self.sumP(leftN,CurrentS,sum,listNleft)
            if rightN:
                rightsumP=self.sumP(rightN,CurrentS,sum,listNright)
            return listS+leftsumP+rightsumP


            
            