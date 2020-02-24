class Solution:
    def generateAbbreviations(self, word):
        #recursion method
        if word == "":
            return [""]
        resultL = []
        for item in self.generateAbbreviations(word[1:]):
            if item == "" or item[0].isalpha():
                resultL.append(word[0]+item)
                resultL.append("1"+item)
            elif item[0].isdecimal():
                i = 0
                while i< len(item) and item[i].isdecimal():
                    i+=1
                resultL.append(word[0]+item)
                resultL.append(str(int(item[:i])+1)+item[i:])
            
        return resultL


Solution().generateAbbreviations("interaction")
class Solution1:
    def generateAbbreviations(self,word):
        #backtracking
        #grow the strings one char at a time. similiar to solution in LC784.
        lenW = len(word)
        self.ans = []
        def backtracking(index, construct, numberMarker):
            if index == len(word):
                if numberMarker == 0:
                    self.ans.append(construct)
                else:
                    self.ans.append(construct+str(numberMarker))
            else:
                if numberMarker != 0:
                    noSubC = construct+str(numberMarker)+word[index]
                else:
                    noSubC = construct + word[index]
                backtracking(index+1,noSubC,0)
                subC = construct
                backtracking(index+1,subC,numberMarker+1)
        backtracking(0,"",0)
        return self.ans