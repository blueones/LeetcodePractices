class Solution:
    def letterCasePermutation(self, S) :
        self.resultL = []
        lenS = len(S)
        def backtracking(index,current):
            if index == lenS:
                self.resultL.append(current)
                
            else:
                currentI = S[index]
                if currentI.isdecimal():
                    current+=currentI
                    backtracking(index+1,current)
                else:
                    current += currentI.upper()
                    backtracking(index+1,current)
                    current=current[:-1]
                    current += currentI.lower()
                    backtracking(index+1,current)
        backtracking(0,"")
        return self.resultL
class Solution1:
    def letterCasePermutation(self,S):
        if S:
            if S[0].isalpha():
                currentL = [S[0].upper(), S[0].lower()]
            else:
                currentL = [S[0]]
            res = []
            for item in self.letterCasePermutation(S[1:]):
                for stringC in currentL:
                    res.append(stringC + item)
            #wrong answer: think about it's not what you want. easily made mistake
            # for item in self.letterCasePermutation(s[1:]):
            #     for i in range(len(currentL)):
            #         currentL[i] += item
            return res
        else:
            return [""]#very easily made mistake here. 

Solution1().letterCasePermutation("a1b1")           