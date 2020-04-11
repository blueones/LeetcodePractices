# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.left = float("-inf")
        self.right = float("inf")
        def dfs(node):
            if node != None:
                if node.val >= target: # here node.val need to have equal too. otherwise it's going to miss the situation where node.val == target.
                    self.right = min(node.val, self.right)
                    dfs(node.left)
                elif node.val < target:
                    self.left = max(node.val, self.left)
                    dfs(node.right)
        dfs(root)
        return self.left if abs(target - self.left) < abs(target - self.right) else self.right
class Solution1:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.left = float("-inf")
        self.right = float("inf")
        def dfs(node):
            if node != None:
                if node.val >= target:
                    self.right = min(node.val, self.right)
                    dfs(node.left)
                elif node.val < target:
                    self.left = max(node.val, self.left)
                    dfs(node.right)
        dfs(root)
        return self.left if abs(target - self.left) < abs(target - self.right) else self.right
class Solution2:
    def closestValue(self,root,target):
        #iteratively inorder traverse this BST, so it's ordered from small to big. 
        stack = []
        min_value = float("-inf")
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop(-1)
                if root.val<target:
                    min_value = max(min_value,root.val)
                elif root.val>= target:
                    return min(min_value,root.val, key = lambda x:abs(x-target))
                root = root.right
            else:
                break

        return min_value    
class Solution3:
    def closestValue(self,root,target):
        #modification on top of solution1. eliminate class variable. 
        left = float("-inf")
        right = float("inf")
        def dfs(node,min_val,max_val):
            if node != None:
                if node.val >= target:
                    max_val= min(max_val,node.val)
                    min_kid, max_kid = dfs(node.left,min_val,max_val)
                elif node.val < target:
                    min_val= max(min_val,node.val)
                    min_kid, max_kid = dfs(node.right,min_val,max_val)
                return max(min_val,min_kid),min(max_val,max_kid)
            else:
                return min_val, max_val
        min_f, max_f= dfs(root,left,right)
        return min(min_f,max_f,key = lambda x:abs(x-target))
class Solution4:
    def closestValue(self,root,target):
        closest = root.val
        while root:
            closest = min(closest,root.val, key = lambda x:abs(x-target))
            root = root.left if root.val> target else root.right
        return closest
