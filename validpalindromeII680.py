class Solution:
    def validPalindrome(self, s: str) -> bool:
        #two pointer
        def checkP(s):
            lenS = len(s)
            left = 0
            right = lenS-1
        
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        lenS = len(s)
        left = 0
        right = lenS-1
        ticket = True
        while left<=right:
            if s[left]!=s[right]:
                return checkP(s[left:right]) or checkP(s[left+1:right+1])
            left+=1
            right-=1
        return True