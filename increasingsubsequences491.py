class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        #constructing a tree really
        self.resultL = []
        for num in nums:
            