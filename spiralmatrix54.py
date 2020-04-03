class Solution:
    def spiralOrder(self, matrix):
        if matrix== []:
            return []
        row = len(matrix)
        column = len(matrix[0])
        low_row = 0
        high_row = row - 1
        low_column = 0
        high_column = column - 1
        resultL = []
        while low_row <= high_row and low_column <= high_column:
            for column in range(low_column,high_column+1,1):
                resultL.append(matrix[low_row][column])
            for row in range(low_row+1,high_row+1,1):
                resultL.append(matrix[row][high_column])
            if high_row!=low_row:
                for column in range(high_column-1,low_column-1,-1):
                    resultL.append(matrix[high_row][column])
            if high_column != low_column:
                for row in range(high_row-1,low_row,-1):
                    resultL.append(matrix[row][low_column])
            low_row+=1   
            high_row-=1  
            low_column+=1  
            high_column-=1 
        return resultL 
Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
class Solution1:
    def spiralOrder(self,matrix):
        

