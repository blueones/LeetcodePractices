class Solution:
    def longestRepeatingSubstring(self, S):
        lenS=len(S)
        resultL=set()
        for i in range(1,lenS-1,1):
            counter=0
            for index in range(0,lenS-i,1):
                if S[index]!=S[index+i]:
                    counter=0
                if S[index]==S[index+i]:
                    counter+=1
                resultL.add(counter)
        return max(resultL)




class Solution1:
    def longestRepeatingSubstring(self, S: str) -> int:
        lenS=len(S)
        ans = 0
        for i in range(1,lenS-1,1):
            counter=0
            for index in range(0,lenS-i,1):
                if S[index]!=S[index+i]:
                    counter=0
                else:
                    counter+=1
                ans = max(ans,counter)
        return ans