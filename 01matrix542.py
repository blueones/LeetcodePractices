class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix ==[]:
            return []
        self.row = len(matrix)
        self.column = len(matrix[0])
        ans = [[200 for i in range(self.column)] for j in range(self.row)]
        self.visited = [[False for i in range(self.column)] for j in range(self.row)]
        mark_total = self.row*self.column
        for i in range(self.row):
            for j in range(self.column):
                if matrix[i][j] == 0:
                    ans[i][j] = matrix[i][j]
                    self.visited[i][j] = True
                    mark_total -= 1
        distance_current = 0
        while mark_total > 0:
            distance_current += 1
            marked_current = self.neighbor_calculate(distance_current, ans)
            mark_total -= marked_current
        return ans
    def valid(self, row_index, column_index):
        return row_index >= 0 and row_index< self.row and column_index>= 0 and column_index < self.column
    def neighbor_calculate(self, distance, current_matrix):
        #return the number of cells marked. 
        marked = 0
        for i in range(self.row):
            for j in range(self.column):
                if current_matrix[i][j] == distance - 1:
                    for direction in [(1,0), (-1,0), (0, 1), (0,-1)]:
                        neighbor_row = i+direction[0]
                        neighbor_column = j+direction[1]
                        if self.valid(neighbor_row, neighbor_column) and self.visited[neighbor_row][neighbor_column] == False:
                            self.visited[neighbor_row][neighbor_column]= True
                            current_matrix[neighbor_row][neighbor_column]= distance
                            marked += 1
        return marked
                            
                            
        
        