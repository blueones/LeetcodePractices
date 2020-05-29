class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.string = characters
        self.lengthString = len(characters)
        self.length = combinationLength
        self.listofcombined = []
        self.__create__("",0, 0)
        self.resultL = len(self.listofcombined)
        # print(self.listofcombined)
        self.pointer = 0
    def __create__(self, stringC, index, cumuNum):
        if cumuNum == self.length:
            self.listofcombined.append(stringC)
            
        else:
            for i in range(index, self.lengthString):
                self.__create__( stringC + self.string[i] , i+1, cumuNum+1)
        
        
            
            
        
        

    def next(self) -> str:
        if self.hasNext():
            returnV = self.listofcombined[self.pointer]
            self.pointer += 1
            return returnV
        

    def hasNext(self) -> bool:
        if self.pointer < self.resultL:
            return True
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.string = characters
        self.lengthString = len(characters)
        self.length = combinationLength
        self.start = False
        self.current = self.string[:self.length]
        self.index = [i for i in range(self.length)]
    def __create__(self, current_string, index):
        for i in range(self.length-1, -1, -1):
            if index[i]!= self.lengthString-1-(self.length-1-i):
                index[i] += 1
                for j in range(i+1, self.length):
                    index[j] = index[i]+(j-i)
                return index

    def next(self) -> str:
        if self.start == False:
            self.start = True
            return self.current
        else:
            if self.hasNext():
                self.index = self.__create__(self.current, self.index)

                self.current = "".join([self.string[i] for i in self.index])
                return self.current
        
        
        

    def hasNext(self) -> bool:
        for i in range(self.length-1, -1, -1):
            if self.index[i]!= self.lengthString-1-(self.length-1-i):
                return True
        return False
        
        
    