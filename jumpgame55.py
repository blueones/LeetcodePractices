#backtracking thinking
#keep going to the last one if stuck then return false
#orders are top to bottom, results bottom up. 

from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_n = len(nums)
        def helper(index):
            if index == len_n-1:
                return True
            else:
                if nums[index] != 0:
                    for step in range(1, nums[index]+1):
                        if index+step< len_n:
                            if helper(index+step):
                                return True
                return False
        return helper(0)
#speed up the backtracking process by always go to the furthest jump first. still the same O(2**n) worst case time complexity, but should be faster averagely
#plus use memoization to store results. in python you can choose to use lru_cache
class SolutionSpeedUp:
    def canJump(self, nums: List[int]) -> bool:
        len_n = len(nums)
        @lru_cache()
        def helper(index):
            if index == len_n-1:
                return True
            else:
                if nums[index] != 0:
                    for step in range( nums[index],0,-1):
                        if index+step< len_n:
                            if helper(index+step):
                                return True
                return False
        return helper(0)


#write own memoization. 
#think that we don't have to mark true for all the position repeatedly
# (which is what we were doing in the last two solution, 
# we traversed thru its reachable position at A position, 
# and we do the same for B position, and when A and B have overlapping reachable positions,
#  we will mark those positions again. Even when we have "memoization", it's not really saving time. 
#  it's a wasteful operation)


# what if we change what we are storing in memo, 
# instead of if this position is reachable, how about we save if this position is accessible to our destination.
class SolutionMemo:
    def canJump(self, nums: List[int]) -> bool:
        len_n = len(nums)
        memo = [False for i in range(len(nums))]
        memo[len_n - 1] = True
        def helper(index):
            if memo[index] == True:
                return True
            else:
                furthest_jump = min(nums[index] + index, len_n -1)
                for step in range( furthest_jump, index, -1):
                    if helper(step):
                        memo[step] = True
                        return True
                return False
        return helper(0)
class Solution1:
    def canJump(self,nums):
        #also too slow 
        visit = [False for i in range(len(nums))]
        visit[0] = True
        for i in range(0, len(nums)):
            if visit[i] == True:
                furtherest_jump = min(len(nums) - 1, nums[i]+i)
                for j in range(i+1, furtherest_jump+1):
                    visit[j] = True
            else:
                break
        return visit[len(nums)-1]
class Solution2:
    def canJump(self, nums):
        last_position = len(nums) - 1
        for i in range(last_position-1, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0
            


            