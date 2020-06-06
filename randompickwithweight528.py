import random
class Solution:
    #binary search
    def __init__(self, w: List[int]):
        current_w = 0
        self.list = []
        for weight in w:
            current_w += weight
            self.list.append(current_w)
        self.maximum = current_w
    def pickIndex(self) -> int:
        random_pick = random.random()*self.maximum
        
        start = 0
        end = len(self.list)
        while start < end:
            mid = (start+end)//2
            if self.list[mid]> random_pick:
                end = mid
            elif self.list[mid]< random_pick:
                start = mid+1
            
        return start
import random
class Solution1:
    #linear search
    def __init__(self, w: List[int]):
        current_w = 0
        self.list = []
        for weight in w:
            current_w += weight
            self.list.append(current_w)
        self.maximum = current_w
    def pickIndex(self) -> int:
        random_pick = random.random()*self.maximum
        for i, current_sum in enumerate(self.list):
            if current_sum > random_pick:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()