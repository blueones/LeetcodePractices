class Solution:
    def rob(self, nums):
        lenN = len(nums)
        self.robberM = [(0,0) for i in range(lenN)]
        #self.maxR = 0 # original self.maxR. in this question could just be self.maxR = max(self.robberM[0][0],self.robberM[0][1]). to deal with test case where lenN == 1
        if lenN == 0:
            return 0
        #first item is when this item is included, the max
        #second item is when this item is not included, the max
        self.robberM[0]=(nums[0],0)
        self.maxR = max(self.robberM[0][0],self.robberM[0][1])
        for i in range(1, lenN, 1):
            includeS = self.robberM[i-1][1]+nums[i]
            notIncS = max(self.robberM[i-1][0],self.robberM[i-1][1]) # when itself is not included, the value should compare former items both include and not include and pick the larger one. easy mistake to just take the former items' includeS
            self.robberM[i]=(includeS, notIncS)
            self.maxR = max(includeS,notIncS, self.maxR)
        return self.maxR
#Solution().rob([2,1,1,2])
class Solution1:
    def rob(self,nums):
        #simpler solution from leetcode. 
        currentM = 0 #currentM is for this i, if included, the robbed number
        preM = 0 # preM is for this i, if not included, the robbed number
        self.max = 0 # this records the max for each item.
        for i in nums:
            #if not count i
            
            currentM = i+preM
            preM = self.max
            self.max = max(currentM, preM)
        return self.max
Solution1().rob([1,2,3,1])
            
