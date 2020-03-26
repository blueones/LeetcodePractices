class Solution:
    def mySqrt(self, x: int) -> int:
        #first intuition
        square = 1
        guess = 1
        while square <= x:
            guess +=1
            square = guess **2
        return guess-1
class Solution1:
    # binary search
    def mySqrt(x):
        def binarySearch(left,right, target):
            mid = left+(right-left)//2
            if mid**2 == target:
                return mid
            elif mid**2>target:
                return binarySearch(left,mid-1,target)
            elif mid**2<target:
                if (mid+1)**2>target:
                    return mid
                return binarySearch(mid+1,right, target)
        return binarySearch(0,x,x)
class Solution1:
    def mySqrt(x):
        left, right = 1, x
        while left<= right:
            mid = (left+right)//2
            if mid**2 == x:
                return mid
            if mid**2 >x:
                right = mid-1
            if mid**2 < x:
                left = mid+1
        return right
