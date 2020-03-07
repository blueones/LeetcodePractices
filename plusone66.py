class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        lenD = len(digits)
        i = lenD -1
        while carry >0:
            if i == -1:
                digits.insert(0,1)
                carry = 0
            else:
                digits[i]+=carry
                if digits[i]>9:
                    digits[i]-=10
                    carry = 1
                else:
                    carry = 0
                i -= 1
        return digits
            