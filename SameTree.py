# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p!=None and q!=None:
            if p.val==q.val:
                leftP=p.left
                leftQ=q.left
                rightP=p.right
                rightQ=q.right
                if self.isSameTree(leftP,leftQ) and self.isSameTree(rightP,rightQ):
                    return True
        
        else:
            return False'''
class Solution:
    def isSameTree(self,p,q):
        if p==None and q==None:
            return True
        elif p!=None and q!=None:
            if p.val==q.val:
                pleft=p.left
                qleft=q.left
                pright=p.right
                qright=q.right
                return self.isSameTree(pleft,qleft) and self.isSameTree(pright,qright)
        else:
            return False