class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slower = 0
        lenN = len(nums)
        for faster in range(lenN):
            if faster != 0 and nums[faster]!= nums[slower]:
                slower+=1
                nums[slower]= nums[faster]
        return slower+1