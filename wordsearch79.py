class Solution:
    def exist(self, board, word):
        #using visited to mark which are the ones visited.
        #comparing with LC323, this problem though we still want to be able to visit the nodes if the nodes were visited in a earler round. so backtracking is important in this case.
        # thus using self.visited
        self.row = len(board)
        self.column = len(board[0])
        self.visited = [False for i in range(self.row*self.column)]
        self.word = word

        def helper(index,row_index, column_index):
            if index == len(self.word):
                    return True
            if row_index>-1 and row_index< self.row and column_index>-1 and column_index<self.column:
                
                
                if self.visited[row_index*self.column+column_index]==True:
                    return False
                if board[row_index][column_index]==self.word[index]:
                    self.visited[row_index*self.column+column_index]= True
                    if helper(index+1,row_index+1,column_index):
                        return True
                    if helper(index+1,row_index-1,column_index):
                        return True
                    if helper(index+1,row_index,column_index+1):
                        return True
                    if helper(index+1,row_index,column_index-1):
                        return True
                self.visited[row_index*self.column+column_index]= False
            else:
                return False

        for row_index in range(self.row):
            for column_index in range(self.column):
                if not helper(0,row_index,column_index):
                    continue
                else:
                    return True
        return False
Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")