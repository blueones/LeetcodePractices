class Solution:
    def threeSum(self, nums):
        restN=list(set(nums))
        solutionL=[]
        for num in nums:
            countN=nums.count(num)
            numDic=dict()
            numDic[num]=countN
        restNL=restN.copy()
        for number,countNum in numDic.items():
            if countNum>1 and number!=0:
                restNL.remove(number)
                if -number*2 in restN:
                    solutionL.append([number,number,-number*2])
            elif countNum>=3 and number==0:
                solutionL.append([0,0,0])
        restNC=restN.copy()
        for inum in restN:
            restNC.remove(inum)
            oneR=restNC.copy()
            for a in restNC:
                oneR.remove(a)
                if -inum-a in oneR:
                    solutionL.append([inum,a,-inum-a])

        return solutionL
Solution().threeSum([1,2,-2,-2,4,0,5,5,5,-10])