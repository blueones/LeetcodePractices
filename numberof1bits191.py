class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        
        for i in range(32):
            if n & mask == 1:
                bits += 1
            n = n>>1
            
        return bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        #The key idea here is to realize that for any number nn, doing a bit-wise AND of nn and n - 1n−1 flips the least-significant 11-bit in nn to 00.
        count = 0
        while n != 0:
            n = n &(n-1)
            count += 1
        return count