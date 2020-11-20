class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 1
        left = 0
        min_stack = deque() #store the number and then the index. #getting larger from index 0 -n
        max_stack = deque()# getting smaller from index 0 to n
        for right in range( len(nums)):
            #put current which is nums[right] in min_stack and max_stack
            
            while min_stack and min_stack[-1][0] > nums[right]:
                min_stack.pop()
            min_stack.append((nums[right], right))
            while max_stack and max_stack[-1][0] < nums[right]:
                max_stack.pop()
            max_stack.append((nums[right],right))
            
            while min_stack and max_stack and (max_stack[0][0] - min_stack[0][0]) > limit:
                if min_stack[0][1] <= max_stack[0][1]:
                    left = min_stack[0][1]+1
                    min_stack.popleft()
                
                else:
                    left = max_stack[0][1]+1
                    max_stack.popleft()
                    
                    
                    
            longest = max(longest, (right - left)+1)
        return longest