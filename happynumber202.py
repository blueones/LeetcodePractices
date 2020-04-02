class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(n):
            '''calculate the sum of digit's square '''
            digitL=list()
            while n>0:
                left=n%10
                n=(n-left)//10
                digitL.append(left)
            sumS=0
            for dig in digitL:
                sumS+=dig*dig
            return sumS
        resultSet=set()
        numberT=n
        if n==1:
            return True
        while numberT!=1:
            numberT=cal(n)
            if numberT==1:
                return True
            else:
                if numberT in resultSet:
                    return False
                resultSet.add(numberT)
                n=numberT
        
class Solution2:
    def isHappy(self,n):
        '''fast runner and slow runner solution'''
        '''think of the check if a cycle exist in a linked list'''
        def nextN(n):
            # get a list of digits in n
            digitL = list()
            while n > 0:
                
                left = n%10
                n = (n-left)//10
                digitL.append(left)
            sumD = 0
            for digit in digitL:
                sumD += digit*digit
            return sumD
        # hare and tortoise
        slowR = n
        fastR = nextN(n) #make fast runner one step ahead.
        while fastR != 1:
            if fastR == slowR:
                return False
            fastR = nextN(nextN(fastR))
            slowR = nextN(slowR)    
        return True

print(Solution2().isHappy(10))
class Solution2:
    #leetcode challenge April 2nd
    def isHappy(self,n):
        visited_num = {n,}
        while n!= 1:
            digits = 0
            while n > 0:
                digits += (n%10)**2
                n = n//10
            if digits in visited_num:
                return False
            visited_num.add(digits)
            n = digits
        return True
        
        