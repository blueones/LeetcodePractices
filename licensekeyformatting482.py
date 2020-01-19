class Solution1:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # first parse the content so that it's a list of split things without dashes. 
        # transform everything into uppercase
        # count all digits together and do a sum//k and sum%k. sum%k is the num of digits in the first section.
        together = S.replace("-","").upper()
        lenT = len(together)
        while lenT > K:
            lenT = lenT - K
            together = together[:lenT] + "-" + together[lenT:] # the looping idea is right, but it's not efficient
            #every time you do a split of list, a new list is created. so this time efficiency is more than O(n)
        return together
class Solution2:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # when 
        together = S.replace("-","").upper()
        lenT = len(together)
        section1 = K if lenT%K == 0 else lenT%K
        res = together[:section1]
        while section1 < lenT:
            res += "-"+ together[section1:section1+K] # this one the time efficiency is 
            #O(n) since it's calculating all content in the string once. 
            section1 += K
        return res
        
        

    
print(Solution2().licenseKeyFormatting("2-5g-3-J",2))