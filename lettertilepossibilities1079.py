class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.resultL = []
        self.resultNum = 0
        tiles = sorted(tiles)
        def DFS(start, currentL, stringT):
            lenT = len(stringT)
            if currentL !="":
                self.resultL.append(currentL)
                self.resultNum += 1
            for i in range(0, lenT):
                if i>0 and stringT[i]== stringT[i-1]:
                    continue
                currentL+=stringT[i]
                DFS(start+1, currentL, stringT[:i]+stringT[i+1:])
                currentL= currentL[:-1]
        DFS(0,"", tiles)
        return self.resultNum