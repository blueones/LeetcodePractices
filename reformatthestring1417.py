class Solution:
    def reformat(self, s: str) -> str:
        digit_string = ""
        alpha_string = ""
        for cha in s:
            if cha.isalpha():
                alpha_string+=cha
            else:
                digit_string+=cha
        def createfromtwo(start, follow):
            ans = ""
            index = 0
            while index<len(follow):
                ans+=start[index]+follow[index]
                index+=1
            if len(start) == len(follow):
                return ans
            else:
                return ans+start[-1]
                
        if abs(len(digit_string)-len(alpha_string)) >1:
            return ""
        if len(digit_string)>=len(alpha_string):
            return createfromtwo(digit_string,alpha_string)
        else:
            return createfromtwo(alpha_string,digit_string)
            