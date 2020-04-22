class Solution:
    def confusingNumber(self, N: int) -> bool:
        if N == 0:
            return False
        bad_digits = {2,3,4,5,7}
        flip_dict = {0:0, 1:1, 6:9, 8:8, 9:6}
        def helper(number):
            #return a list of digits
            result = []
            while number > 0:
                remainder = number%10
                number = number//10
                if remainder in bad_digits:
                    return False
                result.append(remainder)
            return result
        
        def flip(list_digits):
            result = 0
            for i in range(len(list_digits)):
                result = result*10 + flip_dict[list_digits[i]] 
            return result
        
        digit_list = helper(N)
        if digit_list == False:
            return False
        else:
            flipped = flip(digit_list)
            if flipped == N:
                return False
            else:
                return True
class Solution1:
    def confusingNumber(self, N):
        digits_dict = {"1":"1","6":"9", "8":"8", "9":"6", "0":"0"}
        string = str(N)
        for digit in string:
            if digit in digits_dict:
                continue
            return False
        for i in range(len(string)//2+1):
            if string[i] != digits_dict[string[len(string)-i-1]]:
                return True
        return False
       