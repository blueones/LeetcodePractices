class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0 for i in range(num+1)]
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        if num == 2:
            return [0,1,1]
        ans[1] = 1
        ans[2] = 1
        count = 1
        for i in range(3, num+1):
            if i == 2**(count+1):
                ans[i] = ans[2**count]
                count += 1
            else:
                
                ans[i] = ans[2**count]+ ans[i-2**count]
        return ans
class Solution1:
    def countBits(self, num):
        