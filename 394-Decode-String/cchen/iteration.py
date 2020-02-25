class Solution:
    def decodeString(self, s: str) -> str:
        i, num, res = 0, '', ''
        num_stack, str_stack = [], []

        while i < len(s):
            if s[i].isnumeric():
                num = ''
                while s[i].isnumeric():
                    num += s[i]
                    i += 1
                num_stack.append(num)
                str_stack.append(res)
                res = ''
            elif s[i] == ']':
                res = str_stack.pop() + int(num_stack.pop()) * res
            else:
                res += s[i]
            i += 1

        return res