class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def toInteger(input_string):
            res = 0
            for cha in input_string:
                res = res*10+int(cha)
            return res
        def toString(input_integer):
            res = ""
            while input_integer>0:
                remainder = str(input_integer%10)
                res = remainder + res
                input_integer = input_integer//10
            return res if res!="" else "0"
        
        return toString(toInteger(num1)+toInteger(num2))
class Solution1:
    def addStrings(self,num1,num2):
        