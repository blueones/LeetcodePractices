#solution: top down recursion with memo
from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        @lru_cache(None)
        def maxP(day, bought_price):
            if day >= days:
                return 0
            else:
                #next step to buy if bought_price == -1:
                #next step to sell if bought_price != -1
                if bought_price == -1:
                    max_gain = float("-inf")
                    for i in range(day, days):
                        max_gain = max(max_gain, maxP(i+1, prices[i]))
                    return max_gain
                else:
                    max_gain = float("-inf")
                    for i in range(day, days):
                        current_gain = prices[i] - bought_price
                        max_gain = max(max_gain, current_gain + maxP(i+2, -1))
                    return max_gain
        return maxP(0, -1)
#dp solution from the recursion+memo solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        days = len(prices)
        #bought, sold, rest+
        dp = [[float("-inf"), 0, 0] for i in range(days+1)]
        for i in range(1, days+1):
            #for the day it's index i-1 in prices. 
            dp[i][0] = max(dp[i-1][2] - prices[i-1], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + prices[i-1]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[days])
            
                        
                
#solution: state. p[i] only has something to do with p[i-1]

