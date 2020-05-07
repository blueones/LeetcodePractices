class Solution:
    def maxSlidingWindow(self, nums, k):
        #deque in python
        #wrong. see solution1 for right solution.
        from collections import deque
        deq = deque([])
        max_list = []
        #initialize deq with first k numbers in
        for index in range(k):
            while deq and deq[-1] < nums[index]:
                deq.pop()
            deq.append(nums[index])
        max_list.append(deq[0])
        for index in range(k, len(nums)):
            # we have a problem here. We don't know when to popleft. Since deq doesn't have to be full for us to popleft. 
            #So we need to store indexes instead of nums values. 
            if len(deq) == k:
                deq.popleft()
            while deq and deq[-1] < nums[index]:
                deq.pop()
            deq.append(nums[index])
            max_list.append(deq[0])
        return max_list
class Solution1:
    def maxSlidingWindow(self, nums, k):
        #deque in python
        from collections import deque
        deq = deque([])
        max_list = []
        #initialize deq with first k numbers in
        for index in range(k):
            while deq and nums[deq[-1]] < nums[index]:
                deq.pop()
            deq.append(index)
        max_list.append(nums[deq[0]])

        #dealing with the rest of nums. 
        # always pop elements that are smaller than nums[index], then append nums[index]
        # check if deq[0] is going to be out of window, if it is, popleft. 
        for index in range(k, len(nums)):
            if deq and deq[0] == index - k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[index]:
                deq.pop()
            deq.append(index)
            max_list.append(nums[deq[0]])
        return max_list
