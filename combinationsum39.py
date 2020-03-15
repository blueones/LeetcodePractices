class Solution:
    #wrong solution. leads to permutation instead of combination.
    def combinationSum(self, candidates, target):
        resultL =[]
        lenC = len(candidates)
        def dfs(currentL, numSum,numL, resultL,target, candidates, lenC):
            if numSum == target and numL< lenC:
                resultL.append(currentL)
            elif numSum<target and numL< lenC-1:
                for candidate in candidates:
                    currentL.append(candidate)
                    dfs(currentL[:], numSum+candidate,numL+1, resultL,target, candidates, lenC)
                    currentL.pop(-1)
            
        dfs([],0, 0, resultL, target, candidates, lenC)
        return resultL

class Solution1:
    def combinationSum(self, candidates, target):
        resultL =[]
        lenC = len(candidates)
        def dfs(currentL, numSum,numL, resultL,target, candidates,candidatePoint, lenC):
            if numSum == target:
                resultL.append(currentL)
            elif numSum<target:
                for index in range(candidatePoint,lenC):
                    currentL.append(candidates[index])
                    dfs(currentL[:], numSum+candidates[index],numL+1, resultL,target, candidates,index, lenC)
                    currentL.pop(-1)
            
        dfs([],0, 0, resultL, target, candidates,0, lenC)
        return resultL
Solution1().combinationSum([2,3,5],8)
class Solution1:
    def combinationSum(self, candidates, target):
        resultL =[]
        lenC = len(candidates)
        def dfs(currentL, numSum, candidatePoint):
            if numSum == target:
                resultL.append(currentL)
            elif numSum<target:
                for index in range(candidatePoint,lenC):
                    currentL.append(candidates[index])
                    dfs(currentL[:], numSum+candidates[index],index)
                    currentL.pop(-1)
            
        dfs([],0, 0)
        return resultL