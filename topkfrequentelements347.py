class Solution:
    def topKFrequent(self, nums, k):
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
import collections
class Solution1:
    def topKFrequent(self, nums, k):
        dict_num = {}
        for num in nums:
            if num in dict_num:
                dict_num[num] += 1
            else:
                dict_num[num] = 1
        sorted_dict = sorted(dict_num, key = lambda x: dict_num[x], reverse = True)
        return sorted_dict[:k]
import heapq      
class Solution2:
    def topKFrequent(self, nums, k):
        #heap solution
        dict_num = {}
        for num in nums:
            if num in dict_num:
                dict_num[num] += 1
            else:
                dict_num[num] = 1
        return heapq.nlargest(k, dict_num.keys(), key = dict_num.get)
        