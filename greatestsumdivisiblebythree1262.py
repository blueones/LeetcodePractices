class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod = nums[0]%3
        dp = [[0,0,0] for i in range(len(nums)+1)]
        max_triple = 0
        for index in range(1, len(nums)+1):
            mod = nums[index-1]%3
            dp[index][mod]= max(dp[index-1][0] + nums[index-1], dp[index-1][mod])
          
            dp[index][(mod+1)%3] = max(dp[index-1][1] + nums[index-1],dp[index-1][(mod+1)%3]) if dp[index-1][1]%3 == 1 else dp[index-1][(mod+1)%3]
         
            dp[index][(mod+2)%3] = max(dp[index-1][2] + nums[index-1],dp[index-1][(mod+2)%3]) if dp[index-1][2]%3 == 2 else dp[index-1][(mod+2)%3]
        
        return dp[len(nums)][0]