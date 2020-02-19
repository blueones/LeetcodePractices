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
class Solution1:
    def bstFromPreorder(self,preorder):
        #recursive solution. 
        self.index = 0
        
        def helper(lower = float('-inf'), upper = float('inf')):
            if self.index>= len(preorder) or preorder[self.index]> upper or preorder[self.index] < lower:
                return None
            root = TreeNode(preorder[self.index])
            self.index += 1
            root.left = helper(lower, root.val)
            root.right = helper(root.val, upper)


            return root
        return helper()
class Solution2:
    def bstFromPreorder(self,preorder):
        #iterative solution written by self.
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        stackList = [root]
        for i in range(1, len(preorder)):
            currentNode = TreeNode(preorder[i])
            if stackList!=[] and preorder[i] > stackList[-1].val:
                while stackList and currentNode.val > stackList[-1].val:
                    last = stackList.pop(-1)
                last.right = currentNode
                stackList.append(currentNode)
            elif stackList!=[] and preorder[i] < stackList[-1].val:
                stackList[-1].left = currentNode
                stackList.append(currentNode)
            elif stackList == []:
                stackList.append(currentNode)
        return root