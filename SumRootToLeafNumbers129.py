# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''root=TreeNode(2)
root.left=TreeNode(1)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.left.left=TreeNode(4)
root.left.left.left.left.left=TreeNode(8)
root.left.left.left.left.left.left=TreeNode(3)
root.left.left.left.left.left.left.left=TreeNode(6)
root.left.left.left.left.left.left.left.left=TreeNode(4)
root.left.left.left.left.left.left.left.left.left=TreeNode(7)'''
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
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
        self.sum=0
        #self.sum is the sum of all the path numbers. it gets incremented at leaf.
        #newnumber is to root so far what the path-generated-number is right now. new number is the number*10+root.val

        def dfs(root, number):
            if root.left ==None and root.right==None:
                self.sum+=number*10+root.val
                return
            else:
                newnumber=number*10+root.val
                if root.left:
                    dfs(root.left,newnumber)
                if root.right:
                    dfs(root.right,newnumber)
                return
        if not root:
            return 0
        else:
            dfs(root,0)
        return int(self.sum)




from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = deque()
        if root == None:
            return 0
        stack.append((root, 0))
        while stack:
            current_node, current_num = stack.pop()
            new_sum = current_num*10 + current_node.val
            if current_node.left == None and current_node.right == None:
                root_to_leaf += new_sum
            if current_node.left:
                stack.append((current_node.left, new_sum))
            if current_node.right:
                stack.append((current_node.right, new_sum))
        return root_to_leaf
            