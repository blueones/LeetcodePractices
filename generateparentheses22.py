class Solution1:
    def generateParenthesis(self, n):
        #backtracking question first time
        # if there is still "(" left, then append"(".
        # if it wouldn't exceed the number of left "(", the we can append ")"
        # recursion
        answerList = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                answerList.append(S)
            if left < n:
                backtrack(S+"(", left +1, right)
            if right < left:
                backtrack(S+")", left, right +1)
        backtrack("",0,0)
        return answerList
print(Solution().generateParenthesis(3))


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        #Solution from May 2019.
        list1=list()
        for a in range (2*n):
            if a==0:
                list1.append('(')
                continue
            newlist = []
            for l in list1:
                leftP=0
                rightP=0
                for items in l:
                    if items=="(":
                        leftP+=1
                    elif items==")":
                        rightP+=1
                if leftP>rightP and leftP<n:
                    newlist.append(l+'(')
                    newlist.append(l+')')
                elif leftP>rightP and leftP==n:
                    newlist.append(l+')')
                elif leftP==rightP and leftP<n:
                    newlist.append(l+'(')
            list1 = newlist
        return list1    