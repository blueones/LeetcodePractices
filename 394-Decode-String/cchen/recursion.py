class Solution:
    def decode(self, s, i, j, brk_dict):
        if i > j:
            return ''

        k = i
        while k <= j and not s[k].isnumeric():
            k += 1

        if i < k:
            return s[i:k] + self.decode(s, k, j, brk_dict)
        else:
            k = i + 1
            while k <= j and s[k].isnumeric():
                k += 1
            return int(s[i:k]) * self.decode(s, k + 1, brk_dict[k] - 1, brk_dict) + self.decode(s, brk_dict[k] + 1, j, brk_dict)

    def decodeString(self, s: str) -> str:
        stack = []
        brk_dict = {}
        for i, c in enumerate(s):
            if c == '[':
                stack.append(i)
            elif c == ']':
                brk_dict[stack.pop()] = i

        return self.decode(s, 0, len(s) - 1, brk_dict)