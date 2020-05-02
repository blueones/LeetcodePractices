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
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        index = len(digits) - 1
        carry = 0
        while index >= 0:
            current_digit = (digits[index] + carry) % 10
            carry = (digits[index] + carry)//10
            digits[index] = current_digit
            index -= 1
        if carry != 0:
            return [carry]+digits
        return digits
class Solution2:
    def plusOne(self, digits):
        carry = 1
        index = len(digits) - 1
        while carry > 0:
            if index == -1:
                digits.insert(0, carry)
                break
            else:
                current = digits[index] + carry
                digits[index] = current %10
                carry = current // 10
                index -= 1
        return digits