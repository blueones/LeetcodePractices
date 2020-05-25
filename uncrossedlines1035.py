class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        #get A length and B length
        lenA = len(A)
        lenB = len(B)
        def backtracking(indexA, indexB):
            #check if any of the list has been exhausted, if so, return 0
            if indexA >= lenA or indexB >= lenB:
                return 0
            else:
                max_count = 0
                for i in range(indexA, lenA):
                    for j in range(indexB, lenB):
                        if A[i] == B[j]:
                            count = 1 + backtracking(i+1, j+1)
                            max_count = max(max_count, count)
                return max_count
        return backtracking(0,0)
class Solution1:
    #DP
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for j in range(len(A)-1, -1, -1):
            for i in range(len(B)-1, -1, -1):
                if A[j] != B[i]:
                    dp[j][i] = max(dp[j+1][i+1],dp[j+1][i],dp[j][i+1])
                else:
                    
                    dp[j][i] = 1 + dp[j+1][i+1]
        return dp[0][0]    