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
class Solution2:
    def productExceptSelf(self,nums):
        #note: solve it without division
        #using constant space. 
        lenS = len(nums)
        leftList , rightList = [1]* lenS,[1]* lenS
        #instead of creating rightlist. create what needs to be in rightlist on the fly. since it's related to what that value is in the last loop.
        for i in range(1, lenS):
            leftList[i] = leftList[i-1]*nums[i-1]
        #print(leftList)
        R = 1
        for q in range(lenS-2, -1, -1):
            R= R*nums[q+1]
            rightList[q] = R*leftList[q]
        #print(rightList)
        rightList[-1] = leftList[-1]
        return rightList

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #LC challenge 15 solution
        ans = [1 for num in nums]
        for index in range(1,len(nums),1):
            ans[index] = ans[index-1]*nums[index-1]
        right = 1
        for index in range(len(nums)-2, -1, -1):
            right = right*nums[index+1]
            ans[index] = ans[index]*right
        
        return ans