class Solution:
    def displayTable(self, orders) :
        #definitely needs improvement.
        tables = {}
        food = {}
        for order in orders:
            
            tables[order[1]] = None
            
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



print(Solution1().displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
                