class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        pivot = 0
        exchange = 0
        while exchange < len_nums and pivot <len_nums:
            
            if nums[pivot] == 0:
                while exchange < len_nums and nums[exchange]== 0:
                    exchange += 1
                if exchange <len_nums:
                    nums[pivot],nums[exchange]= nums[exchange],nums[pivot]
                    pivot += 1
                    exchange += 1
            else:
                pivot += 1
                exchange +=1
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        last_nonzero_index = 0
        for index in range(len_nums):
            if nums[index]!= 0:
                nums[last_nonzero_index]= nums[index]
                last_nonzero_index+=1
        for index in range(last_nonzero_index,len_nums):
            nums[index]= 0
class Solution2:
    def moveZeroes(self,nums):
        len_nums = len(nums)
        last_zero_index = 0
        for index in range(len_nums):
            if nums[index]!= 0:
                nums[index],nums[last_zero_index] = nums[last_zero_index],nums[index]
                last_zero_index += 1
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        while zero < len(nums) and nums[zero]!= 0:
            zero += 1
        pivot = zero
        while pivot < len(nums) and pivot == 0:
            pivot += 1
        
        while pivot < len(nums):
            if nums[pivot]!= 0:
                nums[pivot], nums[zero] = nums[zero], nums[pivot]
                zero += 1
                pivot += 1
            else:
                pivot += 1
                

            
            