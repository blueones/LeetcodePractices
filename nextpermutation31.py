class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, index):
            end = len(nums)-1
            while index<end:
                nums[index],nums[end]= nums[end],nums[index]
                index += 1
                end -= 1
        lenN = len(nums)
        self.nums = nums
        i = lenN -1
        while i >0 and nums[i-1]>=nums[i]:
            i -= 1
        if i-1<0:
            reverse(nums,i)
            return nums
        swapV = nums[i-1]
        j = i
        while j<lenN and nums[j] > swapV:
            j+=1
        print(j)
        nums[i-1],nums[j-1] = nums[j-1],nums[i-1]
        # print(nums)
        reverse(nums, i)
        
        
        return nums