class Solution:
    def combinationSum2(self, candidates, target):
        lenC = len(candidates)
        ans = []
        candidates.sort()
        def backtracking(currentL, numSum, start):
            if numSum == target:
                ans.append(currentL)
            elif numSum < target:
                for index in range(start, lenC):
                    if index != start and candidates[index]==candidates[index-1]: #pay attention here should be index != start instead of index != 0
                        continue
                    currentL.append(candidates[index])
                    backtracking(currentL[:],numSum+candidates[index],index+1)
                    currentL.pop(-1)
        backtracking([],0,0)
        return ans
Solution().combinationSum2([10,1,2,7,6,1,5],8)