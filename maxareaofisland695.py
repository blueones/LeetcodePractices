class Solution:
    def maxAreaOfIsland(self, grid):
        #union find. review.
        row = len(grid)
        column = len(grid[0])
        self.dictEle = [i for i in range(row*column)]
        self.islandsize = [1 for j in range(row*column)]
        self.maxSize = 0
        
        def find(x):
            parentLooker = x
            while self.dictEle[parentLooker] != parentLooker:
                parentLooker = self.dictEle[parentLooker]
            return parentLooker
        def union(x,y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if self.islandsize[parentX]< self.islandsize[parentY]:
                    self.islandsize[parentY] += self.islandsize[parentX]
                    self.maxSize = max(self.maxSize,self.islandsize[parentY])
                    self.dictEle[parentX] = parentY
                else:
                    self.islandsize[parentX] += self.islandsize[parentY]
                    self.maxSize = max(self.maxSize,self.islandsize[parentX])
                    self.dictEle[parentY] = parentX
        for a in range(row):
            for b in range(column):
                if grid[a][b] == 0:
                    continue
                else:
                    if b + 1 < column and grid[a][b+1] == 1:
                        union(a*column+b, a*column+b+1)
                    if a+1 < row and grid [a+1][b] == 1:
                        union(a*column+b, (a+1)*column+b)
                    else:
                        self.maxSize = max(self.maxSize, self.islandsize[a*column+b])
        import pdb; pdb.set_trace()
        return self.maxSize
            
Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])

        