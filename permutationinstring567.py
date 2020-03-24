class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        for cha in s1:
            if cha in dict1:
                dict1[cha]+=1
            else:
                dict1[cha]=1
        len1 = len(s1)
        len2 = len(s2)
        if len1>len2:
            return False
        # dict2 = {}
        for i in range(len2-len1+1):
            flag = False
            notM = False
            dict2 = {}
            for j in range(i, i+len1):
                in2 = s2[j]
                if in2 not in dict1:
                    notM = True
                    break
                else:
                    if in2 in dict2:
                        dict2[in2]+=1
                    else:
                        dict2[in2]=1
            if notM:
                continue
            for item in dict1:
                if item not in dict2:
                    notM = True
                    break
                if dict1[item]!= dict2[item]:
                    notM = True
                    break
            if notM:
                continue
            flag = True
            break
        if flag:
            return True
                    