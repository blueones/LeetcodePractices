class Solution:
    def productExceptSelf(self, nums) :
        productall=1
        zeroFlag=0
        zerolist=[]
        lenN=len(nums)
        for ind in range(0,lenN,1):
            if nums[ind]==0:
                zeroFlag+=1
                zerolist.append(ind)
                continue
            productall=productall*nums[ind]
        if zeroFlag==0:
            resultL=[productall//num for num in nums]
            return resultL
        elif zeroFlag==1:
            resultL=[0 for num in nums]
            resultL[zerolist[0]]=productall
            return resultL
        elif zeroFlag>1:
            resultL=[0 for num in nums]
            return resultL
class Solution1:
    def productExceptSelf(self,nums):
        #note:solve it without division
        lenS = len(nums)
        leftList , rightList , answerL = [1]* lenS,[1]* lenS,[1]* lenS 
        # wrong the first time. leftList = rightList = answerL = [1]* lenS, 
        # the leftList and rightList and answerL are all the same list. leads to wrong answer
        for i in range(1, lenS):
            leftList[i] = leftList[i-1]*nums[i-1]
        #print(leftList)
        for q in range(lenS-2, -1, -1):
            rightList[q] = rightList[q+1]*nums[q+1]
        #print(rightList)
        for j in range(0,lenS,1):
            answerL[j]=leftList[j]*rightList[j]
        return answerL



print(Solution1().productExceptSelf([1,2,3,4]))