class Node:
    def __init__(self, val):
        self.val = val
        self.word = False
        self.children = dict()
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for cha in word:
            if cha in current_node.children:
                current_node = current_node.children[cha]
            else:
                current_node.children[cha] = Node(cha)
                current_node = current_node.children[cha]
        current_node.word = True
                
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for cha in word:
            if cha in current_node.children:
                current_node = current_node.children[cha]
            else:
                return False
        if current_node.word == True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for cha in prefix:
            if cha in current_node.children:
                current_node = current_node.children[cha]
            else:
                return False
        
        return True
        