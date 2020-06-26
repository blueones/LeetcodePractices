class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        hash_A = {i:A[i] for i in range(len(A))}
        ordered_index = sorted(hash_A, key = lambda x: hash_A[x])
        min_a = float("inf")
        min_list = deque()
        for i in range(len(A)):
            min_a = min(min_a, ordered_index[i])
            min_list.append(min_a)
        max_a = float("-inf")
        max_list = deque()
        for i in range(len(A)-1, -1, -1):
            max_a = max(max_a, ordered_index[i])
            max_list.appendleft(max_a)
        ans = 0
        for i in range(len(A)):
            ans = max(ans, max_list[i] - min_list[i])
        return ans
class Solution1:
    def maxWidthRamp(self, A: List[int]) -> int:
        B = [i for i in range(len(A))]
        B.sort(key = lambda x:A[x])
        ans = 0
        min_small = float("inf")
        for i in B:
            min_small = min(min_small, i)
            ans = max(ans, i-min_small)
        return ans
            
            