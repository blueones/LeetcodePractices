class Solution1:
    def subsetsWithDup(self, nums):
        self.result =[[]]
        for num in nums:
            tempList = []
            for listI in self.result:
                newList = listI.copy()
                newList.append(num)
                tempList.append(newList)
            self.result += tempList
        return self.result

