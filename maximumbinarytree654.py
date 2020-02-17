# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        #first intuition answer
        #not great. Since for everytime we look for the index for node, we are doing a sort.
        self.nums = nums
        def maxIndex(l,r):
            maxN = float("-inf")
            maxF = l
            for i in range(l,r):
                if self.nums[i]> maxN:
                    maxN = self.nums[i]
                    maxF = i
            return maxF
        def construct(l,r):
            if l>= r:
                return None
            indexM = maxIndex(l,r)
            node = TreeNode(self.nums[indexM])
            node.left = construct(l,indexM)
            node.right = construct(indexM+1,r)
            return node
        return construct(0, len(nums))

        


class Solution1:
    def constructMaximumBinaryTree(self,nums):
        # great solution but not intuitive
        

Solution().constructMaximumBinaryTree([3,2,1,6,0,5])