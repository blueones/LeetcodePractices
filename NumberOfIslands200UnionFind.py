class Solution:
    def __init__(self):
        self.countIndi=0
        self.size=list()
    def numIslands(self, grid):
        ''' main function go through the grid, find neighboring island and see if they are also 1, if they are, then union. and deduct one from the total number of single islands'''
        if grid==[]:
            return 0
        row=len(grid)
        column=len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j]=="1":
                    self.countIndi+=1
        #print("countIndividual island is ",self.countIndi)
        #create a list like how we create a list in union find to represent each node in the grid. 
        self.listIndex=[x for x in range(row*column)]
        self.size=[1 for x in range(row*column)]
        #print(self.listIndex)
        for a in range(row):
            for b in range(column):
                if grid[a][b]=="0":
                    continue
                if b+1<=column-1 and grid[a][b+1]=="1":
                    self.union(a*column+b,a*column+b+1)
                if a+1<=row-1 and grid[a+1][b]=="1":
                    self.union(a*column+b,(a+1)*column+b)
        #print(self.listIndex)
        return self.countIndi
    def find(self,x):
        ''' being called find parent[] of nodes.''' 
        if self.listIndex[x]!=x:
            root=self.find(self.listIndex[x])
            self.listIndex[x]=root
            return root
        return self.listIndex[x]
    def union(self,x,y):
        ''' first check if parent of two nodes are the same. if not the same, then join them and deduct 1 from number of islands.---Combining of islands'''
        parentX=self.find(x)
        parentY=self.find(y)
        #print(parentX,parentY)
        if parentX==parentY:
            return None
        else:
            if self.size[parentX]<=self.size[parentY]:
                self.listIndex[parentX]=parentY
                print(self.listIndex)
                self.countIndi-=1
                self.size[parentY]=self.size[parentX]+self.size[parentY]
            else:
                self.listIndex[parentY]=parentX
                self.countIndi-=1
                self.size[parentX]=self.size[parentX]+self.size[parentY]



print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))