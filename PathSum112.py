

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



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


class Solution1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #recursion written by self Jan 25th
        def dfs(node, sumC):
            if node.left == None and node.right==None:
                if sumC+node.val == sum:
                    return True
                # else:
                #     return False (not needed)
            left = right = False
            if node.left:
                left = dfs(node.left, sumC+node.val)
            if node.right:
                right = dfs(node.right,sumC+node.val)
            return left or right
        if root ==None:
            return False
        return dfs(root,0)
            
class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #iterative 
        if root == None:
            return False
        stackList = [(root,sum-root.val)]
        while stackList != []:
            # current = stackList.pop(-1)
            currentN, sumCurrent = stackList.pop(-1) #better than getting the whole tuple. since we will have to retrive the values in the tuple later. 
            #if current[0].left == None and current[0].right == None:
            if currentN.left == None and currentN.right == None:
                if sumCurrent==0:
                    return True
            if currentN.left:
                stackList.append(currentN.left, sumCurrent-currentN.left.val)
            if currentN.right:
                stackList.append(currentN.right, sumCurrent-currentN.right.val)
            
        return False        
class Solution3:
    def hasPathSum(self,root,sum):
        #recursive. deduct node values and see when reached the leaf, sum is 0. same thing as adding things up. 
        if root == None:
            return False
        if root.left == None and root.right ==None:
            if sum-root.val == 0:
                return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
                  
test = TreeNode(5)
test.left = TreeNode(4)
test.right = TreeNode(8)
test.left.left=TreeNode(11)
test.right.left=TreeNode(13)
test.right.right = TreeNode(4)
test.left.left.left=TreeNode(7)
test.left.left.right=TreeNode(2)
test.right.right.right=TreeNode(1)
print(Solution2().hasPathSum(test,22))