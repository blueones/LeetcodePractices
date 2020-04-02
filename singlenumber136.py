class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_num= {}
        set_num_visited = set()
        for num in nums:
            if num in dict_num:
                dict_num[num]+=1
                set_num_visited.remove(num)
            else:
                dict_num[num]=1
                set_num_visited.add(num)
        return set_num_visited.pop()
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        set_num_visited = set()
        for num in nums:
            if num in set_num_visited:
                set_num_visited.remove(num)
            else:
                set_num_visited.add(num)
        return set_num_visited.pop()
class Solution2:
    #bit manipulation
    def singleNumber(self,nums):
        a = 0
        for num in nums:
            a = a^num
        return a