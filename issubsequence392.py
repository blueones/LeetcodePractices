class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        index_s = 0
        index_t = 0
        while index_s < len_s and index_t < len_t:
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                index_t += 1
        if index_s!= len_s:
            return False
        return True
from collections import defaultdict
class Solution1:
    #follow up, what if there are 1B s incoming for the same t
    #hashmap
    #reviewed how to use bisect. instead of writing binary search myself. Could do that though. 
    def isSubsequence(self, s: str, t: str) -> bool:
        def find_next(number, list_target):
            len_t = len(list_target)
            start = 0
            end = len_t
            while start < end:
                mid = (start+end)//2
                if list_target[mid] <= number:
                    start = mid+1
                else:
                    end = mid
            return start
        dict_cha = defaultdict(list)
        for i, cha in enumerate(t):
            dict_cha[cha].append(i)
       
        index_cha = -1
        for i in s:
            if i not in dict_cha:
                return False
            next_loc = find_next(index_cha, dict_cha[i])
            
            if next_loc == len(dict_cha[i]):
                return False
            index_cha = dict_cha[i][next_loc]
        return True
            
        