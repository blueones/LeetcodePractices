class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        carryO = "0"
        strResult = ""
        while lenA>=1 or lenB>=1:
            ValueA = ValueB ="0"
            if lenA-1>=0:
                ValueA = a[lenA-1]
                lenA -=1
            if lenB-1 >= 0:
                ValueB = b[lenB-1]
                lenB -=1
            if ValueA =="0" and ValueB =="0" and carryO =="0":
                strResult ="0"+strResult
                carryO ="0"
            elif ValueA =="0" and ValueB =="0" and carryO =="1":
                strResult ="1"+strResult
                carryO ="0"
            elif (ValueA =="0" or ValueB =="0") and carryO =="0":
                strResult="1"+ strResult
                carryO ="0"
            elif (ValueA =="0" or ValueB =="0") and carryO =="1":
                strResult="0"+ strResult
                carryO ="1"
            elif ValueA == "1" and ValueB =="1" and carryO =="0":
                strResult="0"+strResult
                carryO ="1"
            elif ValueA == "1" and ValueB =="1" and carryO =="1":
                strResult="1"+strResult
                carryO ="1"
        return strResult if carryO=="0" else carryO+strResult
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        #bit manipulation
        #solution2
        x,y = int(a,2), int(b,2)
        while y:
            answer = x^y
            carry = (x&y)<<1
            x,y = answer, carry
        return bin(x)[2:]
