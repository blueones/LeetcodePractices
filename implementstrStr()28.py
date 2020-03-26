class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        lenH = len(haystack)
        lenN = len(needle)
        for i in range(lenH- lenN+1):
            marker = True
            for j in range(lenN):
                if haystack[i+j]!=needle[j]:
                    marker = False
                    break
            if marker:
                return i
        return -1