from functools import lru_cache
class Solution:
    #recursion+memo
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def backtracking(index1, index2):
            if index1 == len(word1) and index2 == len(word2):
                return 0
            else:
                if index1< len(word1) and index2 < len(word2):
                    if word1[index1] == word2[index2]:
                        distance_current = min(backtracking(index1+1, index2+1), 1+backtracking(index1+1, index2), 1+backtracking(index1, index2+1))
                    else:
                        distance_current = min(1 + backtracking(index1+1, index2+1), 1+ backtracking(index1+1, index2), 1+ backtracking(index1, index2+1))
                    return distance_current
                else:
                    if index1 == len(word1):
                        return len(word2) - index2
                    elif index2 == len(word2):
                        return len(word1)- index1
        return backtracking(0,0)

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp solution. hahahah
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word2)+1):
            dp[len(word1)][i] = len(word2) - i
        for j in range(len(word1)+1):
            dp[j][len(word2)] = len(word1) - j
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1) -1, -1,-1):
                if word1[j] == word2[i]:
                    dp[j][i] = min(1+ dp[j+1][i], 1+ dp[j][i+1], dp[j+1][i+1])
                else:
                    dp[j][i] = min(1+ dp[j+1][i], 1+ dp[j][i+1], 1+ dp[j+1][i+1])
        return dp[0][0]
        