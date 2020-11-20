//Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.


//input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
//output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# first intuition. sliding window with range k, find the smallest number put it at the begining(swap) and keep going.    O(nk)
# second intuition. 
# 1,1.5,5   1,1.5,5,2
#minheap to store K+1 numbers, O(log(k+1)*N)

log 2 x = 1 
x=2 
log(k+1)< 1 

class sortAlmost:
    def sorting():
        #sliding window
        minheap = []
        ans = []
        for i in range(len(arr)):
            #minheap is not full, we need to have a full minheap to pop and assign values to right index location
                
            #minheap is full, we pop the smallest to index i - (k +1)
            if len(minheap) ==k+1:
                current_smallest = heapq.pop(minheap)
                ans.append(current_smallest)
            # then push into minheap to keep going. 
            heapq.push(minheap, arr[i])
        while minheap:
            ans.append(heapq.pop(minheap))
        return ans