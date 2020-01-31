# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #recursive
        # this question is different from lowest common ancestor os a binary tree. 
        #bst has its traits that can help make the solution simpler. 
        #if both p and q are on the left side or right side of the node. keep going to that side.
        # when p and q are not on one side of the node. that means you've reached the lowest common ancestor.
        if root == None:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root



class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #iterative. 
        # find the split point where p and q won't be in the same subtree.
        self.p = p
        self.q = q
        self.resultNode = None
        def iterativeDFS(node):
            stackList = [root]
            while stackList != []:
                currentNode = stackList.pop(-1)
                if currentNode.val > p.val and currentNode.val > q.val:
                    stackList.append(currentNode.left)
                elif currentNode.val < p.val and currentNode.val < q.val:
                    stackList.append(currentNode.right)
                else:
                    self.resultNode = currentNode
        if root == None:
            return None
        iterativeDFS(root)
        return self.resultNode