class Solution:
    def decodeString(self, s):
        #use stack please review excel sheet to find good explanation in youtube video for this solution.
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
class Solution:
    def decodeString(self,s):
        #recursion
        #same idea as solution but using recursion.
        lenS = len(s)
        i = 0
        temp = ""
        while i < lenS:
            if s[i] =="]":
                temp = temp + numb*stringI
                return temp
                i+=1
            if s[i].isdecimal():
                numb = 0
                stackListStr.append(temp)
                while s[i].isdecimal():
                    numb = numb*10+int(s[i])
                    i += 1
            elif s[i] == "[":
                newS = s[i+1:]
                closeNewS = newS.find("]")
                newSS = newS[:closeNewS+1]
                stringI = self.decodeString(newSS)
                i += closeNewS

            elif s[i] =="]":
                temp = temp + numb*stringI
                return temp
                i+=1
                
            else:
                temp += s[i]
                i+=1
        return temp

