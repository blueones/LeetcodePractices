class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        current = m
        for i in range(m,n+1,1):
            current = current&i
        return current
            
class Solution1:
    def rangeBitwiseAnd(self,m,n):
        shift = 0
        while m<n:
            m = m >> 1
            n = n >> 1
            shift+=1
        return m << shift