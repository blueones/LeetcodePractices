from functools import lru_cache
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dictionary_nums = {}
        list_nums = []
        for num in nums:
            if num in dictionary_nums:
                dictionary_nums[num] += 1
            else:
                dictionary_nums[num] = 1
                list_nums.append(num)
                
        list_nums.sort()
        @lru_cache(None)
        def helper(index, include):
            
            if index >= len(list_nums):
                
                return 0
            else:
                if include:
                    num = list_nums[index]
                    
                    current_points = num*dictionary_nums[num]
                    
                    if num+1 in dictionary_nums:
                        
                        total_current = max(current_points+ helper(index+1, False),helper(index+1,True))
                    else:
                        total_current = current_points+ max(helper(index+1,True),helper(index+1, False))
                    return total_current
                        
                else:
                        
                    return max(helper(index+1, True),helper(index+1, False))
                
                
                
        return max(helper(0, True), helper(0, False))
#wrong solution
from functools import lru_cache
class WrongSolution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dictionary_nums = {}
        list_nums = []
        for num in nums:
            if num in dictionary_nums:
                dictionary_nums[num] += 1
            else:
                dictionary_nums[num] = 1
                list_nums.append(num)
                
        list_nums.sort()
        @lru_cache(None)
        def helper(index, include):
            if index == len(list_nums):
                
                return 0
            else:
                if include:
                    num = list_nums[index]
                    if dictionary_nums[num] != 0:
                        current_points = num*dictionary_nums[num]
                        if num-1 in dictionary_nums:
                            minus_num = dictionary_nums[num-1]
                            dictionary_nums[num-1] = 0
                        if num+1 in dictionary_nums:
                            plus_num = dictionary_nums[num+1]
                            dictionary_nums[num+1] = 0
                        current_num = dictionary_nums[num]
                        dictionary_nums[num] = 0
                        total_current = current_points+ max(helper(index+1,True),helper(index+1, False))
                        #backtracking. setting dictionary_num back to before current_num is counted towards winning points.
                        dictionary_nums[num] = current_num
                        if num-1 in dictionary_nums:

                            dictionary_nums[num-1] = minus_num 
                        if num+1 in dictionary_nums:

                            dictionary_nums[num+1] = plus_num
                        
                        return total_current
                    return max(helper(index+1,True),helper(index+1,False))
                return max(helper(index+1,True),helper(index+1,False))
                
                
        return max(helper(0,True), helper(0, False))