class Solution1:
    def subsetsWithDup(self, nums):
        lenN = len(nums)
        
        if lenN == 0:
            return [[]]
        nums.sort()
        self.resultL = []
        def backtracking(first, currentL):
            self.resultL.append(currentL.copy())
            last = None
            for i in range(first, lenN):
                if nums[i] == last:
                    continue
                newL = currentL + [nums[i]]
                backtracking(i+1, newL)
                last = nums[i]
        backtracking(0,[])
        return self.resultL

