from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #we have a monotonic queue that is increasing.
        deque_window = deque()
        for index in range(len(nums)):
            if deque_window:
                if deque_window[0]+limit >= nums[index] and deque_window[-1]-limit<= nums[index]:
                    