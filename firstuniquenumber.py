class OrderedDictionary:
    def __init__(self, nums):
        self.dict_nodes = dict()
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.valid_tail = self.start
        self.size = 0
        self.start.next = self.end
        self.end.before = self.start
        for num in nums:
            self.add(num)
        
    def add(self, key):
        if key in self.dict_nodes:
            self.update(key)
        
            
        else:
            node = Node(key,1)
            self.dict_nodes[key] = node
            self.valid_tail.next.before = node
            node.next = self.valid_tail.next
            self.valid_tail.next = node
            node.before = self.valid_tail
            self.valid_tail = self.valid_tail.next
            self.size += 1

    def update(self, key):
        node = self.dict_nodes[key]
        if node.val == 1:
            if self.valid_tail == node:
                self.valid_tail = node.before
            node.before.next = node.next
            node.next.before = node.before
            self.end.before.next = node
            node.before = self.end.before
            node.next = self.end
            self.end.before = node
            self.size -= 1
        node.val += 1
    def peek(self):
        if self.size == 0:
            return -1
        else:
            return self.start.next.key
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.before = None
        self.next = None
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.number = len(nums)
        self.OrderedDictionary = OrderedDictionary(nums)

    def showFirstUnique(self) -> int:
        return self.OrderedDictionary.peek()

    def add(self, value: int) -> None:
        self.OrderedDictionary.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)