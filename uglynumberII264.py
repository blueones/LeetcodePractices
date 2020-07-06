import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = []
        seen = {1,}
        heap = []
        heapq.heappush(heap, 1)
        for i in range(1690):
            current = heapq.heappop(heap)
            ugly_numbers.append(current)
            multiplier = [2,3,5]
            for multi in multiplier:
                new_ugly = current*multi
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return ugly_numbers[n-1]
            