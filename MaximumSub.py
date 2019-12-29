import math

class Solution(object):
   
        
        
    def maxSub(self,nums):
        if len(nums)==0:
            return "It's an empty list"
        elif len(nums)==1:
            return nums[0],nums[0],nums[0],nums[0]
        elif len(nums)>=2:
            middle=math.ceil(len(nums)/2)
            leftList=nums[:middle]
            rightList=nums[middle:]
            sumL,leftML,rightML,totalSL=self.maxSub(leftList)
            sumR,leftMR,rightMR,totalSR=self.maxSub(rightList)
            sum2=max(sumL,sumR,rightML+leftMR)
            leftM2=max(leftML,leftMR+totalSL)
            rightM2=max(rightMR, rightML+totalSR)
            totalS2=totalSL+totalSR
            return sum2, leftM2,rightM2,totalS2
        
        
    def maxSubArray(self, nums):
        s,l,r,a=self.maxSub(nums)
        print (self.maxSub(nums))
        return s

print(Solution().maxSubArray([2,3,5,12,5,7,-2.-4]))
