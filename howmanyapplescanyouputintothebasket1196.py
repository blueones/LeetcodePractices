class Solution:
    def maxNumberOfApples(self, arr):
        arr.sort()
        appN=len(arr)
        sumA=0
        apple=0
        for apple in range(0,appN,1):
            sumA+=arr[apple]
            if sumA>5000:
                return apple
        return apple+1
print(Solution().maxNumberOfApples([900,950,800,1000,700,800]))