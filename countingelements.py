class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict_plus = {}
        count = 0
        for num in arr:
            if num+1 in dict_plus:
                dict_plus[num+1]+=1
            else:
                dict_plus[num+1] = 1
        for num in arr:
            if num in dict_plus:
                
                count +=dict_plus[num]
                dict_plus[num]=0
        return count
class Solution1:
    def countElements(self,arr):
        dict_plus = {}
        count = 0
        for num in arr:
            dict_plus[num]= 0
        for num in arr:
            if num+1 in dict_plus:
                count+=1

        return count
class Solution2:
    def countElements(self,arr):
        dict_plus = set(arr)
        count = 0
        for num in arr:
            if num+1 in dict_plus:
                count+=1
        return count