class Solution:
    def climbStairs(self, n):
        Dp=[0]*n
        for i in range(1,n+1,1):
            if i>2:
                Dp[i-1]=Dp[i-3]+Dp[i-2]
            elif i==2:
                Dp[i-1]=2
            elif i==1:
                Dp[0]=1
        return Dp[n-1]
        

Solution().climbStairs(10)