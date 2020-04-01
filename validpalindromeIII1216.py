class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.s = s
        lenS = len(s)
        left = 0
        right = lenS - 1
        return self.isValidSubPalindrome(left,right,k)

    def isValidSubPalindrome(self,left,right,kleft):
        if kleft>=0:
            if left>=right:
                return True
            while left<right:
                if self.s[left]!=self.s[right]:
                    
                    if self.isValidSubPalindrome(left+1,right,kleft-1):
                        return True
                    else:
                        return self.isValidSubPalindrome(left,right-1,kleft-1)
                    
                left+=1
                right-=1
            return True
        
        return False
class Solution2:
    def isValidPalindrome(self,s,k):
        self.s = s
        lenS = len(s)
        left = 0
        right = lenS-1
        #meaning when we are checking if substring is validsubpalindrome, we have k times deduction left
        dict_palindrome=[[0] *lenS for i in range(lenS)]
        def isValidSubPalindrome(left, right, dict_palindrome):
            if left>=right:
                return 0
            if s[left]==s[right]:
                dict_palindrome[left][right] =isValidSubPalindrome(left+1,right-1,dict_palindrome)
            else:
                dict_palindrome[left][right]=min(isValidSubPalindrome(left+1,right,dict_palindrome),isValidSubPalindrome(left,right-1,dict_palindrome))+1
            return dict_palindrome[left][right]
        return isValidSubPalindrome(left,right,dict_palindrome)<=k
        # for left in range(lenS):
        #     for right in range(lenS-1, -1,-1):
        #         if dict_palindrome[(left,right)]>=0 and left<right:
        #             if s[left]==s[right]:
        #                 dict_palindrome[(left+1,right-1)]=dict_palindrome[(left,right)]
        #             else:
        #                 dict_palindrome[(left+1,right)]=dict_palindrome[(left,right)]-1
        #                 dict_palindrome[(left,right-1)]=dict_palindrome[(left,right)]-1
        #         elif dict_palindrome[(left,right)]<0 and left<right:
        #             return False
        # return True
        # while left<right:
        #         if dict_palindrome[(left,right)]>=0 and left<right:
        #             if s[left]==s[right]:
        #                 dict_palindrome[(left+1,right-1)]=dict_palindrome[(left,right)]
        #                 left= left+1
        #                 right = right-1
        #             else:
        #                 dict_palindrome[(left+1,right)]=dict_palindrome[(left,right)]-1
        #                 dict_palindrome[(left,right-1)]=dict_palindrome[(left,right)]-1
        #         elif dict_palindrome[(left,right)]<0 and left<right:
        #             return False
        # return True
class Solution3:
    def isValidPalindrome(self,s,k):
        lenS = len(s)
        dict_palindrome = [[float('inf')]*lenS for i in range(lenS)]
        #for all self to self, it's 0
        for i in range(0,lenS):
            dict_palindrome[i][i]=0
        for m in range(1, lenS):
            for left in range(0, lenS-m):
                right = left+m
                if m == 1:
                    if s[left]==s[right]:
                        dict_palindrome[left][right]=0
                    else:
                        dict_palindrome[left][right]=1
                else:
                    if s[left]==s[right]:
                        dict_palindrome[left][right]=dict_palindrome[left+1][right-1]
                    else:
                        dict_palindrome[left][right]=min(dict_palindrome[left+1][right],dict_palindrome[left][right-1])+1
        return dict_palindrome[0][lenS-1]<=k

#extension of this question
#to return the final string.

class Solution4:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        dict_palindrome = [[[0,""]for j in range(lenS)] for i in range(lenS)]
        palindrome_length = (0,"")
        for i in range(lenS):
            length = 1
            stringC = s[i]
            dict_palindrome[i][i]=(length,stringC)
            if length>palindrome_length[0]:
                    palindrome_length=(length,stringC)
        for m in range(1,lenS):
            for left in range(lenS-m):
                right = left+m
                if m==1:
                    if s[left]==s[right]:
                        length =2
                        stringC = s[left:right+1]
                    else:
                        deduct=1
                        stringC = s[left]
                    
                if s[left]==s[right]:
                    length=dict_palindrome[left+1][right-1][0]+2
                    stringC = s[left]+dict_palindrome[left+1][right-1][1]+s[right]
                else:
                    length = dict_palindrome[left+1][right-1][0]
                    stringC = dict_palindrome[left+1][right-1][1]

                dict_palindrome[left][right]=[length,stringC]
                if length>palindrome_length[0]:
                    palindrome_length=(length,stringC)
        return palindrome_length[1]