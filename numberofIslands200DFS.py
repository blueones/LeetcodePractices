class Solution1:
    def numIslands(self, grid):
        if grid==[]:
            return 0
        if grid!=[]:
            row=len(grid)
            leng=len(grid[0])
            listnodes=list()
            numI=0
            for i in range(row):
                for j in range(leng):
                    listnodes.append([i,j])
            for x in listnodes:
                if grid[x[0]][x[1]]=="1":
                    numI+=1
                    self.islands(grid,x)
                
                    
            return numI
            

    def islands(self,grid,node1):
        row=len(grid)
        leng=len(grid[0])
        grid[node1[0]][node1[1]]="0"
        if node1[1]-1>-1:
            node1left=[node1[0],node1[1]-1]
            if grid[node1[0]][node1[1]-1]=="1":
                self.islands(grid,node1left)
        if node1[1]+1<leng:
            node1right=[node1[0],node1[1]+1]
            if grid[node1[0]][node1[1]+1]=="1":
                self.islands(grid,node1right)
        if node1[0]-1>-1:
            node1up=[node1[0]-1,node1[1]]
            if grid[node1[0]-1][node1[1]]=="1":
                self.islands(grid,node1up)
        if node1[0]+1<row:
            node1down=[node1[0]+1,node1[1]]
            if grid[node1[0]+1][node1[1]]=="1":
                self.islands(grid,node1down)    
            
class Solution2:
    def numIslands(self,grid):
        self.row=len(grid)
        if self.row==0:
            return 0
        self.column=len(grid[0])
        self.listofNodes=[False for i in range(self.row*self.column)]
        self.islandsNumber=0
        for node in range(self.row*self.column):
            rowN=node//self.column
            columnN=node%self.column
            nodeValue=grid[rowN][columnN]
            if nodeValue=="1" and self.listofNodes[node]!=True:
                #print("entered")
                self.islandFinder(grid,node)
                self.islandsNumber+=1
        return self.islandsNumber
    def islandFinder(self,grid,node):
        rowN=node//self.column
        #print("rowN is ",rowN)
        columnN=node%self.column
        #print("columnN is ",columnN)
        nodeValue=grid[rowN][columnN]
        if self.listofNodes[node]!=True and nodeValue=="1":
            #print("node now is ",node)
            self.listofNodes[node]=True
            if rowN-1>-1:
                #print("entered 1")
                self.islandFinder(grid,node-self.column)
            if rowN+1<self.row:
                #print("entered 2")
                self.islandFinder(grid,node+self.column)
            if columnN-1>-1:
                #print("entered 3")
                self.islandFinder(grid,node-1)
            if columnN+1<self.column:
                #print("entered 4")
                self.islandFinder(grid,node+1)

        
                    
            
        


            

print(Solution2().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
        
