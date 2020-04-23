class Solution:
    def deletion_distance(self,str1,str2):
        len1 = len(str1)
        len2 = len(str2)
        dp = [[0 for i in range(len2+1)] for j in range(len1+1)]
        ind1 = 0
        for ind2 in range(0, len2+1): 
            dp[ind1][ind2] = ind2
        ind2 = 0
        for ind1 in range(0,len1+1):
            dp[ind1][ind2] = ind1
        for ind1 in range(1,len1+1):
            for ind2 in range(1, len2+1):
                if str1[ind1-1] == str2[ind2-1]:
                    dp[ind1][ind2] = dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = min(dp[ind1][ind2-1]+1, dp[ind1-1][ind2]+1)
        return dp[len1][len2]
print(Solution().deletion_distance("","hit"))