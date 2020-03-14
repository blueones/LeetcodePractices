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
# Solution().fourSum([0,0,0,0],0)
class Solution1:
    def fourSum(self,nums,target):
        lenN = len(nums)
        nums.sort()
        ans = []
        for i in range(lenN):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            currentI = nums[i]
            iTarget = target - currentI
            for j in range(i+1,lenN):
                if j != i+1 and nums[j]== nums[j-1]:
                    continue
                currentJ = nums[j]
                jTarget = iTarget - currentJ
                leftM = j+1
                rightM = lenN-1
                while leftM<rightM:
                    if nums[leftM]+nums[rightM]==jTarget:
                        ans.append([currentI,currentJ,nums[leftM],nums[rightM]])
                        leftM+=1
                        rightM-=1
                        while leftM-1>j and leftM<lenN and nums[leftM-1]==nums[leftM]: #leftM <lenN easy to forget
                            leftM+=1
                        while rightM+1<lenN and rightM>j and nums[rightM+1] == nums[rightM]:# rightM>j easy to forget
                            rightM-=1
                    elif nums[leftM]+nums[rightM] > jTarget:
                        rightM -= 1
                    elif nums[leftM]+nums[rightM] < jTarget:
                        leftM += 1
        return ans

Solution1().fourSum([0,0,0,0],0)