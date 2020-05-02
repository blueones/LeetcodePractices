# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        len_arr = len(arr)
        def checkingHelper(node, index):
            if node == None:
                if index == len_arr:
                    return True
                else:
                    return False
            else:
                
                if index< len_arr and node.val == arr[index]:
                    return checkingHelper(node.left, index+1) or checkingHelper(node.right, index+1)
                else:
                    return False
        return checkingHelper(root, 0)