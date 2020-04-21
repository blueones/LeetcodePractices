class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        n = len_nums
        memory_set = set(range(n+1))
        for num in nums:
            memory_set.remove(num)
            
        return memory_set.pop()