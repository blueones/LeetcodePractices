# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node,value):
            #return current node's cumulative sum.
            if node != None:
                valueC = dfs(node.right,value)
                node.val += valueC
                return dfs(node.left,node.val)
            else:
                return value
        dfs(root,0)
        return root
sunnyNode = TreeNode(0)
sunnyNode.left = TreeNode(-1)
sunnyNode.left.left = TreeNode(-3)
print(Solution().convertBST(sunnyNode))

class Solution1:
    #reverse inorder traversal to sum and fuzhi.
    
    def convertBST(self,root):
        self.sumCurrent = 0
        def inorder(node):
            if node != None:
                inorder(node.right)
                self.sumCurrent += node.val
                node.val = self.sumCurrent
                inorder(node.left)
        head = root
        inorder(head)
        return root
        

