# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # divide and conquer
        #recursion
        #generate new list for every recursion. Not ideal for space and time complexity.
        
        lenS = len(nums)
        if lenS == 0:
            return None
        midIndex = lenS//2
        headNode = TreeNode(nums[midIndex])
        headNode.left = self.sortedArrayToBST(nums[:midIndex])
        headNode.right = self.sortedArrayToBST(nums[midIndex+1:])
        return headNode
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #only access one list. better than solution1 in time and space complexity
        #include left margin but left out right margin.
        lenS = len(nums)
        def dfs(left, right):
            if left == right:
                return None
            midIndex = (left+right)//2
            headNode = TreeNode(nums[midIndex])
            if midIndex-1>= left:
                headNode.left = dfs(left,midIndex)
            headNode.right = dfs(midIndex+1,right)
            return headNode
        return dfs(0,lenS)
class Solution3:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #only access one list. better than solution1 in time and space complexity
        #include left and right margins. so left can be equal to right. 
        lenS = len(nums)
        def dfs(left, right):
            if left > right: #included left and right margins, so left can be equal to right
                return None
            midIndex = (left+right)//2
            headNode = TreeNode(nums[midIndex])
            if midIndex-1>= left:
                headNode.left = dfs(left,midIndex-1)
            headNode.right = dfs(midIndex+1,right)
            return headNode
        return dfs(0,lenS-1)