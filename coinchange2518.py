from functools import lru_cache
class Solution:
    #bottomup+memo
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache
        def backtracking(index, current_amount):
            if current_amount >= amount:
                if current_amount == amount:
                    return 1
                return 0
            else:
                coin_correct = 0
                for i in range(index, len(coins)):
                    coin_correct += backtracking(i, current_amount + coins[i])
                return coin_correct
        return backtracking(0, 0)
class Solution1:
    # DP
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(amount+1):
                if i-coin >= 0:
                    dp[i] = dp[i]+ dp[i-coin]
        return dp[amount]
                    