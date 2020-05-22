class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {order[index]:index for index in range(len(order))}
        def compare(wordA, wordB):
            #if wordA before wordB return True, else return False
            index = 0
            while index < len(wordA) and index< len(wordB) and wordA[index] == wordB[index]:
                index +=1
            if index < len(wordA) and index < len(wordB):
                if order_dict[wordA[index]] < order_dict[wordB[index]]:
                    return True
                return False
            else:
                if index == len(wordA) and index == len(wordB):
                    return True
                elif index == len(wordA):
                    return True
                return False
        for i in range(1, len(words)):
            if compare(words[i-1], words[i]) == False:
                return False
        return True
        