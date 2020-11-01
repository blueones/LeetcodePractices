class Solution:
    def prisonbreak(self, row, column, horizontal_list, vertical_list):
        row_total = row+1
        column_total = column +1
        horizontal = set(horizontal_list)
        vertical = set(vertical_list)
        # def helper(column, )
        tmp = 1
        max_space = 1
        for i in range(1, row_total):
            if i in horizontal:
                tmp+=1
                max_space = max(max_space,tmp)
            else:
                tmp = 1
        

