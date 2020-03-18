class Solution:
    def removeElement(self, nums, val) -> int:
        #border control for two pointer bumps into issues.
        lenN = len(nums)
        rightS = lenN-1
        leftS = 0
        
        while leftS<=rightS:
            
            if nums[leftS] == val:
                while rightS>leftS and nums[rightS]==val:
                    rightS-=1
                nums[leftS], nums[rightS] = nums[rightS],nums[leftS]
                if leftS == rightS:
                    return leftS
                leftS += 1 
            else:
                leftS +=1
          
        return leftS
Solution().removeElement([2],3)
class Solution1:
    def removeElement(self,nums,val):
        lenN = len(nums)
        rightS = lenN -1
        leftS = 0
        while leftS <= rightS:
            if nums[leftS]==val:
                nums[leftS],nums[rightS]= nums[rightS],nums[leftS]
                rightS-=1
            else:
                leftS+=1
        return leftS
class Solution2:
    def removeElement(self,nums,val):
        lenN =len(nums)
        marker = 0
        for walker in range(lenN):
            if nums[walker]!=val:
                nums[marker]=nums[walker]
                marker +=1
            walker +=1
        return marker