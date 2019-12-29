# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root==None:
            return True
        else:
            if root.left!=None and root.left.val<root.val and root.right==None:
                return self.isValidBST(root.left)
            if root.right!=None and root.right.val>root.val and root.left==None:
                return self.isValidBST(root.right)
            if root.right!=None and root.left!=None:
                if root.right.val>root.val and root.left.val<root.val:
                    return (self.isValidBST(root.left) and self.isValidBST(root.right))
            elif root.right==None and root.left==None:
                return True


class Solution1:
    def isValidBST(self, root):
        def dfs(root,left,right):
            if root==None:
                return True
            if root.val<=left or root.val>=right:
                return False
            return dfs(root.left,left, root.val) and dfs(root.right,root.val,right)
            
        return (dfs(root,float('-inf'),float('inf')))


class Solution2:
    def isValidBST(self,root):
        def dfs(root,_min,_max):
            if not root:
                return True
            if root.val<=_min or root.val>=_max:
                return False
            return dfs(root.left,_min,root.val) and dfs(root.right,root.val,_max)
        return dfs(root,float('-inf'),float('inf'))
SunnyTree = TreeNode(10)
SunnyTree.left = TreeNode(5)
SunnyTree.right = TreeNode(15)
SunnyTree.right.left=TreeNode(6)
SunnyTree.right.right=TreeNode(20)


'''SunnyTree.right.left = TreeNode(3)
SunnyTree.right.right = TreeNode(3)'''

print(Solution1().isValidBST(SunnyTree))