class Solution:
    def removeKdigits(self, num, k) :
        #return the smallest one digit from the selectable digits.
        def remove(num,k):
            lenN = len(num)
            if k >= lenN or lenN == 0:
                return ""
            if k == 0:
                return num
            digitF = 9
            itemIndex = 0
            for i in range(0, k+1):
                if int(num[i])< digitF:
                    digitF = int(num[i])
                    itemIndex = i
            return str(digitF) + remove(num[itemIndex+1:],k-itemIndex)
        resultS = remove(num,k)
        if resultS == "":
            return '0'
        resultS = str(int(resultS))
Solution().removeKdigits("112", 1)
class Solution1:
    def removeKdigits(self,num,k):
        
            