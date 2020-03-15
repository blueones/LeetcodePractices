class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        lenL = len(A)
        aplusb = {}
        for a in A:
            for b in B:
                if a+b not in aplusb:
                    aplusb[a+b] = 1
                else:
                    aplusb[a+b]+=1
        for c in C:
            for d in D:
                if (-c-d) in aplusb:
                    ans+=aplusb[(-c-d)]
        return ans
