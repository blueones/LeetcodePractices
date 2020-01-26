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


class Solution1:
    def twoSum(self,nums,target):
        # binary search method
        lenS = len(nums)
        if lenS <= 1:
            return []
        dictofvisited = {}
        for i in range(0, lenS, 1):
            if target-nums[i] in dictofvisited and dictofvisited[target-nums[i]]!=i:
                return [i, dictofvisited[target-nums[i]]]
            else:
                dictofvisited[nums[i]]= i
                
        return []
              


        