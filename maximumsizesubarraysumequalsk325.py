class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dict_sum = {0:[-1]}
        current_sum = 0
        max_len = 0
        for index in range(len(nums)):
            current_sum += nums[index]
            if current_sum in dict_sum:
                if len(dict_sum[current_sum]) == 1:
                    dict_sum[current_sum].append(index)
                elif len(dict_sum[current_sum])==2:
                    dict_sum[current_sum][1] = index
            else:
                dict_sum[current_sum]=[index]
        for sum_in in dict_sum:
            if sum_in+k in dict_sum:
                max_len = max(max_len, dict_sum[sum_in+k][-1]-dict_sum[sum_in][0])
                
                             
        return max_len
class Solution1:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dict_sum = {0:[-1]}
        current_sum = 0
        max_len = 0
        for index in range(len(nums)):
            current_sum += nums[index]
            if current_sum not in dict_sum:
                dict_sum[current_sum]=[index]
            else:
                if len(dict_sum[current_sum])==1:
                    dict_sum[current_sum].append(index)
                else:
                    dict_sum[current_sum][1]= index
            if current_sum-k in dict_sum:
                
                max_len = max(max_len, dict_sum[current_sum][-1]-dict_sum[current_sum-k][0] )
                

                             
        return max_len
                