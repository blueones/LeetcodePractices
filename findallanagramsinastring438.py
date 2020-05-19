class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        array_p = [0 for i in range(26)]
        for chara in p:
            array_p[ord(chara) - ord("a")] += 1
        window_length = 0
        array_s = [0 for i in range(26)]
        ans = []
        for index in range(len(s)):
            
            array_s[ord(s[index]) - ord("a")] += 1
            window_length += 1
            if window_length > len(p):
                array_s[ord(s[index-len(p)]) - ord("a")] -= 1
                window_length -= 1
            
            if array_s == array_p:
                ans.append(index - len(p) +1)
        return ans
        
        