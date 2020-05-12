class Solution:
    #TLE Solution. backtracking. recursion
    def ways(self, pizza: List[str], k: int) -> int:
        self.ans = 0
        def helper(left, right, up, down, k):
            if left < right and up < down:
                if k == 0:
                    good_piece = False
                    for i in range(left,right):
                        for j in range(up, down):
                            if pizza[j][i] == "A":
                                good_piece = True
                                break
                        if good_piece == True:
                            break
                    if good_piece:
                        self.ans += 1
                        self.ans = self.ans%(10**9+7)
                else:
                    cut = False
                    for i in range(left, right-1):
                        if cut:
                            helper(i+1, right, up, down, k-1)
                        else:
                            for j in range(up, down):
                                if pizza[j][i] == "A":
                                    cut = True
                                    break
                            if cut:
                                helper(i+1, right, up, down, k-1)
                        
                    cut = False
                    for x in range(up, down-1):
                        if cut:
                            helper(left, right, x+1, down, k-1)
                        else:
                            for y in range(left, right):
                                if pizza[x][y] =="A":
                                    cut = True
                                    break
                            if cut:
                                helper(left, right, x+1, down, k-1)
                        
        helper(0, len(pizza[0]), 0, len(pizza), k-1)
        return self.ans%(10**9+7)