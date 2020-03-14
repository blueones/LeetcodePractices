class Solution:
    def reverseBits(self, n: int) -> int:
        #how would you optimize it
        resultN = 0
        for i in range(32):
            n%2 = lastDigit
            n = n//2
            resultN = resultN*2+lastDigit
        return resultN
class Solution:
    def reverseBits(self,n):
        #bit manipulation
        ans = 0
        for i in range(32):
            ans = (ans<<1) + (n&1)
            n>>=1
        return ans