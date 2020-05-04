class Solution:
    def largestMultipleOfThree(self, digits):
        #wrong answer. failed at input[2,2,1,1,1]
        mod1 = []
        mod2 = []
        mod0 = []
        for digit in digits:
            mod = digit%3
            if mod == 0:
                mod0.append(digit)
            elif mod == 1:
                mod1.append(digit)
            else:
                mod2.append(digit)
        len1 = len(mod1)
        len2 = len(mod2)
        len1_mod1 = len1%3
        len1_len = len1 - len1_mod1
        len2_mod2 = len2%3
        len2_len = len2 - len2_mod2
        mod1and2 = min(len1_mod1, len2_mod2)
        mod1.sort()
        mod2.sort()
        get1 = mod1[:len1_len+mod1and2]
        get2 = mod2[:len2_len+mod1and2]
        final= mod0+ get1 +get2
        final.sort(reverse = True)
        len_final = len(final)
        if len_final == 0:
            return ""
        if final[0] == 0:
            return "0"
        pointer = 0
        ans = ""
        
        while pointer < len_final:
            ans += str(final[pointer])
            pointer += 1
        return ans
        
class Solution:
    def largestMultipleOfThree(self, digits):
        #find out if sum is mod1 or mod2, then check if there are mod1 or mod2 digits to do deduction, if yes then always deduct as few digits as possible. if not then we don't have a valid answer. 
        mod1 = []
        mod2 = []
        mod0 = []
        for digit in digits:
            mod = digit%3
            if mod == 0:
                mod0.append(digit)
            elif mod == 1:
                mod1.append(digit)
            else:
                mod2.append(digit)
        len1 = len(mod1)
        len2 = len(mod2)
        mod1.sort()
        mod2.sort()
        digits_sum = sum(digits)
        if digits_sum%3 == 1:
            if len1 > 0:
                final = mod1[1:] + mod2 + mod0
            elif len2 > 1:
                final = mod1 + mod2[2:] + mod0
            else:
                return ""
        elif digits_sum%3 == 2:
            if len2 > 0:
                final = mod1 + mod2[1:] + mod0
            elif len1 > 1:
                final = mod1[2:] + mod2 + mod0
        else:
            final = mod1 + mod2 + mod0
        final.sort(reverse = True)
        if final == []:
            return ""
        if final[0] == 0:
            return "0"
        
        ans = ""
        for digit in final:
            ans += str(digit)
        return ans

class Solution2:
    def largestMultipleOfThree(self, digits):
        #DP
        digits.sort(reverse= True)
        dp = [["" for i in range(3)] for j in range(len(digits))]
        dp[0][digits[0]%3] = str(digits[0])
        for i in range(1, len(digits)):
            dp[i] = dp[i-1].copy()
            for j in range(3):
                if dp[i-1][j] != "":
                    index = (j+digits[i])%3
                    val = dp[i-1][j] +str(digits[i])
                else:
                    index = (digits[i])%3
                    val = str(digits[i])
                    #comparing with dp[i][index] instead of dp[i-1][index] 
                    # since dp[i][index] is possibly being updated in j's for loop. we want the biggest one. 
                if self.bigger(val,dp[i][index]): #comparing the number of digits. can't use val > dp[i][index] since "2" > "11"
                    dp[i][index] = val
        final = dp[len(digits)-1][0]
        ans =sorted(final, reverse = True)
        if ans == []:
            return ""
        elif ans[0] == "0":
            return "0"
        result_ans = ""
        for i in ans:
            result_ans += i
        return result_ans
    def bigger(string1, string2):
        if len(string1) > len(string2):
            return True
        else:
            return False
Solution2().largestMultipleOfThree([2,1,1,1])
        
