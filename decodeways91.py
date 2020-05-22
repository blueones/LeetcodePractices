from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        #TLE solution.
        self.ans = 0
        @lru_cache
        def backtracking(index):
            if index >= len(s):
                self.ans += 1
            else:
                if s[index] != "0":
                    for i in range(2):
                        if index+i<len(s):
                            potential = int(s[index:index+i+1])
                            if potential < 27:
                                backtracking(index+i+1)
                
        backtracking(0)
        return self.ans
class Solution1:
    def numDecodings(self, s):
        @lru_cache
        def backtracking(index):
            if index == len(s):
                return 1
            else:
                count = 0
                if s[index] != "0":
                    for i in range(2):
                        if index+i < len(s):
                            potential = int(s[index:index+i+1])
                            if potential <= 26:
                                count += backtracking(index+1+i)
                return count
        return backtracking(0)
