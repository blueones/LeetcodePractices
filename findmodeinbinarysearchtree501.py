# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        self.resultL = {}
        if root == None:
            return []
        self.maxN = 1
        def dfs(root):
            if root:
                if root.val in self.resultL:
                    self.resultL[root.val] += 1
                    self.maxN = max(self.maxN,self.resultL[root.val])
                else:
                    self.resultL[root.val] =1
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
        dfs(root)
        result = []
        for nodeV in self.resultL:
            if self.resultL[nodeV] == self.maxN:
                result.append(nodeV)
        return result
class Solution1:
    def findMode(self,root):
        #Could you do that without using any extra space? 
        #try to make this better by taking advantage of BST trait which is that inorder traversal of a BST is ordered.
        if root == None:
            return []
        self.result = []
        self.target = None
        self.counter = 0
        self.counterMax = 0
        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                if root.val == self.target:
                    self.counter += 1
                    if self.counter > self.counterMax:
                        self.counterMax = self.counter
                        self.result = [root.val]
                    elif self.counter == self.counterMax:
                        self.result.append(root.val)
                elif root.val != self.target:
                    self.target = root.val
                    self.counter = 1
                    if self.counter > self.counterMax:
                        self.counterMax = self.counter
                        self.result = [root.val]
                    elif self.counter == self.counterMax:
                        self.result.append(root.val)
                if root.right:
                    inorder(root.right)
        inorder(root)
        return self.result
sunnyNode = TreeNode(1)
sunnyNode.right = TreeNode(2)
sunnyNode.right.left = TreeNode(2)
Solution1().findMode(sunnyNode)

class Solution2:
    def findMode(self,root):
        '''WRONG ANSWER.'''
        #Could you do that without using any extra space? 
        #try to make this better by taking advantage of BST trait which is that inorder traversal of a BST is ordered.
        if root == None:
            return []
        self.result = []
        def inorder(root,target, counter, counterMax):
            if root:
                if root.left:
                    inorder(root.left,target,counter,counterMax)
                if root.val == target:
                    counter += 1
                    if counter > counterMax:
                        counterMax = counter
                        self.result = [root.val]
                    elif counter == counterMax:
                        self.result.append(root.val)
                elif root.val != target:
                    target = root.val
                    counter = 1
                    if counter > counterMax:
                        counterMax = counter
                        self.result = [root.val]
                    elif counter == counterMax:
                        self.result.append(root.val,target,counter,counterMax)
                if root.right:
                    inorder(root.right)
        inorder(root, None, 0,0)
        return self.result