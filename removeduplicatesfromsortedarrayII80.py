class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slower = 0
        lenN = len(nums)
        for faster in range(lenN):
            if faster != 0 and nums[faster]!= nums[slower]:
                slower+=1
                nums[slower]=nums[faster]
            elif faster!= 0 and nums[faster] == nums[slower]:
                
                if slower==0 or (slower-1>=0 and nums[slower-1]!=nums[faster]):
                    slower+=1
                    nums[slower]= nums[faster]
        return slower+1
