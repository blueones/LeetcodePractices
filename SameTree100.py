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
        if p == None and q == None:
            return True
        else:
            if p != None and q != None:
                if p.val == q.val:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
            return False
from collections import deque
class Solution1:
    #iterative
    def isSameTree(self,p,q):
        queue = deque()
        queue.append((p,q))
        while queue:
            current_p, current_q = queue.popleft()
            if current_p == None and current_q == None:
                continue
            elif current_p != None and current_q != None:
                if current_p.val == current_q.val:
                    queue.append((current_p.left, current_q.left))
                    queue.append((current_p.right, current_q.right))
                else:
                    return False
            else:
                return False
        return True