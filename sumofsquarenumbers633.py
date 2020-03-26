import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        right = math.floor(math.sqrt(c))
        dictOfSqure = {}
        for i in range(right+1):
            if c - i**2 in dictOfSqure or c == 2*i**2: #wrong answer if you don't add "or c == 2*i**2". because if i**2 + i**2 ==c, then it will return False. 
                return True
            else:
                dictOfSqure[i**2]=1
        return False

class Solution1:
    def judgeSquareSum(self,c):
        #binary search
        def binarySearch(left,right,square):
            mid = left+(right-left)//2
            if mid**2 == square:
                return True
            elif mid**2> square:
                binarySearch(left, mid-1, square)
            elif mid**2< square:
                binarySearch(mid+1,right,square)
        right = math.floor(math.sqrt(c))
        for i in range(right+1):
            resi = c - i**2
            if binarySearch(0,resi//2,resi):
                return True
            #check if resi is square of something
        return False
        
                