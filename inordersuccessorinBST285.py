# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        #inorder traversal of the BST. 
        stackList = []
        flag = False
        while True:
            if root:
                stackList.append(root)
                root = root.left
            elif stackList:
                currentNode = stackList.pop(-1)
                if flag == True:
                    self.answer = currentNode
                    break
                if currentNode == p:
                    flag == True
                root = currentNode.right
            else:
                break
        return self.answer

