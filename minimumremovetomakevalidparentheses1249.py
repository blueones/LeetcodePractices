class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        invalid_set = set()
        ans = []
        for index, character in enumerate(s):
            if character == "(":
                stack.append(index)
            elif character == ")":
                if stack:
                    stack.pop()
                else:
                    invalid_set.add(index)
        while stack:
            invalid_set.add(stack.pop())
        for index, character in enumerate(s):
            if index not in invalid_set:
                ans.append(character)
        return "".join(ans)