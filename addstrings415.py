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
        pointer1 = len(num1) -1
        pointer2 = len(num2) -1
        carry = 0
        ans_list = deque()
        while pointer1 >= 0 or pointer2 >= 0:
            digit1 = digit2 = 0
            #int() could also be written ord(something) - ord("0")
            if pointer1 >= 0:
                digit1 = int(num1[pointer1])
            if pointer2 >= 0:
                digit2 = int(num2[pointer2])
            temp = digit1+ digit2 + carry
            ans_list.appendleft(str(temp%10))
            carry = temp//10
            pointer1 -= 1
            pointer2 -= 1
        if carry != 0:
            ans_list.appendleft(str(carry))
        return "".join(ans_list)
            