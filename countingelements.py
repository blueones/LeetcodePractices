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
            