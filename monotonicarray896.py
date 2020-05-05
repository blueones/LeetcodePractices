class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing_flag = True if (A[-1] - A[0]) >= 0 else False
        if increasing_flag:
            for i in range(1, len(A)):
                if A[i] - A[i-1] < 0:
                    return False
            return True
        else:
            for i in range(1, len(A)):
                if A[i] - A[i-1] > 0:
                    return False
            return True
class Solution:
    def isMonotonic(self, A):
        increasing = decreasing = True
        i = 1
        while i < len(A) and (decreasing or increasing):
            if A[i] > A[i-1] :
                decreasing = False
            elif A[i] < A[i-1]:
                increasing = False
            i += 1
        return increasing or decreasing