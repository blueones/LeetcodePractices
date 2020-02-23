class Solution:
    def decodeString(self, s):
        stackListNum = []
        stackListStr = []
        stringC = ""
        temp = ""
        lenS = len(s)
        i = 0
        while i < lenS:
            if s[i].isdecimal():
                numb = 0
                stackListStr.append(temp)
                temp = ""
                while s[i].isdecimal():
                    numb = numb*10+int(s[i])
                    i += 1
            elif s[i] == "[":
                stackListNum.append(numb)
                i+=1

            elif s[i] =="]":
                temp = stackListStr.pop(-1) + temp*stackListNum.pop(-1)
                i+=1
                
            else:
                temp += s[i]
                i+=1
        return temp
Solution().decodeString("100[leetcode]")