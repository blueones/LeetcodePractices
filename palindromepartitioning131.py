class Solution:
    def partition(self, s) :
        lenS = len(s)
        matrix_palindrome = [[False for j in range(lenS)] for i in range(lenS)]
        for m in range(lenS):
            for left in range(lenS-m):
                right = left+m
                if left == right or left+1 == right:
                    matrix_palindrome[left][right] = ( s[left] == s[right] )
                else:
                    matrix_palindrome[left][right] = ( s[left] == s[right] and matrix_palindrome[left+1][right-1] )
        resultL = []
        def backtracking(s, begin,current_sofar):
            if begin>=lenS:
                resultL.append(current_sofar)
            elif begin<lenS:
                for right in range(begin,lenS):
                    if matrix_palindrome[begin][right]:
                        currentL=s[begin:right+1]
                        current_sofar.append(currentL)
                        backtracking(s,right+1,current_sofar[:])
                        current_sofar.pop(-1)
        backtracking(s,0,[])
        return resultL
Solution().partition("aab")
                


