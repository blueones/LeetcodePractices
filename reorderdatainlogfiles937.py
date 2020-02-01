class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitL = []
        letterL = []
        for log in logs:
            logF = log.split(" ")[1][0]
            if logF in [str(n) for n in range(10)]:
                digitL.append(log)
            else:
                letterL.append(log)
        letterL.sort(key = lambda x:x[:len(x.split(" ")[0])+1])
        letterL.sort(key = lambda x:x[len(x.split(" ")[0])+1:])
        
        return letterL+digitL

class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #this problem is really testing the grasp you have on string split, review string split method"
        digitL = []
        letterL = []
        for log in logs:
            logF = log.split(" ",1)[1][0]
            if logF in [str(n) for n in range(10)]:
                digitL.append(log)
            else:
                letterL.append(log)
        letterL.sort(key = lambda x:x[:len(x.split(" ",1)[0])+1])
        letterL.sort(key = lambda x:x[len(x.split(" ",1)[0])+1:])
        
        return letterL+digitL
class Solution2:
    def reorderLogFiles(self,logs):
        #creating custom rules for ordering.
        
