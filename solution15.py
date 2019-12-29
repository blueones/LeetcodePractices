class Solution:
    def threeSum(self, nums):
        restN=list(set(nums))
        solutionL=[]
        for num in nums:
            countN=nums.count(num)
            numDic=dict()
            numDic[num]=countN
            
        for number,countNum in numDic:
            if countNum>1 and number!=0:
                restN.remove(number)
                if -number*2 in restN:
                    solutionL.append([number,number,-number*2])
            elif countNum>=3 and number==0:
                solutionL.append([0,0,0])
        for inum in restN:
            restNC=restN.copy()
            twoRest=restNC.remove(inum)
            for a in twoRest:
                oneR=twoRest.copy()
                if -inum-a in oneR.remove(a):
                    solutionL.append([inum,a,-inum-a])
        return solutionL

Solution().threeSum([1,2,3,4,4,4,6,6,-2,-4,0,2])