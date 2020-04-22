class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n) solution
        dict_sum = {0: 1}
        count = 0
        sum_current = 0
        for num in nums:
            sum_current += num
            if sum_current - k in dict_sum:
                count += dict_sum[sum_current-k]
            
            if sum_current in dict_sum:
                dict_sum[sum_current] += 1
            else:
                dict_sum[sum_current] = 1
        return count