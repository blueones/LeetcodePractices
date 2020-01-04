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
            elif t==None and s!=None:
                return False
            elif t!=None and s==None:
                return False
            else:
                if s.val==t.val:
                    #print("s is ",s.val,"t is ",t.val)
                    leftR=rightR=False
                    leftR=comparetrees(s.left,t.left)
                    rightR=comparetrees(s.right,t.right)
                    #print(leftR and rightR, "return for this level")
                    return leftR and rightR
            return False

        
        if s.val==t.val:
            if comparetrees(s,t):
                return True
            else:
                leftR=rightR=False
            if s.left:
                leftR= self.isSubtree(s.left,t)
                print("should've been here")
                if leftR:
                    return leftR
            if s.right:
                rightR= self.isSubtree(s.right,t)
                if rightR:
                    return rightR
        else: 
            print("here?")
            leftR=rightR=False
            if s.left:
                leftR= self.isSubtree(s.left,t)
                print("should've been here")
                if leftR:
                    return leftR
            if s.right:
                rightR= self.isSubtree(s.right,t)
                if rightR:
                    return rightR
        return False

# sunnynode=TreeNode(3)
# sunnynode.left=TreeNode(4)
# sunnynode.right=TreeNode(5)
# sunnynode.left.left=TreeNode(1)
# sunnynode.left.right=TreeNode(2)
# sunny=TreeNode(4)
# sunny.left=TreeNode(1)
# sunny.right=TreeNode(2)
 
sunnynode=TreeNode(1)
sunnynode.left=TreeNode(1)
sunny=TreeNode(1)
print(Solution().isSubtree(sunnynode,sunny))