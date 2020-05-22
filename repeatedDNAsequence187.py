class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        window = s[:10]
        dict_sequence = {window: 1 }
        for i in range(10, len(s)):
            new_window = window[1:] + s[i]
            if new_window in dict_sequence:
                dict_sequence[new_window] += 1
            else:
                dict_sequence[new_window] = 1
            window = new_window
        ans = []
        for item in dict_sequence:
            if dict_sequence[item] > 1 :
                ans.append(item)
        return ans
        