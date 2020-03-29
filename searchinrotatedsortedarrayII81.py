class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lenN = len(nums)
        if lenN == 0:
            return False
        left = 0
        right = lenN-1
        while left<= right:
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            
            if nums[mid]> nums[left]:
                if target> nums[mid]:
                    left = mid+1
                elif target<nums[mid] and target < nums[left]:
                    left = mid+1
                elif target<nums[mid] and target >= nums[left]:
                    right = mid-1

            elif nums[mid]<nums[left]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                elif target > nums[mid] and target > nums[right]:
                    right = mid-1
                elif target < nums[mid]:
                    right = mid-1
            else:
                left+=1

        return False

        
