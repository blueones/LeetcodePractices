class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        parts = [i for i in range(4*N**2)]
        count = 4*N**2
        def find(x):
            if x != parts[x]:
                ancestor = find(parts[x])
                parts[x] = ancestor
                return ancestor
            else:
                return x
                
        def union(x,y, count):
            ancestor_x = find(x)
            ancestor_y = find(y)
            if ancestor_x != ancestor_y:
                parts[ancestor_x] = ancestor_y
                count -= 1
                
                return count
            else:
                return count
                
                
        for i in range(N**2):
            row_index = i//N
            column_index = i%N
            if grid[row_index][column_index] == " ":
                count = union(i*4, i*4+1, count)
                count = union(i*4+1, i*4+2, count)
                count = union(i*4+2, i*4+3, count)
            elif grid[row_index][column_index] == "/":
                count = union(i*4+1, i*4+2, count)
                count = union(i*4, i*4+3, count)
                
            elif grid[row_index][column_index] == "\\":
                count = union(i*4, i*4+1, count)
                count = union(i*4+2, i*4+3, count)
            if row_index < N-1:
                
                count = union(i*4+2, (i+N)*4, count)
                
            if column_index < N-1:
                
                count = union(i*4+1, (i+1)*4+3, count)
                
               

        return count