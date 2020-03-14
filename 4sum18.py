class Solution:
    def fourSum(self, nums, target):
        lenN = len(nums)
        nums.sort()
        ans = []
        for i in range(lenN):
            if i!= 0 and nums[i] ==nums[i-1]:
                continue
            currentI = nums[i]
            for j in range(i+1, lenN):
                if j!= i+1 and nums[j] ==nums[j-1]:
                    continue
                currentJ = nums[j]
                setH = set()
                h = j
                while h< lenN-1:
                    h +=1
                    currentV = nums[h]
                    
                    if target - currentV -currentI-currentJ in setH:
                        ans.append([target - currentV -currentI-currentJ,currentJ,currentI,currentV])
                        while nums[h+1]== nums[h] and h+1< lenN:
                            h+=1
                    else:
                        setH.add(currentV)
        return ans
Solution().fourSum([0,0,0,0],0)