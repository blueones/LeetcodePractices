class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        list_words = paragraph.replace(","," ").split(" ")
        banned_set = set(banned)
        dict_words = {}
        for word in list_words:
            word_lower = word.lower()
            if word == "":
                continue
            if word_lower[-1].isalpha() == False:
                word_lower= word_lower[:-1]
            if word_lower in dict_words:
                dict_words[word_lower] += 1
            else:
                dict_words[word_lower] = 1
        
        sorted_words = sorted(dict_words,reverse = True, key = lambda x:dict_words[x])
        
        for word in sorted_words:
            if word in banned_set:
                continue
            return word
            