from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        self.min_coin = float("inf")
        @lru_cache(None)
        def helper(coins_num, current ):
            if coins_num < self.min_coin:
                if current == amount:
                    self.min_coin = min(self.min_coin, coins_num)
                elif current < amount:
                    for i in coins:
                        helper(coins_num+1, current+i)
        helper(0, 0)
        return self.min_coin if self.min_coin!= float("inf") else -1
#lru_cache也可以套在没return的function上，没return其实是有implicit return which is None. 所以cache可以避免重复操作。

#DFS+剪枝
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        self.min_coin = float("inf")
        
        def helper(coins_num, current, index ):
            
            
            if index == len(coins)-1 :
                if(amount-current)%coins[index] == 0:
                    self.min_coin = min(self.min_coin, coins_num+ (amount-current)//coins[index])
                    
            else:
                current_num = (amount-current)//coins[index]
                
                
                for k in range(current_num, -1, -1):
                    #self.min_coin is being updated so need this step to constantly prune.
                    if coins_num+k >= self.min_coin:
                        break
                    helper(coins_num+k, current + k*coins[index], index+1)
        helper(0, 0, 0)
        return self.min_coin if self.min_coin!= float("inf") else -1
