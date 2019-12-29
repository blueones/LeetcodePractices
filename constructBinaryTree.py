# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TestTreeClass:
    def testReturn(self, preorder, inorder):


class Solution:
    def buildTree(self, preorder, inorder):
        #get first element of three batches, connect treeNodes
        if len(preorder)==1:
            return TreeNode(preorder[0])
        elif len(preorder)==0:
            return None

        else:
            #Split
            rootM=preorder[0]
            rootN=inorder.index(rootM)
            bunchLpre=preorder[1:rootN+1]
            bunchRpre=preorder[rootN+1:]
            bunchLin=inorder[0:rootN]
            bunchRin=inorder[rootN+1:]
            root=TreeNode(rootM)
            root.left=self.buildTree(bunchLpre,bunchLin)
            root.right=self.buildTree(bunchRpre,bunchRin)
            return root
            
            

        
        
        
    
    

