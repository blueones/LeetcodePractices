from collections import defaultdict
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        #rolling hash
        #mod operations
        # hashing
        len_S = len(S)
        start = 1
        end = len_S - 1
        mod = 2**31-1
        base = 26
        
        def hashing(first, last, length):
            hashed = 0
            for i in range(first, last+1):
                hashed = (hashed*base + ord(S[i])-61)%mod
            return hashed%mod
            
        def hash_search(length):
            #rolling hash
            modlength = (base**(length))%mod
            visited = defaultdict(set)
            #first hash
            first_hashed = hashing(0, length-1, length)
            visited[first_hashed].add((0, length))
            for i in range(1, len_S - length+1):
              
                new_hashed = ((first_hashed*base)%mod - ((ord(S[i-1])-61)*modlength)%mod + mod +(ord(S[i+length-1])-61))%mod
                first_hashed = new_hashed
                
                if new_hashed in visited:
                    for possible_string in visited[new_hashed]:
                        if S[possible_string[0]:possible_string[1]] == S[i:i+length]:
                    
                            return (True, S[i:i+length])
                    
                
                visited[new_hashed].add((i, i+length))
                
            
            return (False,"")
        longest_sub = ""
        while start <= end:
            
            mid = (start+end)//2
            mid_duplicate, string_sub = hash_search(mid)
            if mid_duplicate:
                longest_sub = string_sub
                start = mid + 1
            else:
                end = mid - 1
        return longest_sub
            
               