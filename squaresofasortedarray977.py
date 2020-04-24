class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [i**2 for i in A]
        #merge sort
        #find middle
        #merge sort
        start = 0
        end = len(A)
        while start< end:
            mid = (start+end)//2
            if A[mid] == 0:
                start = mid
                break
            elif A[mid]>0:
                end = mid
            else:
                start = mid+1
        mid = start
        resultL = []
        left_index = mid-1
        right_index = mid
        while left_index>= 0 or right_index < len(A):
            if left_index < 0:
                return resultL+result[right_index:]
            elif right_index > len(A)-1:
                leftside = result[:left_index+1]
                return resultL+leftside[::-1]
            elif result[left_index]<= result[right_index]:
                resultL.append(result[left_index])
                left_index -= 1
            elif result[left_index]> result[right_index]:
                resultL.append(result[right_index])
                right_index += 1
        return resultL