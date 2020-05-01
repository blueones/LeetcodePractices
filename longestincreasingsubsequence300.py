class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.max_length = 0
        memo = 
        def helper(index,current_string):
            if index == len(nums):
                self.max_length = max(self.max_length, len(current_string))
            else:
                for i in range(index, len(nums)):
                    current_value = nums[i]
                    if current_string == []:
                        helper(index+1, [current_value])
                    elif current_string != [] and current_value > current_string[-1]:
                        helper(index+1, current_string + [current_value])
                    else:
                        self.max_length = max(self.max_length, len(current_string))
                    
        helper(0,[])
        return self.max_length
class SolutionBottomUp:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        
        def helper(index, pre):
            #input: index is current index in nums
            #input: pre is last number
            if index == len(nums):
                return 0
            else:
                result = []
                for i in range(index, len(nums)):
                    current_value = nums[i]
                    include = 1
                    if current_value > pre:
                        include = 1 + helper(index+1, current_value)
                    not_include = helper(index+1, pre)
                    result.append(include)
                    result.append(not_include)
                dp[index]= max(result)
                return max(result)

                    
                    
        helper(0,float("-inf"))
        return dp[0]              
class Solution1:
    def lengthOfLIS(self, nums):
        # exponential time complexity
        len_nums = len(nums)
        def helper(index, pre):
            if index == len_nums:
                return 0
            else:
                include_self = 0
                if nums[index] > pre:
                    include_self = 1 + helper(index+1, nums[index])
                not_include_self = helper(index+1, pre)
                return max(include_self, not_include_self)
                
        return helper(0, float("-inf"))
                        
class Solution2:
    def lengthOfLIS(self, nums):
        