class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        len_s = len(s)
        max_len = 0
        for i in range(len_s):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop(-1)
                if stack:
                    max_len = max(max_len, i - stack[-1])
                    
                else:
                    stack.append(i)
        return max_len
class Solution1:
    def longestValidParentheses(self,s):
        