class Solution:
    def rob(self, nums):
        lenN = len(nums)
        self.robberM = [(0,0,0,0) for i in range(lenN)]
        #self.maxR = 0 # original self.maxR. in this question could just be self.maxR = max(self.robberM[0][0],self.robberM[0][1]). to deal with test case where lenN == 1
        if lenN == 0:
            return 0
        #first item is when this item is included, the max
        #second item is when this item is not included, the max
        #third item is if includedMax used the nums[0]
        #forth item is if notIncludedMax used the nums[0]
        self.robberM[0]=(nums[0],0,True, False)
        self.maxR = max(self.robberM[0][0],self.robberM[0][1])
        if lenN == 1:
            return self.maxR
        for i in range(1, lenN, 1):
            includeS = self.robberM[i-1][1]+nums[i]
            UsedFIn = self.robberM[i-1][3]
            if self.robberM[i-1][0] > self.robberM[i-1][1]:
                notIncS = self.robberM[i-1][0]
                UsedFNot = self.robberM[i-1][2]
            elif self.robberM[i-1][0] < self.robberM[i-1][1]:
                notIncS = self.robberM[i-1][1]
                UsedFNot = self.robberM[i-1][3]
            else:
                notIncS = self.robberM[i-1][1]
                UsedFNot = self.robberM[i-1][2] and self.robberM[i-1][3]

            # when itself is not included, the value should compare former items both include and not include and pick the larger one. easy mistake to just take the former items' includeS
            self.robberM[i]=(includeS, notIncS, UsedFIn,UsedFNot)

        if self.robberM[lenN-1][0]> self.robberM[lenN-1][1]:
            if self.robberM[lenN-1][2]:
                self.maxR = max(self.maxR,self.robberM[lenN-1][1])
            else:
                self.maxR = max(self.maxR,self.robberM[lenN-1][0])
        else:
            self.maxR = max(self.maxR,self.robberM[lenN-1][1])

        return self.maxR
#Solution().rob([[2,2,4,3,2,5]])
class Solution1:
    def rob(self, nums):
        lenN = len(nums)
        self.robberM = [(0,0,0,0) for i in range(lenN)]
        #self.maxR = 0 # original self.maxR. in this question could just be self.maxR = max(self.robberM[0][0],self.robberM[0][1]). to deal with test case where lenN == 1
        if lenN == 0:
            return 0
        #first item is when this item is included, the max
        #second item is when this item is not included, the max
        #third item is if includedMax used the nums[0]
        #forth item is if notIncludedMax used the nums[0]
        self.robberM[0]=(nums[0],0,True, False)
        self.maxR = max(self.robberM[0][0],self.robberM[0][1])
        if lenN == 1:
            return self.maxR
        for i in range(1, lenN, 1):
            includeS = self.robberM[i-1][1]+nums[i]
            UsedFIn = self.robberM[i-1][3]
            if self.robberM[i-1][0] > self.robberM[i-1][1]:
                notIncS = self.robberM[i-1][0]
                UsedFNot = self.robberM[i-1][2]
            elif self.robberM[i-1][0] < self.robberM[i-1][1]:
                notIncS = self.robberM[i-1][1]
                UsedFNot = self.robberM[i-1][3]
            else:
                notIncS = self.robberM[i-1][1]
                UsedFNot = self.robberM[i-1][2] and self.robberM[i-1][3]

            # when itself is not included, the value should compare former items both include and not include and pick the larger one. easy mistake to just take the former items' includeS
            self.robberM[i]=(includeS, notIncS, UsedFIn,UsedFNot)

        if UsedFIn:
            self.maxR = max(self.robberM[lenN-1][0]- nums[0], self.robberM[lenN-1][1])
        else:
            self.maxR = max(self.robberM[lenN-1][0], self.robberM[lenN-1][1])
        return self.maxR
Solution1().rob([2,2,4,3,2,5])