class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
        max_substring = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_substring = max(max_substring, dp[i][j])
        return max_substring
              