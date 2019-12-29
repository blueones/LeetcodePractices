# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root=TreeNode(2)
root.left=TreeNode(1)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.left.left=TreeNode(4)
root.left.left.left.left.left=TreeNode(8)
root.left.left.left.left.left.left=TreeNode(3)
root.left.left.left.left.left.left.left=TreeNode(6)
root.left.left.left.left.left.left.left.left=TreeNode(4)
root.left.left.left.left.left.left.left.left.left=TreeNode(7)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        listAll=self.sumPath(root,[])
        print(listAll)
        listSum=[]
        for i in listAll:
            a=0
            
            for j in range(len(i)):
                num=i[j]*(10**(len(i)-j-1))
                print("num is",num)
                a+=num
            
            listSum.append(a)
        b=0
        for x in listSum:
            b+=x
        return b


    def sumPath(self,root,listC):
        if root==None:
            return []
        elif root!=None:
            listN=[root.val]
            listC+=listN
            listAll=[]
            if root.left==None and root.right==None:
                listAll.append(listC)
            leftN=root.left
            rightN=root.right
            leftlistC=listC.copy()
            rightlistC=listC.copy()
            if leftN!=None:
                leftlistAll=self.sumPath(leftN, leftlistC)
                listAll+=leftlistAll
            if rightN!=None:
                rightlistAll=self.sumPath(rightN,rightlistC)
                listAll+=rightlistAll
            return listAll


            
class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
print(Solution().sumNumbers(root))