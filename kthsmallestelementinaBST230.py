# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #inorder traverse. 
        inordertra = []
        def inorder(node):
            if node.left:
                inorder(node.left)

            inordertra.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return inordertra[k-1]
class Solution:
    def kthSmallest(self,root,k):
        #use stack to traverse, don't have to traverse the whole tree and don't have to save all in a list
        stackList = []
        pointer = 0
        while True:
            if root:
                stackList.append(root)
                root = root.left
            elif stackList!=[]:
                currentNode = stackList.pop(-1)
                pointer +=1
                if pointer == k:
                    return currentNode.val
                root = currentNode.right
            else:
                break
    