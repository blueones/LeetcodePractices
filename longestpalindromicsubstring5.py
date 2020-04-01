class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        dict_palindrome = [[False for j in range(lenS)] for i in range(lenS)]
        palindrome_length = (0,"")
        for i in range(lenS):
            length = 1
            stringC = s[i]
            dict_palindrome[i][i]=True
            if length>palindrome_length[0]:
                    palindrome_length=(length,stringC)
        for m in range(1,lenS):
            for left in range(lenS-m):
                right = left+m
                if m==1:
                    if s[left]==s[right]:
                        length =2
                        dict_palindrome[left][right] = True
                        if length>palindrome_length[0]:
                            palindrome_length=(length,s[left:right+1])
                    else:
                        dict_palindrome[left][right] = False
                else:
                    if s[left]==s[right] and dict_palindrome[left+1][right-1]:
                        length = right - left+1
                        dict_palindrome[left][right] = True
                        if length>palindrome_length[0]:
                            palindrome_length=(length,s[left:right+1])
                    else:
                        dict_palindrome[left][right] = False      
        return palindrome_length[1]
Solution().longestPalindrome("cbbd")
        
