class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.good_oranges = 0
        row = len(grid)
        column = len(grid[0])
        for row_index in range(row):
            for column_index in range(column):
                if grid[row_index][column_index] == 1:
                    self.good_oranges += 1
        self.impossible = True
        if self.good_oranges == 0:
            return 0
        def to_rotten():
            self.impossible = True
            for row_index in range(row):
                for column_index in range(column):
                    if grid[row_index][column_index] == 3:
                        grid[row_index][column_index] = 2
            for row_index in range(row):
                for column_index in range(column):
                    
                    if grid[row_index][column_index] == 2:
                        
                        if row_index+1 >= 0 and row_index+1<row and grid[row_index+1][column_index] == 1:
                            self.good_oranges -= 1
                            grid[row_index+1][column_index] = 3
                            self.impossible = False
                        if row_index-1 >= 0 and row_index-1 < row and grid[row_index-1][column_index] == 1:
                            
                            self.good_oranges -= 1
                            grid[row_index-1][column_index] = 3
                            self.impossible = False
                        if column_index+1 >= 0 and column_index+1 < column and grid[row_index][column_index+1] == 1:
                            
                            self.good_oranges -= 1
                            grid[row_index][column_index+1] = 3
                            self.impossible = False
                        if column_index-1 >= 0 and column_index-1< column and grid[row_index][column_index-1] == 1:
                            self.good_oranges -= 1
                            grid[row_index][column_index-1] = 3
                            self.impossible = False
            if self.good_oranges == 0:
                return False
            return True
        time = 0
        rotten = to_rotten()
        while rotten:
            
            time += 1
            rotten = to_rotten()
            if self.impossible:
                return -1
        return time+1
class Solution:
    #多源BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == []:
            return -1
        row = len(grid)
        column = len(grid[0])
        queue = deque()
        oranges = 0
        good_oranges =0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for row_index in range(row):
            for column_index in range(column):
                orange = grid[row_index][column_index] 
                if orange == 2:
                    queue.append((row_index, column_index))
                    grid[row_index][column_index] = 3
                elif orange == 1:
                    good_oranges += 1
        times = 0
        if good_oranges == 0:
            return 0
    
        def check_valid(row_index, column_index):
            if row_index >= 0 and row_index < row and column_index >= 0 and column_index < column:
                return True
            return False
        while queue:
            current_rotten = len(queue)
            times += 1
            for i in range(current_rotten):
                current_row, current_column = queue.popleft()
                for row_direction, column_direction in directions:
                    neighbor_row, neighbor_column = current_row+row_direction,current_column+column_direction
                    if check_valid(neighbor_row, neighbor_column) and grid[neighbor_row][neighbor_column] == 1:
                        queue.append((neighbor_row, neighbor_column))
                        grid[neighbor_row][neighbor_column] = 3
                        good_oranges -= 1
        return times-1 if good_oranges == 0 else -1