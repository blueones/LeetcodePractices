# // Given an array of integers. Find two disjoint subarrays such that the absolute difference between the sum of the two subarrays is maximum 

# // Example:
# // [2 -1 -2 1 -4 0 8] 
# // ans: (-1 -2 1 -4) (2 8) diff=16.
# // -6 10 16
class Solution:
    def find_difference(self, input_list):
        #left_max left_max[i] is from left till element i, what's the maximum so far 0 till len(input_list) - 2
        #left_min left_min[i] is from left till element i, what's the minimum so far 0 till len(input_list) - 2
        #right_max right_max[i] is from right till element i(not including element i), what is the maximum so far len(input_list) - 2 to 0
        #right_min right_min[i] is form right till elememt i(not including element i), what is the minimum so far len(input_list) - 2 to 0
        left_max = [[input_list[0], input_list[0]] for i in range(len(input_list)-1)]
        left_min = [[input_list[0], input_list[0]] for i in range(len(input_list)-1)]
        right_max = [[input_list[-1], input_list[-1]] for i in range(len(input_list)-1)]
        right_min = [[input_list[-1], input_list[-1]] for i in range(len(input_list)-1)]
        for i in range(1, len(input_list)-1):
            left_max[i][0] = max(left_max[i-1][0], left_max[i-1][1]+input_list[i], input_list[i])
            left_max[i][1] = max(left_max[i-1][1]+input_list[i], input_list[i])
            left_min[i][0] = min(left_min[i-1][0], left_min[i-1][1]+input_list[i], input_list[i])
            left_min[i][1] = min(left_min[i-1][1]+input_list[i], input_list[i])
        for i in range(len(input_list)-3, -1, -1):
            right_max[i][0] = max(right_max[i+1][0], right_max[i+1][1]+input_list[i+1], input_list[i+1])
            right_max[i][1] = max(right_max[i+1][1]+input_list[i+1], input_list[i+1])
            right_min[i][0] = min(right_min[i+1][0], right_min[i+1][1]+input_list[i+1], input_list[i+1])
            right_min[i][1] = min(right_min[i+1][1]+input_list[i+1], input_list[i+1])
        ans = float("-inf")
        for i in range(len(input_list)-1):
            ans = max(ans, abs(left_max[i][0]-right_min[i][0]), abs(right_max[i][0]- left_min[i][0]))
        return ans
print(Solution().find_difference([2, -1 ,-2, 1 ,-4, 2 ,8]))
