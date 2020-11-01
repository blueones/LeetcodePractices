class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = deque()
        result = 0
        for cha in S:
            if cha == "(":
                stack.append("(")
            elif cha == ")":
                if len(stack) == 0:
                    result += 1
                else:
                    stack.pop()
        return result + len(stack)