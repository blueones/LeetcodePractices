class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.max_length = 0
        memo = 
        def helper(index,current_string):
            if index == len(nums):
                self.max_length = max(self.max_length, len(current_string))
            else:
                for i in range(index, len(nums)):
                    current_value = nums[i]
                    if current_string == []:
                        helper(index+1, [current_value])
                    elif current_string != [] and current_value > current_string[-1]:
                        helper(index+1, current_string + [current_value])
                    else:
                        self.max_length = max(self.max_length, len(current_string))
                    
        helper(0,[])
        return self.max_length
class SolutionBottomUp:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        
        def helper(index, pre):
            #input: index is current index in nums
            #input: pre is last number
            if index == len(nums):
                return 0
            else:
                result = []
                for i in range(index, len(nums)):
                    current_value = nums[i]
                    include = 1
                    if current_value > pre:
                        include = 1 + helper(index+1, current_value)
                    not_include = helper(index+1, pre)
                    result.append(include)
                    result.append(not_include)
                dp[index]= max(result)
                return max(result)

                    
                    
        helper(0,float("-inf"))
        return dp[0]              
class Solution1:
    def lengthOfLIS(self, nums):
        # exponential time complexity
        len_nums = len(nums)
        def helper(index, pre):
            if index == len_nums:
                return 0
            else:
                include_self = 0
                if nums[index] > pre:
                    include_self = 1 + helper(index+1, nums[index])
                not_include_self = helper(index+1, pre)
                return max(include_self, not_include_self)
                
        return helper(0, float("-inf"))
                        
class Solution2:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        #dp[i] represents at index i, necessarily include index i, the longest subsequence. 
        dp = [1 for i in range(len(nums))]
        max_len = 1
        for i in range(1, len(nums)):

            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            max_len = max(max_len, dp[i])
        return max_len
class Solution:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        dp = [1 for i in range(len(nums))]
        maxresult = 1
        for i in range(1, len(nums)):
            #calculate dp[i]
            #dp[i] = max(dp[0]...dp[i-1] when nums[i] > nums[0]...nums[i-1]
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            maxresult = max(maxresult, dp[i])
        return maxresult
#segment tree solution
class SegmentTreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.val = 0
        self.left_tree = None
        self.right_tree = None
class SegmentTree:
    def __init__(self, left, right):
        def build_tree(left, right):
            if left >right:
                return None
            current = SegmentTreeNode(left, right)
            if left == right:
                return current
            else:
                mid = left+(right-left)//2
                current.left_tree = build_tree( left, mid)
                current.right_tree = build_tree(mid+1, right)
                return current
        
        self.root = build_tree(left, right)
        
    def update(self, index, value):
        def update_tree(node, index, value):
            current_left = node.left
            current_right = node.right
            if current_left == current_right and current_left == index:
                node.val = value
            else:
                mid = current_left+(current_right-current_left)//2
                if index <= mid:
                    update_tree(node.left_tree, index, value)
                else:
                    update_tree(node.right_tree, index, value)
                node.val = max(node.left_tree.val, node.right_tree.val)
        update_tree(self.root, index, value)
    def range_query(self, left, right):
        def range(node, left, right):
            if node.left >= left and node.right <= right:
                return node.val
            else:
                mid = node.left + (node.right- node.left)//2
                if left > mid:
                    return range(node.right_tree, left, right)
                elif right <= mid:
                    return range(node.left_tree, left, right)
                else:
                    return max(range(node.left_tree, left, mid), range(node.right_tree, mid+1, right))
        return range(self.root, left, right)
                    
                
        
class Solution:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        segment_tree = SegmentTree(0, len(nums)-1)
        temp_nums = sorted(nums)
        order_dict = {}
        for index, num in enumerate(temp_nums):
            if num not in order_dict:
                order_dict[num] = index
        for num in nums:
            current_index = order_dict[num]
            if current_index == 0:
                current_LIS = 1
            else:
                current_LIS = segment_tree.range_query(0, current_index-1)+1
            segment_tree.update(current_index, current_LIS)
        return segment_tree.range_query(0, len(nums)-1)