# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator1:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.in_order_left(root)
    def in_order_left(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            topMost = self.stack.pop(-1)
            if topMost.right:
                self.in_order_left(topMost.right)
            return topMost.val
            

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack != []:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class BSTIterator2:
# flatten the tree into an array. time and space trade off. hasnext and next methods are O(1) but creating the object takes O(N)
    def __init__(self, root: TreeNode):
        self.listN = []
        def inorder(node):
            if node != None:
                if node.left:
                    inorder(node.left)
                self.listN.append(node.val)
                if node.right:
                    inorder(node.right)
        inorder(root)
        self.index = -1

    def next(self) -> int:
        """
        @return the next smallest number

        """
        self.index += 1
        return self.listN[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.index+1 < len(self.listN):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

    def next(self) -> int:
        while self.pointer:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left
        if self.stack:
            self.pointer = self.stack.pop()
            ans = self.pointer.val
            self.pointer = self.pointer.right
            return ans

    def hasNext(self) -> bool:
        return self.pointer or self.stack