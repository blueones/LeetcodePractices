class Solution:
    #the algorithm is to find all the networks with at least a "O" on the border.
    #mark these nodes in these networks "A", then turn all the rest of the "O"s(they will be insider "O"s) to X,
    #then turn all the "A"s into "O"
    '''
    1. find rootnodes.
    2. find networks(graph BFS/DFS).
    '''
    def solve(self, board):
        row=len(board)
        if row>0:
            line=len(board[0])
        else:
            line=0

        
        for i in range(1,row-1,1):
            for j in range(1,line-1,1):
                if board[i][j]=="O":

    def dfs():

                    


Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
        