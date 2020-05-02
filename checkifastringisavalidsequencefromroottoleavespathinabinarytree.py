# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        #wrong. failed at [8, 3, null, 2, 1, 5, 4], [8]
        # leaf definition is that node.left == None and node.right == None. 
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
class Solution1:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        len_arr = len(arr)
        def checkingHelper(node, index):
            if index < len_arr and node.val == arr[index]:
                if node.left == None and node.right == None:
                    if index == len_arr-1:
                        return True
                    else:
                        return False
                if node.left:
                    left_checking = checkingHelper(node.left, index+1)
                    if left_checking:
                        return True
                if node.right:
                    right_checking = checkingHelper(node.right, index+1)
                    return right_checking
            else:
                return False
                
        return checkingHelper(root, 0)