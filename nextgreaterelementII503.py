class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double_nums = nums*2
        stack_traverse = []
        dict_next_greater = {}
        len_nums = len(nums)
        result = []
        for num in range(2*len_nums):
            while stack_traverse and nums[stack_traverse[-1]]< nums[num]:
                dict_next_greater[stack_traverse.pop(-1)]= num
            stack_traverse.append(num)
        for i in len_nums:
            if i not in dict_next_greater:
                result.append(-1)
            else:
                if dict_next_greater[i]<len_nums:
                    result.append(nums[dict_next_greater[i]])
                else:
                    index_nums = dict_next_greater[i]-len_nums
                    result.append(nums[index_nums])
        return result
class Solution1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack_traverse = []
        dict_next_greater = {}
        len_nums = len(nums)
        result = []
        for num in range(2*len_nums):
            while stack_traverse and nums[stack_traverse[-1]]< nums[num%len_nums]:
                dict_next_greater[stack_traverse.pop(-1)]= num%len_nums 
            stack_traverse.append(num%len_nums)
        for i in range(len_nums):
            if i not in dict_next_greater:
                result.append(-1)
            else:
                
                result.append(nums[dict_next_greater[i]])
                
        return result