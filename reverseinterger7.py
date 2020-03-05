class Solution:
    def reverse(self, x: int) -> int:
        #pop the last digit of x
        tempR = 0
        flag = True if x>=0 else False
        abx = x if x>0 else -x
        
        while abx>=10:
            pop = abx%10
            abx = abx//10
            tempR = tempR*10+pop
        if flag == True:
            if tempR * 10 + abx > 2**31-1:
                return 0
        elif flag == False:
            if tempR*10 + abx > 2**31:
                return 0
        tempR = tempR*10 + abx
        

        return tempR if flag == True else -tempR
Solution().reverse(-123)