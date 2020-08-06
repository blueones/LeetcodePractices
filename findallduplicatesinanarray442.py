class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        index = 0
        while index < len(nums):
            
            num = nums[index]
            if num!= 0 and num != index+1:
                if nums[num-1] != num:
                    nums[index], nums[num-1] = nums[num-1], nums[index]
                else:
                    ans.append(num)
                    nums[index] = 0
                    index += 1
            else:
                index += 1
        return ans
#solution leetcode
#negate number at index num-1 position
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for index, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            
            nums[ abs(num)-1] *= -1
        return ans