class Solution:
    def subsets(self, nums):
        self.result =[[]]
        for num in nums:
            tempList = []
            for listI in self.result:
                newList = listI.copy()
                newList.append(num)
                tempList.append(newList)
            self.result += tempList
        return self.result

Solution().subsets([1,2,3])
class Solution1:
    def subsets(self,nums):
        #same idea as solution, but slightly better time and space complexity. improved implementation
        lenN = len(nums)
        self.result = [[]]
        for num in nums:
            self.result +=[[num] + currentListItem for currentListItem in self.result] #
        return self.result
class Solution2:
    def subsets(self,nums):
        #backtracking solution
        #different from solution and solution1. those two are to traverse each item in the list, and add it onto the existing resultL's items.
        # while this solution is to iterate thru N number lists. when there is only 0 element, 1 element, 2 elements, till length elements.
        self.resultL = []
        lenN = len(nums)
        if nums == []:
            return [[]]
        def backtracking(currentL, index):
            self.resultL.append(currentL)
            for i in range(index,lenN):
                newL = currentL+ [nums[i]] #don't write the wrong variable... 5 freaking hours of debug time. learn your lesson pls...
                backtracking(newL, i+1)
        backtracking([],0)
        return self.resultL
Solution2().subsets([1,2,3])
class Solution3:
    #iterative solution
    #different from solution and solution1. those two are to traverse each item in the list, and add it onto the existing resultL's items.
    # while this solution is to iterate thru N number lists. when there is only 0 element, 1 element, 2 elements, till length elements. 
    def subsets(self,nums):
        #backtracking solution
        #different from solution and solution1. those two are to traverse each item in the list, and add it onto the existing resultL's items.
        # while this solution is to iterate thru N number lists. when there is only 0 element, 1 element, 2 elements, till length elements.
        self.resultL = []
        lenN = len(nums)
        if nums == []:
            return [[]]
        def backtracking(currentL, index):
            self.resultL.append(currentL)
            for i in range(index,lenN):
                newL = currentL+ [nums[index]]

                backtracking(newL, index+1)
        backtracking([],0)
        return self.resultL