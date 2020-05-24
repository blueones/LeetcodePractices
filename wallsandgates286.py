class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms == []:
            return
        
        row = len(rooms)
        column = len(rooms[0])
        visited = [[False for i in range(column)] for j in range(row)]
        def valid(row_index, column_index):
            if row_index < row and row_index >= 0 and column_index< column and column_index >= 0:
                return True
            return False
        
        
        def bfs_traverse(row_index, column_index, distance):
            if valid(row_index, column_index) == False or rooms[row_index][column_index] < distance:
                return
            else:
                # if rooms[row_index] [column_index] != -1 and rooms[row_index] [column_index] != 0:
                if distance < rooms[row_index][column_index]:

                    rooms[row_index][column_index] = distance
                if rooms[row_index] [column_index] != -1:
                    if valid(row_index+1, column_index):
                        bfs_traverse(row_index+1, column_index, distance+1)
                    if valid(row_index, column_index+1):
                        bfs_traverse(row_index, column_index +1 , distance+1)
                    if valid(row_index-1, column_index):
                        bfs_traverse(row_index-1, column_index, distance+1)
                    if valid(row_index, column_index-1):
                        bfs_traverse(row_index, column_index-1, distance+1)
                    
        
        for row_index in range(row):
            for column_index in range(column):
                if rooms[row_index][column_index] == 0:
                    bfs_traverse(row_index, column_index, 0)
class Solution1:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms == []:
            return
        
        row = len(rooms)
        column = len(rooms[0])
        visited = [[False for i in range(column)] for j in range(row)]
        def valid(row_index, column_index):
            if row_index < row and row_index >= 0 and column_index< column and column_index >= 0:
                return True
            return False
        
        
        def bfs_traverse(row_index, column_index, distance):
            if valid(row_index, column_index) == False or rooms[row_index][column_index] < distance:
                return
            else:
                # if rooms[row_index] [column_index] != -1 and rooms[row_index] [column_index] != 0:

                rooms[row_index][column_index] = distance
                  
                bfs_traverse(row_index+1, column_index, distance+1)

                bfs_traverse(row_index, column_index +1 , distance+1)

                bfs_traverse(row_index-1, column_index, distance+1)

                bfs_traverse(row_index, column_index-1, distance+1)
                    
        
        for row_index in range(row):
            for column_index in range(column):
                if rooms[row_index][column_index] == 0:
                    bfs_traverse(row_index, column_index, 0)
                                 
                                 