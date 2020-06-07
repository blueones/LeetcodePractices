class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        len_arr = len(arr)
        arr.sort()
        median_index = (len_arr-1)//2 
        median = arr[median_index]
        start = 0 
        end = len_arr-1
        count = 0
        ans = []
        while count < k:
            if (arr[end]-median) >= (median-arr[start]):
                ans.append(arr[end])
                end -= 1
                
            else: 
                ans.append(arr[start])
                start += 1
            count +=1
        return ans
        