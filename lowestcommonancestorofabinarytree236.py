# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #recursion solution
        self.resNode = None
        def dfs(head):
            if head == None:
                return False
            mid = True if head== p or head == q else False 
            #check if node is p or q. 
            # the check if left or right is p or q. 
            # if two out of three are True, then node is saved in result.
            #as parent of the result node, only one out of three are true. when head is on the node, it represents itself. 
            # when it's representing a whole subtree, then it's mid or left or right
            left = dfs(head.left)
            right = dfs(head.right)
            
            if mid + left + right >= 2:
                self.resNode = head
            return mid or left or right
        dfs(root)
        return self.resNode
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

class Solution3:
    def lowestCommonAncestor(self, root, p, q):
        #written by self. iterative method.
        stackList = [root]
        parentDictionary = {root: None}
        while p not in parentDictionary or q not in parentDictionary:
            currentNode = stackList.pop(-1)
            if currentNode.left:
                parentDictionary[currentNode.left]=currentNode
                stackList.append(currentNode.left)
            if currentNode.right:
                parentDictionary[currentNode.right]=currentNode
                stackList.append(currentNode.right)
        ancestorsP = set()
        while p:
            ancestorsP.add(p)
            p = parentDictionary[p]
        while q not in ancestorsP:
            q = parentDictionary[q]
        return q