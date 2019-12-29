class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        d=0
        r=1
        while r>=1:
            d+=1
            r=x//(10**d)
            
        highestdigit=d
        digitL=list()
        number=x
        for i in range(d-1,-1,-1):
            digitNum=number//(10**i)
            remainder=number%(10**i)
            digitL.append(digitNum)
            number=remainder
        #print (digitL)
        reverseX=0
        for i in range(d):
            reverseX=reverseX+10**(i)*digitL[i]
        if reverseX==x:
            return True
        else:
            return False



print(Solution().isPalindrome(12034))
