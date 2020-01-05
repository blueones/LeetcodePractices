class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(n):
            digitL=list()
            digit=1
            while digit>0:
                digit=n//10
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
        

print(Solution().isHappy(19))