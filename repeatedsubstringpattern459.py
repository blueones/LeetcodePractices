class Solution:
    def repeatedSubstringPattern(self, s):
        #the first element of the whole string 
        # is always the beginning of the substring.
        # brute force solution. 
        begin = s[0]
        lenS = len(s)
        #find all potential substrings
        potenL = list()
        for i in range(1, len(s)//2+1, 1):
            if s[i] == begin:
                potenL.append(s[:i])
        print("potenL is ", potenL)
        for substring in potenL:
            checkL = len(substring)
            substringflag = True
            for i in range(0,lenS,checkL):
                if substring != s[i:i+checkL]:
                    print(s[i:i+checkL])
                    substringflag = False
                    break
            if substringflag == True:
                return True
        return False

print(Solution().repeatedSubstringPattern("abab"))