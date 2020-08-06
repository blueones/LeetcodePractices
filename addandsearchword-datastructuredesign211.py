class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.add_word(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_trie(trie, word):
            current = trie
            length = len(word)
            index = 0
            while index < length:
                cha = word[index]
                if cha != ".":
                    if cha in current.chas:
                        current = current.chas[cha]
                        index += 1
                    else:
                        return False
                else:
                    for child in current.chas:
                        if search_in_trie(current.chas[child], word[index+1:]):
                            return True
                    return False


            if current.word == True:
                return True
            return False
        return search_in_trie(self.trie.root, word)
                
                
class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    def add_word(self, word):
        current = self.root
        for cha in word:
            if cha in current.chas:
                current = current.chas[cha]
            else:
                current.chas[cha] = TrieNode(cha)
                current = current.chas[cha]
        current.word = True
    def search_word(self, word):
        current = self.root
        for cha in word:
            if cha in current.chas:
                current = current.chas[cha]
            else:
                return False
        if current.word == True:
            return True
        return False
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.chas = defaultdict()
        self.word = False
