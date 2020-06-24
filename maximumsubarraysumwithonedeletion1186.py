from functools import lru_cache
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        @lru_cache(maxsize = None)
        def backtracking(index, numberofdeletion):
            if index == len(arr):
                return (0, float("-inf"))
            if numberofdeletion == 1:
                current_add_max, current_max = backtracking(index+1, 1)
                return max(arr[index]+current_add_max, 0), max(current_max, arr[index]+current_add_max, arr[index])
            else:
                current_add_max, current_max = backtracking(index+1, 1)
                current_add_max0, current_max0 = backtracking(index+1, 0)
                return max(arr[index] + current_add_max0, current_add_max, 0), max(current_max, current_max0, arr[index]+current_add_max, current_add_max0+arr[index], arr[index])
        return backtracking(0, 0)[1]