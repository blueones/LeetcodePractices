
'''
Since every house is either robbed or not robbed and at least half of the houses are not robbed,
 the solution is simply the larger of two cases with consecutive houses, 
 i.e. house i not robbed, break the circle, solve it, or house i + 1 not robbed. 
 Hence, the following solution.
 I chose i = n and i + 1 = 0 for simpler coding. But, you can choose whichever two consecutive ones.

 Great solution. It took me a while to figure out why this is logically correct.
  At the first glance, I think the perfect way to split the problem is 1. not rob the 1st house; 
  2. rob 1st house, because 1 and 2 won't have any intersection (code below follows this idea and beats 100%). 
  However, the way this solution splits this problem is
   1. not rob the 1st house; 2. not rob the last house.
    As you can see, the second statement of these two split strategies are different 
    and they are not logically equal because "not rob the last house" means 
    you can choose to rob the 1st house or not. Then why it is still correct? 
    It is because the 2nd statement from the 2nd strategy contains the 2nd statement from the 1st strategy. 
    In other words, the 2nd set has some overlap with the 1st set in the 2nd strategy. 
    Since our goal is only to find the max, it is okay to include some overlap.
'''
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
class Solution2:
    def rob(self, nums):
        lenN = len(nums)
        self.robberM = [(0,0,0,0) for i in range(lenN)]
        #self.maxR = 0 # original self.maxR. in this question could just be self.maxR = max(self.robberM[0][0],self.robberM[0][1]). to deal with test case where lenN == 1
        if lenN == 0:
            return 0
        #first item is when this item is included, and include first item nums[0], the max
        #second item is when this item is not included, and include the first item nums[0], the max
        #third item is when this item is included,, and not include the first item nums[0],
        #forth item is when this item is not included,, and not include the first item nums[0],

        self.robberM[0]= (nums[0],0,0,0)
        self.maxR = max(self.robberM[0][0],self.robberM[0][1])
        if lenN == 1:
            return self.maxR
        for i in range(1, lenN, 1):
            #for house i
            includedFirst = nums[i] + self.robberM[i-1][1]
            notIncludedFirst = max(self.robberM[i-1][0],self.robberM[i-1][1])
            includedNotFirst = nums[i] + self.robberM[i-1][3]
            notIncludedNotFirst = max(self.robberM[i-1][2],self.robberM[i-1][3])
            self.robberM[i]= (includedFirst,notIncludedFirst,includedNotFirst,notIncludedNotFirst)
        self.maxR = max(self.robberM[lenN-1][1],self.robberM[lenN-1][2],self.robberM[lenN-1][3])
        return self.maxR
        

class Solution3:
    def rob(self,nums):
        #use simplified solution from 198, start with robbing nums[0], then start with robbing nums[1]
        # when you are robbing nums[1], then forsure it's not robbing nums[0].
        # so what we are really doing is covering both cases:
        #  starting with robbing nums[0] end with (maybe)robbing the second to last house, and starting without robbing nums[0] and (maybe)robbing the last house.
        
        lenN = len(nums)
        if lenN == 0:
            return 0
        if lenN == 1:
            return nums[0]
        self.nums = nums
        def robO(start, end):
        #simpler solution from leetcode. 
            
            currentM = 0 #currentM is for this i, if included, the robbed number
            preM = 0 # preM is for this i, if not included, the robbed number
            self.max = 0 # this records the max for each item.
            for i in range(start, end+1,1):
                currentM = nums[i]+preM
                preM = self.max
                self.max = max(currentM, preM)
            return self.max
        
        return max(robO(1,lenN -1),robO(0,lenN -2))
class Solution4:
    def rob(self,nums):
        #solution4 is a simplified version of solution 2. same idea but to eliminate some unnecessary space. 
        lenN = len(nums)
        #self.maxR = 0 # original self.maxR. in this question could just be self.maxR = max(self.robberM[0][0],self.robberM[0][1]). to deal with test case where lenN == 1
        if lenN == 0:
            return 0
        #first item is when this item is included, and include first item nums[0], the max
        #second item is when this item is not included, and include the first item nums[0], the max
        #third item is when this item is included,, and not include the first item nums[0],
        #forth item is when this item is not included,, and not include the first item nums[0],
        if lenN == 1:
            return nums[0]
        includedFirst = nums[0]
        notIncludedFirst = 0
        includedNotFirst = 0
        notIncludedNotFirst = 0
        for i in range(1,lenN,1):
            #for house i
            lastIncludedFirst = includedFirst
            includedFirst = nums[i] + notIncludedFirst
            notIncludedFirst = max(lastIncludedFirst, notIncludedFirst)
            lastIncludedNotFirst = includedNotFirst
            includedNotFirst = nums[i] + notIncludedNotFirst
            notIncludedNotFirst = max(lastIncludedNotFirst,notIncludedNotFirst)
            
        return max(notIncludedFirst,includedNotFirst,notIncludedNotFirst)