class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2**31 and divisor ==-1:
            return 2**31-1
        negatives = 2
        if dividend> 0:
            negatives -=1
            dividend=-dividend
        if divisor>0:
            negatives -=1
            divisor= -divisor
            
        count = 0
        while dividend<= 0:
            dividend-=-divisor
            count+=1
        count -=1
        if negatives == 1:
            return -count
        else:
            return count
class Solution1:
    def divide(self,dividend,divisor):
        quotient = 0
        while dividend>=divisor:
            power_two = 1
            value = divisor
            while value+value<dividend:
                power_two+=power_two
                value += value
            dividend -= value
            quotient+=power_two
        return quotient


