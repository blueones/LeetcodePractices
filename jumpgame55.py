from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_n = len(nums)
        @lru_cache()
        def helper(index):
            if index == len_n-1:
                return True
            else:
                ans = []
                if nums[index] != 0:
                    for step in range(1, nums[index]+1):
                        if index+step< len_n:
                            ans.append(helper(index+step))
                return any(ans)
        return helper(0)
class Solution1:
    def canJump(self,nums):
        #also too slow
        visit = [False for i in range(len(nums))]
        visit[0] = True
        for i in range(0, len(nums)):
            if visit[i] == True:
                for j in range(nums[i]+1):
                    if i+j < len(nums):
                        visit[i+j] = True
            else:
                break
        return visit[len(nums)-1]
class Solution2:
    def canJump(self, nums):
        


            