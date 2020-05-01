class Solution:
    def maximalSquare(self, matrix) :
        #brutal force.
        max_square = 0
        if matrix == []:
            return max_square
        row = len(matrix)
        column = len(matrix[0])
        for row_index in range(row):
            for column_index in range(column):
                if matrix[row_index][column_index] == "1":
                    extend = min(row - 1 - row_index, column - 1 - column_index)
                    extend_checked = 1
                    flag = True
                    while extend_checked <= extend and flag:
                        
                        for row_checking in range(row_index, row_index+ extend_checked +1):
                            if matrix[row_checking][column_index+ extend_checked] == "0":
                                flag = False
                                break
                        if flag:
                            for column_checking in range(column_index, column_index+ extend_checked +1):
                                if matrix[row_index+ extend_checked][column_checking] == "0":
                                    flag = False
                                    break
                        if flag:
                            extend_checked += 1
                        else:
                            break
                            
                    
                        
                    max_square = max(max_square, extend_checked+1)
        return max_square**2
class Solution1:
    def maximalSquare(self, matrix):
        #DP
        #DP[i][j] represents with matrix[i][j] as the lower right corner, the largest square length 
        if matrix ==[]:
            return 0
        max_len = 0
        row = len(matrix)
        column = len(matrix[0])
        dp = [[0 for j in range(column+1)] for i in range(row+1)]
        for row_index in range(1, row+1):
            for column_index in range(1, column+1):
                if matrix[row_index-1][column_index-1] == "1":
                    dp[row_index][column_index] = min(dp[row_index-1][column_index], dp[row_index][column_index-1], dp[row_index-1][column_index-1]) + 1
                    max_len = max(max_len, dp[row_index][column_index])
        return max_len**2
class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #solution3 in LC solutions. do not need a matrix to save results. just one array is good. 
        if matrix ==[]:
            return 0
        max_len = 0
        row = len(matrix)
        column = len(matrix[0])
        dp = [0 for j in range(column+1)]
        
        for row_index in range(1, row+1):
            pre = 0
            for column_index in range(1, column+1):
                if matrix[row_index-1][column_index-1] == "1":
                    new_pre = dp[column_index]
                    dp[column_index] = min(dp[column_index], dp[column_index-1], pre) + 1
                    pre = new_pre
                    max_len = max(max_len, dp[column_index])
                else:
                    new_pre = dp[column_index]
                    dp[column_index] = 0
                    pre = new_pre
        return max_len**2
class Solution3:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #LC Solution 3. improve space complexity. 
        if matrix ==[]:
            return 0
        max_len = 0
        row = len(matrix)
        column = len(matrix[0])
        dp = [0 for j in range(column+1)]
        
        for row_index in range(1, row+1):
            pre = 0
            for column_index in range(1, column+1):
                new_pre = dp[column_index]
                if matrix[row_index-1][column_index-1] == "1":
                    
                    dp[column_index] = min(dp[column_index], dp[column_index-1], pre) + 1
                    max_len = max(max_len, dp[column_index])
                else:
                    dp[column_index] = 0
                pre = new_pre
        return max_len**2