def funa(n):
    if n>10:
        return True
    else:
        return False

def funb(x,y):
    res_a = funa(x)
    res_b = funa(y)
    if res_a and res_b:
        return True
    else:
        return False
print(funb(15,16))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(9)

#              1
#        2            9  
# [1,2,9]
# [1,3,10]




class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.luyibian(root,0,sum)

    def luyibian(self,root,current,sum):
        if root==None:
            return False
        else:
            current += root.val
            resultN=(root.left==None and root.right==None and current==sum)
            resultL=self.luyibian(root.left,current,sum)
            resultR=self.luyibian(root.right,current,sum)

            return resultR or resultL or resultN


            

Solution().luyibian(test,0,3)