
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        #find the smallest of node's right subtree. so it's knowing the root of the subtree, and find the leftmost node(inorder traversal first)
        #use the iterative inorder traversal of tree idea. go backwards...
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        flag = node.parent   
        while flag:
            flag = flag.parent
            if flag.val > node.val:
                return flag
        return None
            
        