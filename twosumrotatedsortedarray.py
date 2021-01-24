# Given a rotated sorted array, return number of pairs whose sum is equal to given target
# [4,5,6,7,0,1,2]
#  target = 8

# result -> <1,7>,<2,6>, 


# 1. nlogn: for each item, search for its partner with a binary search solution. (binary search)
# 2. O(n): traverse the array while storing what we have encountered, and check if coming items are partners of encountered items. (two sum hash solution. )

# solution2: space complexity is O(n). 
# traverse and check if target - current_element is in hashmap, is so add number of that to ans.
# store current_element to hashmap.
# 4-7
# 0-2

# # [6,7, 0,1,2,2]
#    ^        ^  
# #  target = 8
 

# # [2,6,7,0,1,4]
# //# [4,4,5,6,7,7,0,1,1,2,4,4]
# //           ^     ^
# //           ^

# previous pointer: if current > previous, it;s in the same increasing range.
#                 else, it's taking a turn, to be in a second increasing range. 
# first_small, first large: mark first increasing range
# second_small, second large: mark second increasing range
# class RotatedTwoSum:
#     def twosum(self, input_array, target):
#         rotated_point = self.find_rotated_point(input_array)
#         # index 2
#         first_small = float("inf") 6
#         first_large = float("-inf") 7
#         second_small= float("inf") 0
#         second_large = float("-inf") 2  
#         ans += 1
#         def in_btw(item, lower_range, higher_range):
#             return item >= lower_range and item <= higher_range
#         for index,item in enumerate(input_array):
#             if in_btw(target - item, first_small, first_large) or in_btw(target - item, second_small, second_large):
#                 ans += 1                                  
#             if index < rotated_point:
#                 if first_small== float("inf"):
#                     first_small = item
#                 first_large = item  
#             else:
#                 if second_small== float("inf"):
#                     second_small = item
#                 second_large = item  
#         return ans
    
            
                
                
        
#     def find_rotated_point(self, input_array):
#         pass