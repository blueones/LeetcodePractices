class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if board == []:
            return []
        trie_words = Trie()
        row = len(board)
        column = len(board[0])
        visited = [[False for i in range(column)] for j in range(row)]
        self.ans = []
        def add_to_trie(word):
            current_node = trie_words.root
            for letter in word:
                if letter in current_node.children:
                    current_node = current_node.children[letter]
                else:
                    new_node = Node(letter)
                    current_node.children[letter] = new_node
                    current_node = current_node.children[letter]
            current_node.word = word
        for word in words:
            add_to_trie(word)
        def dfs(current_node, current_row, current_column):
            if visited[current_row][current_column] == False:
                visited[current_row][current_column] = True
                letter = board[current_row][current_column] 
                if letter in current_node.children:
                    current_node = current_node.children[letter]
            
                    if current_node.word != False:
                        self.ans.append(current_node.word)
                        current_node.word = False
                    
                    if current_row + 1 < row :
                        dfs(current_node, current_row+1, current_column)

                    if current_row - 1 >= 0 :
                        dfs(current_node, current_row-1, current_column)

                    if current_column + 1 < column :
                        dfs(current_node, current_row, current_column+1)
                    if current_column - 1 >= 0 :
                        dfs(current_node, current_row, current_column-1)
                visited[current_row][current_column] = False
            
        for i in range(row):
            for j in range(column):
                dfs(trie_words.root, i, j)
        
        
        return self.ans
                
                
                
        
class Node:
    def __init__(self, val):
        self.val = val
        self.word = False
        self.children = dict()
    
class Trie:
    def __init__(self):
        self.root = Node(None)
#     def add(self, word):
#         current_node = self.root
#         for letter in word:
#             if letter not in current_node.children:
                
#                 new_child = Node(letter)
#                 current_node.children[letter] = new_child
#             current_node = current_node.children[letter]
#         current_node.word = True
    def if_exist(self, word):
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False
        if current_node.word == False:
            return False
        return True
        