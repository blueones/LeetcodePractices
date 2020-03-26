class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer
        if s =="":
            return True
        parsedS= ""
        for cha in s:
            if cha.isalnum():
                parsedS+= cha.lower()

        lenS = len(parsedS)
        left = 0
        right = lenS-1
        while left<=right:
            if parsedS[left]!=parsedS[right]:
                return False
            left+=1
            right-=1
        return True
