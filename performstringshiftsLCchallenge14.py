class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = 0
        for direction in shift:
            if direction[0]==0: #shift left
                count += direction[1]
            else:
                count -= direction[1]
            
        count= count%len(s)
        return s[count:]+s[:count]
        