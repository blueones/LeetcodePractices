from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        #if target == 0 now, shouldn't initiate new color
        # have options to choose between N colors for each house really unless you can't initiate a new color.
        @lru_cache
        def backtracking(index, target, current_color):
            if target < 0:
                return float("inf")
            else:
                if index == len(houses):
                    if target == 0:
                        return 0
                    return float("inf")
                else:
                    if houses[index]== 0:
                        min_cost = float("inf")
                        for color in range(1,n+1,1):
                            if color != current_color:
                                
                                this_cost = cost[index][color-1] + backtracking(index+1, target-1, color)
                            else:
                                if index == 0:
                                    
                                    this_cost = cost[index][color-1]+ backtracking(index+1, target-1, color)
                                else:
                                    this_cost = cost[index][color-1]+ backtracking(index+1, target, color)
                            
                            min_cost = min(min_cost, this_cost)

                        return min_cost
                    else:

                        if current_color != houses[index]:

                            this_cost = backtracking(index+1, target-1, houses[index])

                            return this_cost
                        else:
                            if index==0:
                                target = target - 1
                            return backtracking(index+1, target, houses[index])
                        
        if houses ==[]:
            return 0
        else:
            min_cost = float("inf")
            for color in range(1,n+1, 1):
                color_cost = backtracking(0, target, color)
                
                min_cost = min(min_cost, color_cost)
            
            return min_cost if min_cost != float("inf") else -1