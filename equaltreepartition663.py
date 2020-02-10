# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def checkEqualTree(self, root: TreeNode) -> bool:
        #calculating the sum of the tree and see if a subtree's sum is half of the whole tree's sum
        if root == None:
            return False
        def sum(node):
            if node:
                currentSum = node.val
                return node.val + sum(node.left)+ sum(node.right)
            else:
                return 0
        totalSum = sum(root)
        targetSum = totalSum/2
        self.answer = False
        def dfs(node):
            if node:
                currentSum = node.val + dfs(node.left) + dfs( node.right)
                if currentSum == targetSum:
                    self.answer = True
                return currentSum
            else:
                return 0
        dfs(root.left)
        dfs(root.right)
        return self.answer

class Solution2:
    def checkEqualTree(self,root):
        # solution 1 is doing great on space complexity and solution 2 is going to be doing good on time. since it will record all the subtree sums.
        if root == None:
            return False
        self.sumset = list() # don't use set. for test case [0, none, 0], it will result in a false even though it should've been true
        def sum(node):
            if node:
                currentSum = node.val+ sum(node.left)+ sum(node.right)
                self.sumset.append(currentSum)
                return currentSum
            else:
                return 0
        totalSum= sum(root)
        targetSum = totalSum/2
        self.sumset.pop(-1) # take out root's sum. 
        return targetSum in self.sumset

