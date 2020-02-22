class Solution:
    def expand(self, S):
        flag = False
        listOfItem = []
        for cha in S:
            if cha == "{":
                flag = True
                currentS = ""
            elif cha == "}":
                flag = False
                listOfItem.append(currentS)
            elif cha == ",":
                continue
            else:
                if flag:
                    currentS += cha
                else:
                    listOfItem.append(cha)
        
        def backtrack(listSt,index):
            res = []
            if index >= len(listSt):
                return [""]
            for chara in backtrack(listSt, index+1):
                for item in listSt[index]:
                    res.append(item+chara)
            return res
        return sorted(backtrack(listOfItem,0))

                



Solution().expand("{a,b}c{d,e}f")