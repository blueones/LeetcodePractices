# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if root!=None:
            return self.binarynodetoleaf(root,"",[])
        


    def binarynodetoleaf(self,root,stringR,outputL):
        if stringR=="":
            stringR+=str(root.val)
        else:
            stringR+="->"
            stringR+=str(root.val)
        leftN=root.left
        rightN=root.right
        if leftN==None and rightN==None:
            outputL.append(stringR)
        if leftN!=None:
            self.binarynodetoleaf(leftN,stringR,outputL)
        if rightN!=None:
            self.binarynodetoleaf(rightN,stringR,outputL)
        return outputL

        
class Solution1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        self.listR = []
        def dfs(node, stringC):
            if stringC == "":
                stringC += str(node.val)
            else:
                stringC += "->"
                stringC += str(node.val)
            if node.left == None and node.right == None:
                self.listR.append(stringC)
            if node.left:
                dfs(node.left,stringC)
            if node.right:
                dfs(node.right,stringC)
        dfs(root,"")
        return self.listR