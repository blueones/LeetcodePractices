class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.listW = dictionary
        self.lenL = len(dictionary)
        self.dict = {}
        self.mark = {}
        

    def isUnique(self, word: str) -> bool:
        for item in self.listW:
            if len(item) < 3:
                abb = item
                if abb in self.mark:
                    return False
                else:
                    
                self.dict[item] = item
                
            else:
                self.dict[item]= item[0]+str(len(item)-2)+item[-1]
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)