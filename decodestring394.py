class Solution:
    def decodeString(self, s):
        #use stack please review excel sheet to find good explanation in youtube video for this solution.
        stackListNum = []
        stackListStr = []
        stringC = ""
        temp = ""
        lenS = len(s)
        i = 0
        while i < lenS:
            if s[i].isdecimal():
                numb = 0
                stackListStr.append(temp)
                temp = ""
                while s[i].isdecimal():
                    numb = numb*10+int(s[i])
                    i += 1
            elif s[i] == "[":
                stackListNum.append(numb)
                i+=1

            elif s[i] =="]":
                temp = stackListStr.pop(-1) + temp*stackListNum.pop(-1)
                i+=1
                
            else:
                temp += s[i]
                i+=1
        return temp

class Solution1:
    def decodeString(self,s):
        #recursion
        #same idea as solution but using recursion.
        self.dict={}
        lenS = len(s)
        def decode(s,begin, end):
            index = begin
            temp = ""
            numberR = ""
            inside = ""
            while index in range(begin, end):
                if s[index].isdecimal():
                    while s[index].isdecimal():
                        numberR += s[index]
                        index += 1
                    inside = decode(s,index+1,self.dict[index])
                    index = self.dict[index]-1
                elif s[index] == "]":
                    if numberR!="":
                        temp += int(numberR)*inside
                    else:
                        temp += inside
                    numberR = ""
                elif s[index].isalpha():
                    temp+=s[index]
                index+=1
            return temp
                   
        def parseString(s):
            stackL = []
            for i in range(lenS):
                if s[i] == "[":
                    stackL.append(i)
                elif s[i]=="]":
                    poppedP = stackL.pop(-1)
                    self.dict[poppedP]= i
        parseString(s)
        return decode(s,0,lenS)
print(Solution1().decodeString("3[a2[c]]"))       

