class Solution1:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = K
        lenA = len(A)
        i = lenA -1
        while carry >0:
            if i== -1:
                A.insert(0,carry%10)
                carry = carry//10
            else:
                sumN = A[i]+ carry
                A[i]= sumN if sumN<10 else sumN%10
                carry = sumN //10
                i-=1
        return A