#given an array of integers, 
# each element is to be divided by an integer 
# so that the sum of the results is less than or equal to a threshold integer. 
# each non-integer result of division is rounded up before it's added to the sum. 
# for example, 1/9 = 0.111.... round up to 1. 
# determine the minimum divisor to make the sum less than or equal to the threshold.
 #example
 # arr = [1,5,7]
 #threshold = 8
# if the divisor is 1, the result are arr = [1,5,7] which sums to 13, 
# which is greater than the threshold 8.andif the divisor is 2, 
# the results are arr = [1,3,4] which sums to 8, which is equal to the threshold 8.
# the minimum divisor to make the sum less than or equal to the threshold is 2. 
import math
class MinimumDivisor:
    def minimum_divisor(self, input_array, threshold):
        def divider(divide):
            divided = [math.ceil(i//divide) for i in input_array]
            return sum(divided)
        low = 1
        high = max(input_array)
        while low <= high:
            mid = (low+high)//2
            if divider(mid) <= threshold:
                high = mid-1
            else:
                low = mid+1
        return low
print(MinimumDivisor().minimum_divisor([1,5,7],8))

                                                                                                                        

