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