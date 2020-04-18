class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = start_val = 0
        for num in nums:
            start_val += num
            min_val = min(min_val,start_val)
        return 1-min_val
            
            