# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        #tree construction. insertion
        if preorder == []:
            return None
        self.root = TreeNode(preorder[0])
        for i in range(1, len(preorder),1):
            self.insert(preorder[i])
        return self.root
    def insert(self,newItem):
        pre = self.root

        while pre:
            if pre.val > newItem:
                preP = pre
                pre = pre.left
            elif pre.val < newItem:
                preP = pre
                pre = pre.right
        currentNode = TreeNode(newItem)
        if preP.val > newItem:
            preP.left = currentNode
        else:
            preP.right = currentNode