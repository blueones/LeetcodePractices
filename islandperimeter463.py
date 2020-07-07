class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    ans += 4
                    if i+1 < row and grid[i+1][j] == 1:
                        ans -= 2
                    if j+1 < column and grid[i][j+1] == 1:
                        ans -= 2
        return ans
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid == []:
            return 0
        row = len(grid)
        column = len(grid[0])
        visited = [False for i in range(row*column)]
        diffs = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(current_row, current_column):
            visited[current_row*column+current_column] = True
            count = 4
            morecount = 0
            
            for row_diff, column_diff in diffs:
                neighbor_row = current_row+row_diff
                neighbor_column = current_column + column_diff
                if neighbor_row >= 0 and neighbor_row < row and neighbor_column >= 0 and neighbor_column < column and grid[neighbor_row][neighbor_column] == 1 :
                    count -= 1
                    if visited[neighbor_row*column+neighbor_column] == False:
                        morecount += dfs(neighbor_row, neighbor_column)
            return count+morecount
        for i in range(row):
            for j in range(column):
                if visited[i*column+j] == False and grid[i][j] == 1:
                    return dfs(i, j)
                        