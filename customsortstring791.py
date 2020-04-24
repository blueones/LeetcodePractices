class Solution:
    def customSortString(self,S,T):
        T = sorted(T)
        resultT = ""
        counter_T = {}
        for cha in T:
            if cha in counter_T:
                counter_T[cha]+=1
            else:
                counter_T[cha] = 1
        for cha in S:
            if cha in counter_T:
                resultT += cha*counter_T[cha]
                counter_T[cha] = 0
        for item in counter_T:
            resultT+= item*counter_T[item]
        return resultT
        
