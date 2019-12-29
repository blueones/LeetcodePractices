class Solution:
    def romanToInt(self, s):
        dictionaryT1={
            "CM":900,
            "CD":400,
            "XC":90,
            "XL":40,
            "IX":9,
            "IV":4,
            }
        dictionaryT2={
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        total=0
        string=s
        for x in dictionaryT1:
            if string.find(x)!=-1:
                total=total+dictionaryT1[x]
                
                string = string.replace(x,"")
                print(total,"is total",x, "is x", string, "is the rest of the string")
        for y in string:
            if y in dictionaryT2:
                total=total+dictionaryT2[y]
                string=string.replace(y,"")
                print(total,"is total",y, "is y", string, "is the rest of the string")
        return total
print(Solution().romanToInt("MCMXCIV"))
