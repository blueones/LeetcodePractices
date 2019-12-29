class Solution:
    def searchInsert(self, nums, target):
        self.list=nums
        self.len=len(nums)
        self.target=target
        middle=self.len//2
        return self.findplace(0,self.len-1)
        # find middle of array,
        # compare middle of array with target middle=(beginIndex+endIndex+1)//2
        # if bigger then go to the left of the list to keep on search
        # if smaller than go to the right of the list to keep on search
        # so there are beginIndex, endIndex and middle 
        # when beginIndex == endIndex, compare and see if target ==list[beginIndex], if not see if target large or small, then put it in front of or behind middle. 
        # when middle ==endIndex, compare
        # compare should have a couple scenarios.
        # 1. target==middle 2. target < middle, 3. target >middle 
    def findplace(self,beginIndex, endIndex):
        if beginIndex==endIndex:
            if self.list[beginIndex]>=self.target:
                return beginIndex
            elif self.list[beginIndex]<self.target:
                return beginIndex+1
        else:
            middleIndex=(beginIndex+endIndex)//2
            print("middle is", middleIndex,"begin is ", beginIndex, "end is ", endIndex)
            if self.list[middleIndex]==self.target:
                return middleIndex
            elif self.list[middleIndex]>self.target:
                return self.findplace(beginIndex,middleIndex)
            elif self.list[middleIndex]<self.target:
                return self.findplace(middleIndex+1,endIndex)

print(Solution().searchInsert([1,3],4))