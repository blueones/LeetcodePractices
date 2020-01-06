from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.length=0
        self.cap=capacity
        self.cache=OrderedDict()

    def get(self, key: int) -> int:
        if self.length==0 or key not in self.cache:
            return -1
        else:
            value=self.cache[key]
            del self.cache[key]
            self.length-=1
            self.put(key,value)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if self.length==self.cap:
            if key in self.cache:
                del self.cache[key]
                self.cache[key]=value
            else:
                self.cache.popitem(last=False)
                self.cache[key]=value
        else:    
            if key not in self.cache:
                self.length+=1
                self.cache[key]=value
            else:
                del self.cache[key]
                self.cache[key]=value
            
        print("putting key ",key, "now dic is ", self.cache)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
obj=LRUCache(2)
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
obj.get(1)
obj.get(2)