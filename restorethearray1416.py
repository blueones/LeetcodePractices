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
class Solution1:
    def numberOfArrays(self, s, k):
        #DP
        kMod = 10**9+7 #avoid overflow. 
        dp = [-1 for i in range(len(s)+1)] # dp has len(s)+1 slots. 0~ len(s). dp[len(s)] is saying that at the right of the last digit, there is 1 "".
        dp[len(s)] = 1
        for i in range(len(s)-1,-1, -1):
            if s[i] == "0":
                continue
            dp[i] = 0
            for j in range(i+1, len(s)+1, 1): # thus we need to loop till j == len(s).
                if int(s[i:j]) <= k:
                    if dp[j]!= -1:
                        
                        dp[i] = (dp[i] + dp[j]) % kMod 
                else:
                    break
        return dp[0]
print(Solution1().numberOfArrays("600342244431311113256628376226052681059918526204",703))

