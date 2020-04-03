import math

class Solution2:
   
#Aug, 2019 divide and conquer.      
        
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
class Solution:
    #LC weekly challenge brute force
    def maxSubArray(self, nums: List[int]) -> int:
        len_num = len(nums)
        left = 0
        right = len_num-1
        max_sum = float("-inf")
        for start in range(len_num):
            for end in range(start, len_num):
                sum_current = sum(nums[start:end+1])
                max_sum = max(max_sum,sum_current)
        return max_sum
class Solution1:
    #O(N)solution, good intuitive solution
    def maxSubArray(self, nums: List[int]) -> int:
        len_num = len(nums)
        sum_max = float("-inf")
        current_sum = 0
        for i in range(len_num):
            current_sum += nums[i]
            sum_max = max(sum_max,current_sum)
            if current_sum<= 0:
                current_sum = 0
            
        return sum_max
class Solution3:
    #divide and conquer from April 2020
    def maxSubArray(self,nums):
        

        