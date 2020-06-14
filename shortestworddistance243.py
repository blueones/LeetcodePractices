class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dict_words = dict()
        for index, word in enumerate(words):
            if word in dict_words:
                dict_words[word].append(index)
            else:
                dict_words[word] = [index]
        locations1 = dict_words[word1]
        locations2 = dict_words[word2]
        index1 = index2 = 0
        smallest = float("inf")
        while index1 < len(locations1) and index2 < len(locations2):
            new_distance = abs(locations1[index1] - locations2[index2])
            smallest = min(smallest, new_distance)
            if locations1[index1]> locations2[index2]:
                index2 += 1
            else:
                index1+= 1
        return smallest
class Solution1:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        smallest = len(words)
        loc1 = loc2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                loc1 = i
            elif words[i] == word2:
                loc2 = i
            if loc1 != -1 and loc2 != -1:
                smallest = min(smallest, abs(loc1-loc2))
        return smallest