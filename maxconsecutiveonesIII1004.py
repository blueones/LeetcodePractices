class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        #invariable is max number of K zeros in window.
        start = 0
        max_substring = 0
        len_string = len(A)
        counter = 0
        zeros = 0
        index = 0
        while index < len_string:
            
            if A[index]== 1:
                counter += 1
                
                
            else:
                if zeros == K:
                    while A[start]!= 0:
                        start += 1
                        counter -= 1
                    start += 1
                    
                else:
                    zeros += 1
                    counter += 1
            max_substring = max(max_substring, counter)
            index += 1
        return max_substring