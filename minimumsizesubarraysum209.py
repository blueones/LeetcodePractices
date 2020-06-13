class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #sliding window
        if nums == []:
            return 0
        start = 0
        end = 0
        sum_curr = nums[0]
        min_len = 1 if sum_curr >= s else float("inf")
        for index in range(1, len(nums)):
            end += 1
            sum_curr += nums[index]
            if sum_curr >= s:
                while sum_curr >= s and start < len(nums):
                    sum_curr -= nums[start]
                    
                    start += 1
                start-= 1
                sum_curr += nums[start]
                min_len = min(min_len, end-start+1)
        return min_len if min_len != float("inf") else 0
            