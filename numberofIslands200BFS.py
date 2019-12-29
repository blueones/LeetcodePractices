class Solution:
    def numIslands(self, grid):
        if len(grid)==0:
            return 0
        self.row=len(grid)
        self.column=len(grid[0])
        self.visited=[False for n in range(self.row*self.column)]
        self.islands=0
        for node in range(self.row*self.column):
            queueNodes=list()
            rowNode=node//self.column
            columnNode=node%self.column
            if grid[rowNode][columnNode]=="1" and self.visited[node]==False:
                self.islands+=1
                print(self.islands,"node is ",node)
                queueNodes.append(node)
                self.visited[node]=True
                while queueNodes!=[]:
                    nodeCurrent=queueNodes.pop(0)
                    rowCurrent=nodeCurrent//self.column
                    columnCurrent=nodeCurrent%self.column
                    print("nodeCurrent is ",nodeCurrent)
                    if rowCurrent+1<self.row and self.visited[nodeCurrent+self.column]==False:
                        if grid[rowCurrent+1][columnCurrent]=="1":
                            queueNodes.append(nodeCurrent+self.column)
                            self.visited[nodeCurrent+self.column]=True
                    if columnCurrent+1<self.column and self.visited[nodeCurrent+1]==False:
                        if grid[rowCurrent][columnCurrent+1]=="1":
                            queueNodes.append(nodeCurrent+1)
                            self.visited[nodeCurrent+1]=True
                    if rowCurrent-1>-1 and self.visited[nodeCurrent-self.column]==False:
                        if grid[rowCurrent-1][columnCurrent]=="1":
                            queueNodes.append(nodeCurrent-self.column)
                            self.visited[nodeCurrent-self.column]=True
                    if columnCurrent-1>-1 and self.visited[nodeCurrent-1]==False:
                        if grid[rowCurrent][columnCurrent-1]=="1":
                            queueNodes.append(nodeCurrent-1)
                            self.visited[nodeCurrent-1]=True
                    
            else:
                continue
                
        return self.islands

print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))