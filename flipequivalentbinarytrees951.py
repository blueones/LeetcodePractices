# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == None and root2 == None:
            return True
        elif root1 != None and root2 != None:
            if root1.val == root2.val:
                return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
            else:
                return False
        else:
            return False
class Solution1:
    #used yield, zip, all
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs_print(root):
            if root != None:
                yield root.val
                L = root.left.val if root.left != None else -1
                R = root.right.val if root.right != None else -1
                if L <= R:
                    yield from dfs_print(root.left)
                    yield from dfs_print(root.right)
                else:
                    yield from dfs_print(root.right)
                    yield from dfs_print(root.left)
            else:
                yield -1
        return all([x == y for x, y in zip(dfs_print(root1), dfs_print(root2))])