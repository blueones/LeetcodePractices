# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #
        self.resNode = None
        def dfs(head):
            if head == None:
                return False
            mid = True if head== p or head == q else False 
            #check if node is p or q. 
            # the check if left or right is p or q. 
            # if two out of three are True, then node is saved in result.
            #as parent of the result node, only one out of three are true. when head is on the node, it represents itself. 
            # when it's representing a whole subtree, then it's mid or left or right
            left = dfs(head.left)
            right = dfs(head.right)
            
            if mid + left + right >= 2:
                self.resNode = head
            return mid or left or right
        dfs(root)
        return self.resNode

        