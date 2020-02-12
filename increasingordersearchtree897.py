# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        #inorder traversal. then make a tree as what the question wants.
        stackL = []
        resultL =[]
        while True:
            if root:
                stackL.append(root)
                root = root.left
            elif stackL != []:
                currentN = stackL.pop(-1)
                resultL.append(currentN)
                root = currentN.right
            else:
                break
        lengthL = len(resultL)
        for i in range(lengthL-1):
            resultL[i].left = None
            resultL[i].right = resultL[i+1]
        resultL[-1].left = None #the last one needs to be taken care of seperately
        resultL[-1].right = None # the last one needs to be taken care of seperately
        return resultL[0]
class Solution:
    def increasingBST(self,root):
        #reminded by the solutions on leetcode. use a pseudo node to traverse on the fly. very good trick.
               
        self.pseudoNode = answerNode = TreeNode(None) 
        def dfs(node):
            if node.left:
                dfs(node.left)
            node.left = None
            self.pseudoNode.right = node
            self.pseudoNode = self.pseudoNode.right
            if node.right:
                dfs(node.right) 
        dfs(root)
        return answerNode.right 
class Solution:
    def increasingBST(self,root):
        #reminded by the solutions on leetcode. use a pseudo node to traverse on the fly. very good trick.
               
        pseudoNode = answerNode = TreeNode(None) 
        def dfs(node):
            if node.left:
                dfs(node.left)
            node.left = None
            pseudoNode.right = node
            pseudoNode = pseudoNode.right
            if node.right:
                dfs(node.right) 
        dfs(root)
        return answerNode.right 
