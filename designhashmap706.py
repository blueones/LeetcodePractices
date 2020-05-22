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