class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        #partition each place and observe the pattern.
        largest_left = [A[0] for i in range(len(A))]
        smallest_right = [A[-1] for i in range(len(A))]
        for i in range(1, len(A), 1):
            if A[i] > largest_left[i-1]:
                largest_left[i] = A[i]
            else:
                largest_left[i] = largest_left[i-1]
        for i in range(len(A)-2, -1, -1):
            if A[i] < smallest_right[i+1]:
                    smallest_right[i] = A[i]
            else:
                smallest_right[i] = smallest_right[i+1]
        print(largest_left)
        print(smallest_right)
        
        # i is on the right side of the index i we are doing partitioning.
        for i in range(len(A)-1):
            if largest_left[i] <= smallest_right[i+1]:
                return i+1