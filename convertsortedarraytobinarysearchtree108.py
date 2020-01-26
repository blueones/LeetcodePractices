# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # divide and conquer
        #recursion
        
        lenS = len(nums)
        if lenS == 0:
            return None
        midIndex = lenS//2
        headNode = TreeNode(nums[midIndex])
        headNode.left = self.sortedArrayToBST(nums[:midIndex])
        headNode.right = self.sortedArrayToBST(nums[midIndex+1:])
        return headNode