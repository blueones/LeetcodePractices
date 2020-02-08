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
        

class Solution2:
    def convertBST(self, root: TreeNode) -> TreeNode:
        #iterative method Iterative reverse inorder traversal.
        stackList = list()
        self.currentSum = 0
        node = root
        while True:
            if node:
                stackList.append(node)
                node = node.right
                #print(stackList[-1].val)
            elif stackList != []:
                currentNode = stackList.pop(-1)
                #print(currentNode.val)
                currentNode.val += self.currentSum
                self.currentSum = currentNode.val
                node = currentNode.left
            else:
                break
            
        return root
        