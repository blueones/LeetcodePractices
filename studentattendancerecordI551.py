class Solution:
    def checkRecord(self, s: str) -> bool:
        absentR = 0
        lateMark = 0
        i = 0
        lenS = len(s)
        while absentR <= 1 and i< lenS :
            if s[i] == 'A':
                absentR +=1
                lateMark =0
            elif s[i] == 'L':
                if lateMark == 2:
                    return False
                lateMark += 1
            else:
                lateMark = 0
            i+=1
        if i == lenS and absentR <=1:
            return True
        else:
            return False