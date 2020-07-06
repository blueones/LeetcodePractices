from collections import deque
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        day_prison = {}
        cells_list = []
        counter = 0
        day_cells = 0
        for cell in cells:
            day_cells = day_cells *2 + cell
        def next_day(current_cells):
            left = current_cells << 1
            right = current_cells >> 1
            next_cells = ~(left^right) & (2**7-2)
            return next_cells
        while day_cells not in day_prison and counter < N:
            cells_list.append(day_cells)
            
            day_prison[day_cells] = counter
            day_cells = next_day(day_cells)
            counter += 1
        
        if counter == N:
            target_cells = day_cells
            ans = deque()
            for i in range(8):
                mod = target_cells % 2
                target_cells = target_cells >> 1
                ans.appendleft(mod)
            return ans
        else:
            cycle = counter - day_prison[day_cells]
            index = (N - day_prison[day_cells]) % cycle
            target_cells = cells_list[day_prison[day_cells]+index]
            ans = deque()
            for i in range(8):
                mod = target_cells % 2
                target_cells = target_cells >> 1
                ans.appendleft(mod)
            return ans
        