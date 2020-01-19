class goodNumber:
    #input: N.
    # output: numbers of number that are from 1 to N
    #is valid after each digit 
    #rotation.ArithmeticError
    def checkGoodNumber(self, N):
        self.validdigit = {0:0,1:1,8:8,2:5,5:2,6:9,9:6}
        def checkRotationValid(numberX):
            '''check if input is a valid number, if it is, return digitL, if it is not, return None'''
            digitL = list()
            while numberX >0:
                digitN = numberX%10
                if digitN not in self.validdigit:
                    return None
                numberX = (numberX-digitN)//10
                rotatedDigitN = self.validdigit[digitN]
                digitL.append(rotatedDigitN)
            return digitL
        flag = 0
        for numberTest in range(1, N+1, 1):
            rotated = checkRotationValid(numberTest)
            if  rotated == None:
                continue
            else:
                lenDigit = len(rotated)
                reversedN = 0
                for i in range(0,lenDigit,1):
                    reversedN += rotated[i]*10**(i)
                if reversedN == numberTest:
                    continue
                flag += 1
        return flag
    
        

class Solution2:
    def rotatedDigits(self, N: int) -> int:
        #as long as in the string it does not have 3,4,7 and has at least one of 2,5,6,9, 
        # then it is a good number.
        numberGood = 0
        for numberTest in range(1, N+1, 1):
            StringN = str(numberTest)
            good = False
            for digit in StringN:
                if digit in ("3","4","7"):
                    good = False # need this line because break only jumps out of one loop, good could be true thus leads to wrong answer. 
                    break
                if digit in ("2","5","6","9"):
                    good = True
            if good == True:
                numberGood += 1
        return numberGood
            
                    





print(Solution2().rotatedDigits(857))    