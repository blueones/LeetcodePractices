class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] = (dict_nums[num][0]+1, num)
            else:
                dict_nums[num] = (1,num)
        list_frequency = [dict_nums[item] for item in dict_nums]
        sorted_frequency = sorted(list_frequency, key = lambda x:x[0],reverse = True)
        res = []
        for i in range(k):
            res.append(sorted_frequency[i][1])
        return res
class Solution1:
    def topKFrequent(self, nums, k):
        