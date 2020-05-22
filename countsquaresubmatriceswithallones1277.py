class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        column = len(matrix[0])
        def count(row_index, column_index, square):
            if row_index+square < row and column_index+square < column:
                for i in range(square+1):
                    if matrix[row_index+square][column_index+i] == 1 and matrix[row_index+i][column_index+square] == 1:
                        continue
                    else:
                        return 0
                return 1+ count(row_index, column_index, square+1)
            return 0
        count_ans = 0
        for i in range(row):
            for j in range(column):
                count_ans += count(i, j, 0)
        return count_ans
class Solution1:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #dp solution. dp[i][j] is at position row i column j, as right bottm corner, how many squares is there
        row = len(matrix)
        column = len(matrix[0])
        dp = [[matrix[j][i] for i in range(column)] for j in range(row)]
        count = 0
        for i in range(column):
            count += dp[0][i]
        for j in range(1, row):
            count += dp[j][0]
        for j in range(1, row):
            for i in range(1, column):
                
                dp[j][i] = min(dp[j-1][i], dp[j-1][i-1], dp[j][i-1])+1 if matrix[j][i] == 1 else 0
                count += dp[j][i]
        return count
        