class Solution1:
    def subsetsWithDup(self, nums):
        lenN = len(nums)
        if lenN == 0:
            return []
        nums.sorted()
        self.result = [[]]
        last = nums[0]
        for i in range(0, lenN, 1):
            
        return self.result

