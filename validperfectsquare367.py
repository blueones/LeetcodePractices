class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #binary search, much faster than solution1
        if num<2:
            return True
        left = 2
        right = num/2
        while left<=right:
            x = (left+right)//2
            guess = x*x
            if guess == num:
                return True
            if guess >num:
                right =x-1
            elif guess < num:
                left =x+1
        return False
class Solution1:
    def isPerfectSquare(self,num):
        tryN = 1
        while tryN*tryN<= num:
            if tryN*tryN == num:
                return True
            tryN += 1
        return False