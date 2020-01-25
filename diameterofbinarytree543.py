Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #find out the diameter for all nodes. 
        # for an individual node, 
        # the diameter would be leftnode's length + rightnode's length.
        self.maxDia = 0
        if root == None:
            return 0
        def dfs(node):
            if node == None:
                return 0
            leftL = rightL =1
            if node.left:
                leftL = 1 + dfs(node.left)
            if node.right:
                rightL = 1 + dfs(node.right)
            self.maxDia = max(leftL+rightL -1,self.maxDia) # have to substract one because leftL and rightL have an overlapping node which is the node in this recursion
            return max(leftL,rightL,1)
        dfs(root)
        return self.maxDia-1 #self.maxDia is actually the number of nodes. So we need to distract 1 to get the length. 
class Solution2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #mark the largest diameter using self.maxDia
        # for an individual node, 
        # the nodes in this diameter stripe is leftLength + right length +1(which is the node itself.) but to calculate distance, we need to substract 1. 
        self.maxDia = 0
        if root == None:
            return 0
        def dfs(node):
            if node == None:
                return 0
            leftL = rightL =0
            if node.left:
                leftL = dfs(node.left)
            if node.right:
                rightL = dfs(node.right)
            self.maxDia = max(leftL+rightL +1,self.maxDia) # have to do a plus one. because in here we are calculating the left and right without the NODE. 
            return max(leftL,rightL)+1
        dfs(root)
        return self.maxDia-1 #self.maxDia is actually the number of nodes. So we need to distract 1 to get the length. 

SunnyNode = TreeNode(1)
SunnyNode.left = TreeNode(2)
SunnyNode.right = TreeNode(3)
SunnyNode.left.left = TreeNode(4)
SunnyNode.left.right = TreeNode(5)