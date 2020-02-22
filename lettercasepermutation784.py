class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
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
