class Solution:
    def twoSum(self, nums, target):
        dictionaryT=dict()
        resultL=list()
        for i in range(len(nums)):
            if target-nums[i] in dictionaryT.keys() and dictionaryT[target-nums[i]]!=i:
                print(target-nums[i])
                resultL.append([i,dictionaryT[target-nums[i]]])
            else:
                dictionaryT[nums[i]]=i
            
        return resultL
print (Solution().twoSum([2, 7, 11, 15],9))


        return resultL
print (Solution().twoSum([2, 7, 11, 15],9))


        