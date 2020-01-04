class Solution:
    def isValid(self, s) :
        if s=="":
            return True
        leftP=['[','{','(']
        rightP=[']','}',')']
        parenStack=list()
        if s[0] in leftP:
            for letter in s:
                print(letter)
                if letter in leftP:
                    parenStack.append(letter)
                elif letter in rightP:
                    if parenStack==[]:
                        return False
                    if rightP.index(letter)==leftP.index(parenStack[-1]):
                        parenStack.pop(-1)
                    else:
                        return False
            if parenStack==[]:
                return True
        return False
class Solution2:
    def isvalid(self,s):
        pass
print(Solution().isValid("[]")))