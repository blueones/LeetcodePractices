class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        resultL = []
        lenN = len(nums)
        nums.sort()
        def DFS(currentL, numL, cumuNum):
            lenL = len(numL)
            if cumuNum == lenN:
                resultL.append(currentL[:])
            else:
                for i in range(lenL):
                    # print(i)
                    if i>=1 and numL[i]== numL[i-1]:
                        continue
                    currentL.append(numL[i])
                    numP = numL.copy()
                    numP.remove(numL[i])
                    DFS(currentL, numP,cumuNum+1)
                    currentL.pop(-1)
        DFS([],nums,0)
        return resultL
                    
            