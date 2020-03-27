class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search. draw on the board for the different cases. 
        lenN = len(nums)
        left = 0
        right = lenN-1
        if lenN == 0:
            return -1
        # if target< nums[0] and target> nums[-1]:
        #     return -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>= nums[left]:
                if nums[mid]>target and nums[left]>target:
                    left = mid+1
                elif nums[mid]>target and nums[left]<=target:
                    right = mid-1
                elif nums[mid]<target:
                    left = mid+1

            elif nums[mid]<nums[left]:
                if nums[mid]>target:
                    right = mid-1
                elif nums[mid]<target and nums[right]>=target:
                    left = mid + 1
                elif nums[mid]<target and nums[right]<target:
                    right = mid-1
        return -1

        
            