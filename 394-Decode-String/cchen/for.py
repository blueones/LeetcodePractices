class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        num = ''
        tmp_str = ''

        num_stack = []
        str_stack = []

        for c in s:
            if c.isnumeric():
                if num == '':
                    str_stack.append(tmp_str)
                    tmp_str = ''
                num += c
            elif c == '[':
                num_stack.append(num)
                num = ''
            elif c == ']':
                tmp_str = str_stack.pop() + int(num_stack.pop()) * tmp_str
                if len(num_stack) == 0:
                    res += tmp_str
                    tmp_str = ''
            else:
                tmp_str += c
        res += tmp_str
        return res