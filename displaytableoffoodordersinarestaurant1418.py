class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        #definitely needs improvement.
        tables = {}
        food = {}
        for order in orders:
            if order[1] not in tables:
                tables[order[1]] = None
            if order[2] not in food:
                food[order[2]] = None
        food_kinds = len(food)
        tables_num = len(tables)
        display_table = [["0" for i in range(food_kinds+1)] for j in range(tables_num+1)]
        display_table[0][0] = "Table"
        row_table = 1
        tables = dict(sorted(tables.items(),key = lambda x:int(x[0])))
        for table in tables:
            display_table[row_table][0]= table
            tables[table] = row_table
            row_table+=1
        column_table = 1
        food = dict(sorted(food.items(),key = lambda x:x[0]))
        for food_item in food:
            display_table[0][column_table]= food_item
            food[food_item]= column_table
            column_table +=1
            
        for order in orders:
            if display_table[tables[order[1]]][food[order[2]]] == "0":
                display_table[tables[order[1]]][food[order[2]]]="1"
            else: 
                display_table[tables[order[1]]][food[order[2]]]=str(int(display_table[tables[order[1]]][food[order[2]]])+1)
        return display_table
                