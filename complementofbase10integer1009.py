class Solution:
    def findComplement(self, num: int) -> int:
        #self
        times = 0
        begin = num
        while num != 0:
            num = num >> 1
            print(num)
            times += 1
        times = 1 if times == 0 else times
        return (1 << (times)) -1 - begin
class Solution1:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        mask = 1
        todo = N
        while todo != 0:
            N = N ^ mask
            mask = mask << 1
            todo = todo >> 1
        return N
class Solution2:
    def bitwiseComplement(self, N):
        