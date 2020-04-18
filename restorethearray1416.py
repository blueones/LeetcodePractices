class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        #recursion without memoriation
        def digitsNum(num):
            return len(str(num))
        def helper(s,k):
            len_s = len(s)
            if len_s == 0:
                return 1
            ans_num = 0
            if s[0]=="0":
                return 0
            else:
                for i in range(1,digitsNum(k)+1):
                    if i<= len_s:
                        if int(s[:i])<=k:
                            ans_num += helper(s[i:],k)
                    else:
                        break
                return ans_num
        if s == "":
            return 0
        return helper(s,k)
class Solution:
    def num(self,s,k):
        def digitsNum(num):
            return len(str(num))