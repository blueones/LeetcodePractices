class Solution:
    def letterCombinations(self, digits):
        #recursion
        self.map = {"2":['a','b','c'], "3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'], "6":['m','n','o'], "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}
        ans = []
        if digits == "":
            return []
        for item in self.map[digits[0]]:
            if self.letterCombinations(digits[1:]):
                for follow in self.letterCombinations(digits[1:]):
                    ans.append(item+follow)
            else:
                ans.append(item)
        return ans
class Solution1:
    def letterCombinations(self,digits):
        #backtracking
        self.digits = digits
        self.map = {"2":['a','b','c'], "3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'], "6":['m','n','o'], "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}
        lenD = len(digits)
        self.ans = []
        def backtracking(stringS,index):
            if index == lenD:
                self.ans.append(stringS)
            else:
                for valueS in self.map[self.digits[index]]:

                    newString = stringS + valueS
                    backtracking(newString,index+1)
        if lenD == 0:
            return []
        backtracking("",0)
        return self.ans

