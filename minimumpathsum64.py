class Solution:
    def minPathSum(self, grid):
        #recursive solution without DP
        if grid == []:
            return 0
        row = len(grid)
        column = len(grid[0])
        self.min_sum = float("inf")
        
        def helper(row_index,column_index, current_sum):
            if row_index == row-1 and column_index == column-1:
                self.min_sum = min(self.min_sum,(current_sum+grid[row_index][column_index]))
            else:
                if row_index+1<row:
                    helper(row_index+1,column_index,current_sum+ grid[row_index][column_index])
                if column_index+1<column:
                    helper(row_index,column_index+1, current_sum+grid[row_index][column_index])
        helper(0,0,0)
        return self.min_sum
class Solution1:
    def minPathSum(self,grid):
        #DP, takes extra space dp as we are storing sums. 
        if grid == []:
            return 0
        row = len(grid)
        column = len(grid[0])
        dp = [[float("inf") for i in range(column)] for j in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(column):
                if i-1>=0:
                    dp[i][j]= min(dp[i][j],dp[i-1][j]+grid[i][j])
                if j-1>=0:
                    dp[i][j]= min(dp[i][j],dp[i][j-1]+grid[i][j])
        return dp[row-1][column-1]
Solution1().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
class Solution2:
    def minPathSum(self,grid):
        #DP, takes no extra space. 
        if grid == []:
            return 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if i-1>=0 and j-1>= 0:
                    grid[i][j]= grid[i][j]+ min(grid[i][j-1],grid[i-1][j])
                elif i-1>=0:
                    grid[i][j]= grid[i][j]+ grid[i-1][j]
                elif j-1>=0:
                    grid[i][j]= grid[i][j]+ grid[i][j-1]

        return grid[row-1][column-1]