class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lenN = len(nums)
        start = 0
        end =k-1
        presum = 0
        for i in range(k):
            presum+= nums[i]
        maxS = presum
        while end+1 < lenN:
            presum+= nums[end+1]-nums[start]
            maxS = max(maxS,presum)
            end +=1
            start+=1
        
        return maxS/k
