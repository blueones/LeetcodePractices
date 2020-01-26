# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        #brute force. go thru each node, and for that node leading subtree, see if sum is met. 
        self.resultNum = 0


        def dfs(root):
            #traverse the tree to check each node
            testSum(root,sum)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        def testSum(node, currentSum):
            #check for this node, if there is any path with the target sum
            if node != None:
                if node.val == currentSum:
                    self.resultNum +=1
                if node.left:
                    testSum(node.left, currentSum - node.val)
                if node.right:
                    testSum(node.right,currentSum - node.val)




        if root == None:
            return 0

        
        dfs(root)
        return self.resultNum