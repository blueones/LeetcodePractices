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


# print(Solution().threeSum([-1,0,1,2,-1,-4]))
class Solution1:
    #imprpve solution hashtable
    def threesum(self,nums):
        lenN = len(nums)
        nums.sort()
        self.resultL = []
        for i in range(lenN):
            complementI = 0 - nums[i]
            if i!= 0 and nums[i]== nums[i-1]:
                continue
            tsumL = set()
            #look for 2sum. if two items add up to complementI
            j = i 
            while j < lenN-1:
                j+=1
                if (complementI - nums[j]) in tsumL:
                    self.resultL.append([nums[i],nums[j],complementI-nums[j]])
                    while j+1< lenN and nums[j] == nums[j+1]: #check if following item is the same.  if it's the same then ignore. till it's not the same.
                        j+=1
                tsumL.add(nums[j])    
                
                
        return self.resultL
print(Solution1().threeSum([-1,0,1,2,-1,-4]))              

class Solution2:
    def threesum(self,nums):
        #two pointer
        pass

