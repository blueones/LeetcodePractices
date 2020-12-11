#review of hashing. for this question, collisionn is not that big of a deal. so we could use these two solutions.
# in real engineering scenarios, a lot of times, we need to have cryptographic hash function, which means we don't store keys together with values, 
# then collision definitely needs to be avoided. Normally when the array to store hashed key values is over 10% capacity, we need to rehash and expand capacity. 
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [[] for i in range(3000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = Hash().hash(key)
        for index in range(len(self.array[hash_key])):
            if self.array[hash_key][index][0] == key:
                self.array[hash_key][index][1] = value
                break
        else:
            self.array[hash_key].append([key, value])
        
    
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = Hash().hash(key)
        for key_store,value in self.array[hash_key]:
            if key_store == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = Hash().hash(key)
        for index in range(len(self.array[hash_key])):
            if self.array[hash_key][index][0] == key:
                self.array[hash_key][index] = [None, None]
                
                
        
class Hash:
    def hash(self, key):
        hash_key = key% 3000
        return hash_key
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashed_list = [list() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed = key%100
        for index, key_value in enumerate(self.hashed_list[hashed]):
            if key_value[0] == key:
                self.hashed_list[hashed][index] = (key, value)
                return
        self.hashed_list[hashed].append((key,value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed = key%100
        for key_candidate, value in self.hashed_list[hashed]:
            if key_candidate == key:
                return value
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed = key%100
        for index, key_value in enumerate(self.hashed_list[hashed]):
            if key == key_value[0]:
                self.hashed_list[hashed][index] = self.hashed_list[hashed][-1]
                self.hashed_list[hashed].pop()
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)