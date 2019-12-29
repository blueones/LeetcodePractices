class Solution:
    '''find all regions where there is at least a member on the border. flag it, 
    then turn all the rest of the O(the surrounded ones) into X, 
    then turn all the flaged ones into O. be done with the search. 
         '''

    def findregions(self,x):
        pass
    def unionregions(self,x,y):
        '''rowNx=x//self.column
        columnNx=x%self.column
        rowNy=y//self.column
        columnNy=y%self.column'''
        if self.findregions(x)==self.findregions(y):
            return None
        else:
            pass

    
    def solve(self, board):
        #create a list of each node's root. 
        if board!=[]:
            self.row=len(board)
            self.column=len(board[0])
            self.rootlist=[i for i in range(self.row*self.column)]
            #create the list of index where nodes are on the border and equals to "O"
            listofborder=list()
            listofborder.extend(range(self.column))
            for i in range(1,self.row-1,1):
                listofborder.append(i*self.column)
                listofborder.append(i*self.column+self.column-1)
            listofborder.extend(range(self.row*self.column-1,self.row*self.column-self.column-1,-1))
            dictofborder={i:i for i in listofborder}
            #listofborder includes all the nodes on the border. 
            for root in self.rootlist:
                rowN=root//self.column
                columnN=root%self.column
                if board[rowN][columnN]=="O":
                    if rowN+1<self.row-1 and board[rowN+1][columnN]=="O":
                        self.unionregions(root,root+self.column)
                    if columnN+1< self.column-1 and board[rowN][columnN+1]=="O":
                        self.unionregions(root,root+1)
            


            
Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])