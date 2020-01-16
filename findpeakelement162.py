class Solution:
    def findPeakElement(self, nums):
        if nums == []:
            return -1
        leftF = 0
        rightF = len(nums)-1
        while leftF <= rightF:
            if leftF == rightF:
                return leftF
            middleIndex = (leftF+rightF)//2
            print("middleIndex is ", middleIndex,"leftF is ", leftF, "rightF is  ", rightF)
            if middleIndex == leftF:
                if nums[leftF] > nums[rightF]:
                    return leftF
                return rightF
            middleN = nums[middleIndex]
            leftN = nums[middleIndex-1]
            rightN = nums[middleIndex+1]
            if middleN > leftN and middleN > rightN:
                return middleIndex
            elif middleN > leftN and middleN < rightN:
                leftF = middleIndex + 1
            else:
                rightF = middleIndex - 1

print(Solution().findPeakElement([2,1,2]))