class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
