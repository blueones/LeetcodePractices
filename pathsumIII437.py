# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
class Solution2:
    def pathSum(self, root, target):
        #optimized. two sum method. memorize the intermediate results. 
        # in the brute force solution, we did a lot of repeated calculation. 
        # for example, 1 -> 3 -> 5, we did 1, 1+3, 1+3=5, 3, 3+5, 5
        # this is a classic "space and time tradeoff". we can create a dictionary to save all the path sum and their frequency.
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
