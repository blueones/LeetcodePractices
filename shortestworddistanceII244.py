class WordDistance:

    def __init__(self, words: List[str]):
        self.word_dict = dict()
        for index,word in enumerate(words):
            if word in self.word_dict:
                self.word_dict[word].append(index)
            else:
                self.word_dict[word] = [index]

    def shortest(self, word1: str, word2: str) -> int:
        locations_word1 = self.word_dict[word1]
        locations_word2 = self.word_dict[word2]
        smallest = float("inf")
        start1 = 0
        start2 = 0
        while  start1 < len(locations_word1) and start2 < len(locations_word2):
            location1 = locations_word1[start1]
            location2 = locations_word2[start2]
            new_distance = abs(locations_word1[start1] - locations_word2[start2])
            if location1 < location2:
                start1 += 1
            else:
                start2 += 1
            
            smallest = min(smallest, new_distance)
            
        return smallest
            


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)