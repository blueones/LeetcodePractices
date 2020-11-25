'''
Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.
'''
input: arr = [-8,0,1,5]
output: 2 # since arr[2] == 2
#first intuition O(N)
#second intuition binary search O(logN)
#the first number where array index == array[index], to its left, all the items meet index > array[index], so we are looking for the first item where it doesn't meet index > array[index]


class Search:
    def binary_search(self, input_array):
        #start with beginning element and ending element in this array
        start = 0
        end = len(input_array)-1
        while start <= end:
            mid = start + (end-start)//2
            current_item = input_array[mid]
            if current_item >= mid:
                #look at left section of the current range
                end = mid - 1
            else:
                #look at the right section of the current range
                start = mid + 1
        # go to the far right, and didn't see a match
       
        if start == len(input_array):
            return -1
         # go to the far left, and didn't see a match. everything in this array meet index < current_item. 
        if start == 0 and input_array[start] < start:
            return -1
      
        return start