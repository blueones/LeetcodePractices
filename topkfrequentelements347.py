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
#quickselect
from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = Counter(nums)
        max_frequency = 0
        for word in dict_num:
            frequency = dict_num[word]
            max_frequency = max(max_frequency, frequency)
        list_frequency = [(dict_num[i], i) for i in dict_num]
        #find kth high frequency element
        def findkth(start, end, k):
            
            target_index = random.randint(start, end)
            list_frequency[target_index], list_frequency[end] = list_frequency[end], list_frequency[target_index]
            target = list_frequency[end]
            pivot = start
            words = 0
            for i in range(start, end, 1):
                if list_frequency[i]>= target:
                    list_frequency[pivot], list_frequency[i] =  list_frequency[i], list_frequency[pivot]
                    # words += list_frequency[pivot][0]
                    pivot += 1
            list_frequency[pivot], list_frequency[end] = list_frequency[end], list_frequency[pivot]
            # words += list_frequency[pivot][0]
            # print(list_frequency, pivot, k)
            if pivot > k:
                return findkth(start, pivot-1, k)
            elif pivot < k:
                return findkth(pivot+1, end, k)
            else:
                return pivot
        found = findkth(0, len(list_frequency)-1, k-1)
      
        ans = [ list_frequency[i][1] for i in range(found+1)]
        return ans
#bucketsort
from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = Counter(nums)
        max_frequency = 0
        for word in dict_num:
            frequency = dict_num[word]
            max_frequency = max(max_frequency, frequency)
        bucket = defaultdict(list)
        for num in dict_num:
            bucket[dict_num[num]].append(num)
        ans = []
        count = 0
        for frequency in range(max_frequency, -1, -1):
            if frequency in bucket:
                ans.extend(bucket[frequency])
                count += len(bucket[frequency])
            if count == k:
                return ans
        return ans