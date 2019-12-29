class Solution:
    def threeSum(self, nums):
        uniqueL=list()
        resultL=list()
        for i in nums:
            if i not in uniqueL:
                uniqueL.append(i)
        #print(uniqueL)
        for a in uniqueL:
            numsL=nums.copy()
            numsL.remove(a)
            for x in numsL:
                numsL1=numsL.copy()
                #print("numsL is",numsL)
                #print("x is",x,"a is",a)
                numsL1.remove(x)
                b=(0-a)-x
                if b in numsL1: 
                    if ([a,x,b] in resultL) or([b,a,x] in resultL )or ([x,b,a] in resultL) or ([b,x,a] in resultL) or ([x,a,b]in resultL) or ([a,b,x] in resultL):  
                        continue
                    resultL.append([a,b,x])
        return resultL


print(Solution().threeSum([-1,0,1,2,-1,-4]))
                
        
