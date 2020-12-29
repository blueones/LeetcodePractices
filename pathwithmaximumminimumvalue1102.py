class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        row = len(A)
        column = len(A[0])
        visited = [False for i in range(row*column)]
        # visited[row_index*column + column_index]
        pq = []
        heapq.heappush(pq, (-A[0][0],(0,0)))
        def valid(x, y):
            return x >= 0 and x< row and y>= 0 and y< column   
        while pq:
            current_value, position= heapq.heappop(pq)
            x, y = position
            if x == row-1 and y == column-1:
                return -current_value
            if visited[x*column+y] == False:
                visited[x*column+y] = True
                for difference in [(-1,0),(1,0),(0,1),(0,-1)]:
                    next_x, next_y = x+difference[0], y+difference[1]
                    if valid(next_x, next_y):
                        heapq.heappush(pq, (max(current_value, -A[next_x][next_y]), (next_x, next_y)))
        