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
class LRUCache1:

    def __init__(self, capacity: int):
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.before = self.start
        self.dict_nodes = {}
        self.size = 0
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.dict_nodes:
            #remove from linkedlist and add to head
            current_node = self.dict_nodes[key]
            current_node.before.next = current_node.next
            current_node.next.before = current_node.before
            current_node.before = self.start
            self.start.next.before = current_node
            current_node.next = self.start.next
            self.start.next = current_node
            return current_node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict_nodes:
            self.dict_nodes[key].value = value
            current_node = self.dict_nodes[key]
            current_node.before.next = current_node.next
            current_node.next.before = current_node.before
            current_node.before = self.start
            self.start.next.before = current_node
            current_node.next = self.start.next
            self.start.next = current_node
        else:
            
            if self.size == self.capacity:
                deleted_node = self.end.before
                deleted_node.before.next = self.end
                self.end.before = deleted_node.before
                self.dict_nodes.pop(deleted_node.key)
                self.size -= 1
                self.put(key, value)
                
            else:
                new_node = Node(key,value)
                self.dict_nodes[key] = new_node
                self.start.next.before = new_node
                new_node.next = self.start.next
                new_node.before = self.start
                self.start.next = new_node
                self.size += 1


        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.before = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
