from collections import deque
class Solution:
    def minKnightMoves(self, x, y):
        #TLE. since it goes all directions. solution1 provides a way for pruning. BFS+Pruning.
        origin = [
            [0,3,2],
            [3,2,1],
            [2,1,4]
        ]
        steps = [[-2,1],[-2, -1]]
        x = abs(x)
        y = abs(y)
        if x < y:
            x, y = y, x
        if x <= 2 and y<= 2:
            return origin[x,y]
        else:
            queue = deque()
            queue.append((0,0,0))
            while queue:
                current_x, current_y, current_steps = queue.popleft()
                if current_x <=2 and current_y <=2:
                    return current_steps+steps[current_x+current_y]
from collections import deque
class Solution1:
    def minKnightMoves(self, x: int, y: int) -> int:
        #steps are {(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,-2),(-1,2)}
        if x == 0 and y == 0:
            return 0
        steps= [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,-2),(-1,2)]
        steps_advanced = [(2,1),(2,-1), (1, 2),(1,-2)]
        x= abs(x)
        y = abs(y)
        if x < y:
            x, y = y, x
        queue = deque()
        seen = set()
        queue.append((0,0,0))
        seen.add((0,0))
        while queue:
            current_x, current_y, current_steps = queue.popleft()
            if current_x <= 2 and current_y <= 2:
                for step_x, step_y in steps:
                    new_x, new_y = current_x+step_x, current_y+step_y
                    if new_x == x and new_y == y:
                        return current_steps+1
                    if new_x>= -2 and new_y >= -2 and (new_x, new_y) not in seen:
                        queue.append((new_x, new_y, current_steps+1))
                        seen.add((new_x, new_y))
            else:
                for step_x, step_y in steps_advanced:
                    new_x, new_y = current_x+step_x, current_y+step_y
                    if new_x == x and new_y == y:
                        return current_steps+1
                    if new_x>= -2 and new_y >= -2 and (new_x, new_y) not in seen:
                        queue.append((new_x, new_y, current_steps+1))
                        seen.add((new_x, new_y))
            
        
