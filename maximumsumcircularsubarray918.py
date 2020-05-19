class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sum = A[0]
        #from left to right
        B = [A[0] for i in range(len(A))]
        for index in range(1, len(A)):
            B[index] = max(B[index-1]+A[index], A[index])
            max_sum = max(max_sum, B[index])
                           
        #two part. A[:i] + A[j:] j>= i
        A_left = [A[0] for i in range(len(A))]
        for i in range(1, len(A)):
            A_left[i] = A_left[i-1] + A[i]
        C = [A[-1] for i in range(len(A))]
        
        for j in range(len(A)-2, -1, -1):
            C[j] = A[j] + C[j+1]
        max_right = [C[-1] for j in range(len(A))]
        for j in range(len(A)-2, -1, -1):
            max_right[j] = max(max_right[j+1], C[j])
        for i in range(len(A)-2):
            sum_current = A_left[i] + max_right[i+2]
            max_sum = max(max_sum, sum_current)
        
        return max_sum