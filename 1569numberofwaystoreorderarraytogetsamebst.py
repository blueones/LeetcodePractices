import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        #build the tree
        # while building the tree, calculate possibilities
        
        def helper(indexlist):
            #return possibility after this. 
            if len(indexlist) == 1 or indexlist == []:
                return 1
            top = nums[indexlist[0]]
            left = right = 0
            
            
            left_list = []
            right_list = []
            for i in range(1, len(indexlist)):
                index_num = indexlist[i]
                if nums[index_num] > top:
                    right += 1
                    right_list.append(index_num)
                else:
                    
                    left += 1
                    left_list.append(index_num)
            #C(len(nums)-1 - index) left
            
            left_side = helper(left_list) 
            right_side = helper(right_list)
            return (math.factorial(len(indexlist)-1)//(math.factorial(left)*math.factorial(len(indexlist)-1-left))*left_side*right_side)%(10**9+7)
        
        input_index = [i for i in range(len(nums))]
        return helper(input_index)-1
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        #build the tree
        # while building the tree, calculate possibilities
        
        def helper(indexlist):
            #return possibility after this. 
            if len(indexlist) == 1 or indexlist == []:
                return 1
            top = nums[indexlist[0]]
            left = right = 0
            left_list = []
            right_list = []
            for i in range(1, len(indexlist)):
                index_num = indexlist[i]
                if nums[index_num] > top:
                    right += 1
                    right_list.append(index_num)
                else:
                    left += 1
                    left_list.append(index_num)
            left_side = helper(left_list) 
            right_side = helper(right_list)
            return (comb((len(indexlist)-1),left)*left_side*right_side)%(10**9+7)
        
        input_index = [i for i in range(len(nums))]
        return helper(input_index)-1
       