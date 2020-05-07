class Solution:
    #hashmap
    def majorityElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                
                dict_nums[num] += 1
                if dict_nums[num] > len_nums//2:
                    return num
            else:
                dict_nums[num] = 1
                if dict_nums[num] > len_nums//2:
                    return num
class Solution1:
    def majorityElement(self, nums):
        #divide and conquer
        random.shuffle(nums)
        def helper(start, end):
            #return majority in each half
            if start + 1 == end:
                return nums[start]
            mid = (start + end)//2
            left_major = helper(start, mid)
            right_major = helper(mid, end)
            if left_major == right_major:
                return left_major
            left_count = sum(1 for i in nums if i == left_major)
            right_count = sum(1 for i in nums if i == right_major)
            return left_major if left_count > right_count else right_major
        return helper(0, len(nums))
class Solution2:
    def majorityElement(self, nums):
        #Boyer-Moore Voting algorithm
        counting = 0
        candidate = None
        for num in nums:
            if counting == 0:
                candidate = num
            counting += 1 if num == candidate else -1
        return candidate
            


