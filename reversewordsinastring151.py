class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return ""
        length_string = len(s)
        tail = length_string -1
        ans = ""
        def reverse_word(word):
            reversed = ""
            for index in range(len(word)-1, -1, -1):
                reversed += word[index]
            return reversed
        current_word = ""
        while tail >= 0 and s[tail] == " ":
            tail -= 1
        if tail == -1:
            return ""
        while tail >= 0:
            if s[tail] == " ":
                
                while s[tail] ==" ":
                    tail -= 1
                ans += reverse_word(current_word) +" "
                current_word = ""
            else:
                current_word += s[tail]
            
                tail -= 1
        ans += reverse_word(current_word)
          
                 
        return ans[:-1] if ans[-1] == " " else ans