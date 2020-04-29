class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        def helper(pointer1, pointer2):
            counter = 0
            if pointer1 == len1 or pointer2 == len2:
                return 0
            else:
                if text1[pointer1] == text2[pointer2]:
                    counter = 1 + helper(pointer1+1, pointer2+1)
                else:
                    move_1_counter = helper(pointer1+1, pointer2)
                    move_2_counter = helper(pointer1, pointer2+1)
                    counter = max(move_1_counter, move_2_counter)
                return counter
        return helper(0,0)


from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        @lru_cache()
        def helper(pointer1, pointer2):
            counter = 0
            if pointer1 == len1 or pointer2 == len2:
                return 0
            else:
                if text1[pointer1] == text2[pointer2]:
                    counter = 1 + helper(pointer1+1, pointer2+1)
                else:
                    move_1_counter = helper(pointer1+1, pointer2)
                    move_2_counter = helper(pointer1, pointer2+1)
                    counter = max(move_1_counter, move_2_counter)
                return counter
        return helper(0,0)
class Solution1:
    def longestCommonSubsequence(self, text1, text2):
        # dynamic programming
        len1 = len(text1)
        len2 = len(text2)
        memo = [[0 for i in range(len2)] for j in range(len1)]
        for index1 in range(0, len1):
            if text1[index1] == text2[0]:
                memo[index1][0] = 1
            else:
                memo[index1][0] = memo[index1-1][0]
                
        for index2 in range(1, len2):
            if text2[index2] == text1[0]:
                memo[0][index2] = 1
            else:
                memo[0][index2] = memo[0][index2-1]
                
        for index1 in range(1, len1):
            for index2 in range(1, len2):
                
                if text1[index1] == text2[index2]:
                    memo[index1][index2] = 1 + memo[index1-1][index2-1]
                else:
                    memo[index1][index2] = max(memo[index1-1][index2], memo[index1][index2-1])
        print(memo)
        return memo[len1-1][len2-1]
class Solution1:
    def longestCommonSubsequence(self, text1, text2):
        # dynamic programming better memo with boundary dummies. 
        len1 = len(text1)
        len2 = len(text2)
        memo = [[0 for i in range(len2+1)] for j in range(len1+1)]
            
                
        for index1 in range(1, len1+1):
            for index2 in range(1, len2+1):
                
                if text1[index1-1] == text2[index2-1]:
                    memo[index1][index2] = 1 + memo[index1-1][index2-1]
                else:
                    memo[index1][index2] = max(memo[index1-1][index2], memo[index1][index2-1])
        print(memo)
        return memo[len1][len2]