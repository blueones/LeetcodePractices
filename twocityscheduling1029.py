from functools import lru_cache
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #backtracking recursion+memo
        N = len(costs)//2
        @lru_cache
        def backtracking(index, currentA, currentB):
            if index == len(costs):
                return 0
            else:
                if currentA < N and currentB < N:
                    return min(costs[index][0]+backtracking(index+1, currentA+1, currentB), costs[index][1]+backtracking(index+1, currentA, currentB+1))
                elif currentA == N:
                    return backtracking(index+1, currentA, currentB+1)+ costs[index][1]
                elif currentB == N:
                    return backtracking(index+1, currentA+1, currentB)+costs[index][0]
        return backtracking(0, 0, 0)
class Solution2:
    def twoCitySchedCost(self, costs):
        #DP Solution
        N = len(costs)//2
        dp = [[0 for i in range(N+1)] for j in range(N+1)]
        
        for i in range(N+1):
            for j in range(N+1):
                if i== 0 and j==0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]+costs[i+j-1][1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]+ costs[i+j-1][0]
                else:
                
                    dp[i][j] = min(dp[i][j-1] + costs[i+j-1][1], dp[i-1][j]+ costs[i+j-1][0])
        return dp[N][N]
class Solution1:
    #greedy solution
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        half = len(costs)//2
        costs.sort(key = lambda x: (x[0]-x[1]))
        ans = 0
        for index in range(half):
            ans += costs[index][0]
        for index in range(half, len(costs)):
            ans += costs[index][1]
        return ans
        
            
            