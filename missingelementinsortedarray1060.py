class Solution:
    def missingElement(self, nums, k):
        #add k to nums[0], see if it's smaller than nums[1] or larger than/equal to nums[-1], if so then easy.
        #if it's neither, then it's between nums[1] and nums[-1]
        # check if it's bigger or equal to nums[1], if it is, then it's nums[0]+k-1
        #check if it's bigger or equal to nums[2], if it is, then it's nums[0]+k-1-1    
        if nums[0]+k<nums[1]:
            return nums[0]+k 
        elif nums[0]+k>=nums[-1]:
            return nums[0]+k+len(nums)-1
        else:
            index=1
            k=nums[0]+k
            while k>=num[index]:
                k=k+1
                index+=1
            return k   