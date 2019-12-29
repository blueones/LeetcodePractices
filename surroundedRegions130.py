class Solution:
    def solve(self, board):
        print(board)
        if board!=[]:
            row=len(board)
            leng=len(board[0])
            listBorder=list()
            for i in range(leng):
                listBorder.append([0,i])
                listBorder.append([row-1,i])
            for j in range(1,row-1,1):
                listBorder.append([j,0])
                listBorder.append([j,leng-1])
            networkNodes=list()
            for d in listBorder:
                if board[d[0]][d[1]]=="O":
                    networkNodes.append(d)
            for t in networkNodes:
                self.findNet(board,t)
            for x in range(row):
                for y in range(leng):
                    if board[x][y]=="T":
                        board[x][y]="O"
                    elif board[x][y]=="O":
                        board[x][y]="X"
            print(board)


    def findNet(self,board,node):
        #return a network of Os that are on the borders
        row=len(board)
        leng=len(board[0])
        #print("node is",node)
        if board[node[0]][node[1]]=="O":
            board[node[0]][node[1]]="T"
            #print(board)
            listNN=list()
            if node[0]+1<row-1:
                if board[node[0]+1][node[1]]=="O":
                    listNN.append([node[0]+1,node[1]])
            if node[1]+1<leng-1:
                if board[node[0]][node[1]+1]=="O":
                    listNN.append([node[0],node[1]+1])
            if node[0]-1>0:
                if board[node[0]-1][node[1]]=="O":
                    listNN.append([node[0]-1,node[1]])
            if node[1]-1>0:
                if board[node[0]][node[1]-1]=="O":
                    listNN.append([node[0],node[1]-1])
            #print(listNN)
            for i in listNN:
                self.findNet(board,i)
      
            
board=[["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

Solution().solve(board)
