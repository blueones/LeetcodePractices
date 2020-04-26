class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals ==[]:
            return []
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        current_range = sorted_intervals[0]
        res = [current_range]
        for index in range(1, len(intervals)):
            if sorted_intervals[index][0] <= current_range[1]:
                if sorted_intervals[index][1]>= current_range[1]:
                    current_range = [current_range[0],sorted_intervals[index][1]]
                res.pop(-1)
                res.append(current_range)
            else:
                current_range = sorted_intervals[index]
                res.append(current_range)
        return res
class Solution1:
    def merge(self, intervals):
        if intervals == []:
            return []
        intervals.sort(key = lambda x: x[0])
        current_range = intervals[0]
        res = [current_range]
        
        for index in range(1, len(intervals)):
            if intervals[index][0] > current_range[1]:
                res.append(intervals[index])
            else:
                res[-1][1] = max(current_range[1], intervals[index][1])
            current_range = res[-1]
        return res
class Solution2:
    def merge(self, intervals):
        if intervals == []:
            return []
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        
        for index in range(1, len(intervals)):
            if intervals[index][0] > res[-1][1]:
                res.append(intervals[index])
            else:
                res[-1][1] = max(res[-1][1], intervals[index][1])
        return res
