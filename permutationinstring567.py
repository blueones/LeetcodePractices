class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #same as approach #3 in LC solutions. 
        #time complexity is O(l1+(l2-l1)*l1)
        #space complexity. O(1). the dictionary at most contains 26 key-value pairs.
        len1 = len(s1)
        len2 = len(s2)
        if len1>len2:
            return False
        dict1 = {}
        for cha in s1:
            if cha in dict1:
                dict1[cha]+=1
            else:
                dict1[cha]=1
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
class Solution1:
    def checkInclusion(self,s1,s2):
        # improved from solution.
        # solution choose to do some screening when subset dictionaries are being created. which leads to error-prone logic. 
        # we prefer a widely adaptable logic than a trick logic that may save a little time 
        # but still is the same time complexity when it comes to worst case.
        len1 = len(s1)
        len2 = len(s2)
        if len1>len2:
            return False
        dict1 = {}
        def match(l1, l2):
            for item in l1:
                if item not in l2 or l1[item]!= l2[item]:
                    return False
            return True
        for cha in s1:
            if cha in dict1:
                dict1[cha]+=1
            else:
                dict1[cha]=1
        #sliding window to create dict2 in subsets of s2
        for i in range(0, len2-len1+1):
            dict2={}
            for j in range(0, len1):
                cha2=s2[i+j]
                if cha2 in dict2:
                    dict2[cha2]+=1
                else:
                    dict2[cha2]=1
            if match(dict1,dict2):
                return True
        return False
class Solution2:
    def checkInclusion(self,s1,s2):
        #using array to represent frequency since there are only 26 letters
        #same as approach 4 in LC solutions
        len1 = len(s1)
        len2 = len(s2)
        if len1>len2:
            return False
        list1 = [0]*26
        list2 = [0]*26
        for cha in s1:
            list1[ord(cha)-97]+=1
        for cha2 in s2[:len1]:
            list2[ord(cha2)-97]+=1
        def match(list1,list2):
            for i in range(26):
                if list1[i]!=list2[i]:
                    return False
            return True
        if match(list1,list2):
            return True
        for i in range(0,len2-len1):
            list2[ord(s2[len1+i])-97]+=1
            list2[ord(s2[i])-97]-=1
            if match(list1,list2):
                return True
        return False
class Solution3:
    #LC Daily Challenge. first attempt. 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        array_s1 = [0 for i in range(26)]
        array_s2 = [0 for i in range(26)]
        for cha in s1:
            array_s1[ord(cha)-ord("a")] += 1
        count = 0
        for index in range(len(s2)):
            if count == len(s1):
                array_s2[ord(s2[index-len(s1)])-ord("a")] -= 1
                count -= 1
            array_s2[ord(s2[index])- ord("a")] += 1
            count += 1
            if array_s2 == array_s1:
                return True
        return False
            

        


        