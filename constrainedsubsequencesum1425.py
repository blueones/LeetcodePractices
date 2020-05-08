class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for i in range(len(nums)+1)]
        max_sum = float("-inf")
        for i in range(1, len(nums)+1):
            max_dpi = nums[i-1]
            for j in range(1, k+1):
                index = i-1 -j
                
                if index in range(len(nums)):
                    
                    sum_current = nums[i-1] + dp[index+1]
                    max_dpi = max(max_dpi, sum_current)
            dp[i] = max_dpi
            max_sum = max(dp[i], max_sum)
        return max_sum
class Solution1:
    def constrainedSubsetSum(self, nums, k):
        #improved with deque(monotonic queue)
        dp = [nums[0] for i in range(len(nums))]
        deq = deque()
        deq.append(0)
        max_sum = dp[0]
        for i in range(1, len(nums)):
            if deq and deq[0] >= i-k:
                dp[i] = max(nums[i] + deq[0], nums[i])
            if deq and deq[0] == i-k:
                deq.popleft()
            while deq and deq[-1] < dp[i]:
                deq.pop()
            deq.append(i)
            max_sum = max(dp[i], max_sum)
        return max_sum