class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pointerA = 0
        pointerB = 0
        lenA = len(A)
        lenB = len(B)
        ans = []
        def intersect(range1, range2):
            return [max(range1[0], range2[0]), min(range1[1],range2[1])]
        while pointerA<lenA and pointerB<lenB:
            if A[pointerA][1] >= B[pointerB][0] and B[pointerB][1] >= A[pointerA][0]:
                ans.append(intersect(A[pointerA], B[pointerB]))
                if A[pointerA][1] <= B[pointerB][1]:
                    pointerA += 1
                else:
                    pointerB += 1
            elif A[pointerA][1] < B[pointerB][0] :
                pointerA += 1
            elif A[pointerA][0] > B[pointerB][1] :
                pointerB += 1
        return ans