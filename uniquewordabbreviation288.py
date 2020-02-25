class ValidWordAbbr:
    #a lot of edge cases. first AC answer. 
    def __init__(self, dictionary):
        self.listW = dictionary
        self.lenL = len(dictionary)
        self.dictSet = dict()
        self.mark = set()
        for item in self.listW:
            if item not in self.mark:
                self.mark.add(item)
                abb = self.abbreviation(item)
                if abb not in self.dictSet:
                    self.dictSet[abb]=1
                else:
                    self.dictSet[abb] +=1

    def isUnique(self, word: str) -> bool:
        abbW = self.abbreviation(word)
        if abbW in self.dictSet:
            if word in self.listW and self.dictSet[abbW]==1:
                return True
            else:
                return False
        return True
    def abbreviation(self,word):
        lenW = len(word)
        if lenW <3:
            return word
        else:
            return word[0]+str(lenW-2)+word[-1]
stringE=ValidWordAbbr(["hello"])
print(stringE.isUnique('hello'))

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
class ValidWordAbbr1:
    #a lot of edge cases. first AC answer. 
    def __init__(self, dictionary):
        self.listW = dictionary
        self.lenL = len(dictionary)
        self.dictSet = dict()
        self.mark = set()
        for item in self.listW:
            if item not in self.mark:
                self.mark.add(item)
                abb = self.abbreviation(item)
                if abb not in self.dictSet:
                    self.dictSet[abb]=1
                else:
                    self.dictSet[abb] +=1

    def isUnique(self, word: str) -> bool:
        abbW = self.abbreviation(word)
        if abbW in self.dictSet:
            if word in self.listW and self.dictSet[abbW]==1:
                return True
            else:
                return False
        return True
    def abbreviation(self,word):
        lenW = len(word)
        if lenW <3:
            return word
        else:
            return word[0]+str(lenW-2)+word[-1]