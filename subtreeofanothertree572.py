# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        #see if s.val==t.val
        # if not, see if s.left.val==t.val and s.right.val==t.val
        #if yes, then pass down until s==None and t==None
        def comparetrees(s,t):
            if s==t==None:
                return True
            elif s and t and s.val==t.val:
                return comparetrees(s.left,t.left) and comparetrees(s.right,t.right)
            return False

        if s and t:
            if s.val==t.val and comparetrees(s,t):
                    return True
            else: 
                return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        elif not (s or t):
            return True
        else:
            return False
                

sunnynode=TreeNode(3)
sunnynode.left=TreeNode(4)
sunnynode.right=TreeNode(5)
sunnynode.left.left=TreeNode(1)
sunnynode.left.right=TreeNode(2)
sunnynode.left.left.left=TreeNode(0)
sunny=TreeNode(4)
sunny.left=TreeNode(1)
sunny.right=TreeNode(2)
 
'''sunnynode=TreeNode(1)
sunnynode.left=TreeNode(1)
sunny=TreeNode(1)'''
print(Solution().isSubtree(sunnynode,sunny))