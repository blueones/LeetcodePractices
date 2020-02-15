class Solution:
    def maxProduct(self, nums):
        #This solution is okay but not ideal. checkout Solution1. 
        # the thinking process of this solution is that, for a item, calculate its largest product by, calculating its leftside largest product*itself*rightside largest product.
        # while in fact, when you go thru the entire list, all possibilities are exhausted when  you just do calculating its leftside largest*itself... which is solution1.
        # wow that's dumb... I mean I am dumb... why did I come up with this solution at all lol. bad design. 
        lenN = len(nums)
        self.maxP = nums[0]
        self.leftM=[(0,0) for a in range(lenN)]
        self.rightM=[(0,0) for b in range(lenN)]
        if nums[0] >= 0:
            self.leftM[0] = (nums[0],0)
        elif nums[0] < 0:   
            self.leftM[0] = (0, nums[0])
        for i in range(1,lenN):
            if nums[i] >= 0:
                PMax = max(self.leftM[i-1][0]* nums[i],nums[i])
                self.maxP = max(PMax, self.maxP)
                NMax = self.leftM[i-1][1] * nums[i]
                self.leftM[i]= (PMax,NMax)
            elif nums[i]<0:
                PMax = self.leftM[i-1][1]*nums[i]
                self.maxP = max(PMax, self.maxP)
                NMax = min(nums[i], nums[i]*self.leftM[i-1][0])
                self.leftM[i]= (PMax,NMax)
        if nums[lenN-1] >= 0:
            self.rightM[lenN-1]=(nums[lenN-1],0)
        elif nums[lenN-1] < 0:
            self.rightM[lenN -1]= (0,nums[lenN-1])
        for j in range(lenN-2, -1,-1):
            if nums[j]>= 0:
                PMax = max((self.rightM[j+1][0]*nums[j]), nums[j])
                self.maxP = max(PMax, self.maxP)
                NMax = self.rightM[j+1][1]*nums[j]
                self.rightM[j] = (PMax,NMax)
            elif nums[j]<0:
                PMax = self.rightM[j+1][1]*nums[j]
                self.maxP = max(PMax, self.maxP)
                NMax = min(self.rightM[j+1][0]*nums[j], nums[j])
                self.rightM[j] = (PMax,NMax)
        for m in range(1, lenN,1):
            if nums[m]> 0:
                product = max(self.leftM[m][0]* self.rightM[m][0], self.leftM[m][1]*self.rightM[m][1])//nums[m]
            elif nums[m]< 0:
                product = min(self.leftM[m][1]* self.rightM[m][0], self.leftM[m][0]*self.rightM[m][1])//nums[m]
            else:
                product = 0
            self.maxP = max(self.maxP, product)
        return self.maxP
Solution().maxProduct([-4,-3])
class Solution:
    def maxProduct(self, nums):
        lenN = len(nums)
        self.maxP = nums[0]
        self.leftM=[(0,0) for a in range(lenN)]
        if nums[0] >= 0:
            self.leftM[0] = (nums[0],0)
        elif nums[0] < 0:   
            self.leftM[0] = (0, nums[0])
        for i in range(1,lenN):
            if nums[i] >= 0:
                PMax = max(self.leftM[i-1][0]* nums[i],nums[i])
                self.maxP = max(PMax, self.maxP)
                NMax = self.leftM[i-1][1] * nums[i]
                self.leftM[i]= (PMax,NMax)
            elif nums[i]<0:
                PMax = self.leftM[i-1][1]*nums[i]
                self.maxP = max(PMax, self.maxP)
                NMax = min(nums[i], nums[i]*self.leftM[i-1][0])
                self.leftM[i]= (PMax,NMax)
        
        return self.maxP
Solution().maxProduct([-4,-3])