import random
class RandomizedSet1:
    #a set and an array. general data structure is right. missing updating in remove method. see second solution

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = dict()
        self.array = list()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.random_set:
            return False
        self.random_set[val] = len(self.array)
        self.array.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.random_set:
            index = self.random_set[val]
            self.array[index] = None
            self.random_set.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        pick = math.floor(random.random()* len(self.array))
        if self.array[pick]!= None:
            return self.array[pick]
        else:
            return self.getRandom()
import random
class RandomizedSet1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = dict()
        self.array = list()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.random_set:
            return False
        self.random_set[val] = len(self.array)
        self.array.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.random_set:
            popped, last = self.random_set[val], self.array[-1]
            self.random_set[last] = popped
            self.array[popped] = self.array[-1]
            self.array.pop()
            self.random_set.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        pick = math.floor(random.random()* len(self.array))
        
        return self.array[pick]
        
