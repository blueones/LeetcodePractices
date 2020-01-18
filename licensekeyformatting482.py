class Solution1:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # first parse the content so that it's a list of split things without dashes. 
        # transform everything into uppercase
        # count all digits together and do a sum//k and sum%k. sum%k is the num of digits in the first section.
        together = S.replace("-","").upper()
        lenT = len(together)
        while lenT > K:
            lenT = lenT - K
            together = together[:lenT] + "-" +together[lenT:]
            
            print(lenT)
        return together
class Solution2:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        pass
print(Solution().licenseKeyFormatting("2-5g-3-J",2))