class Solution:
    #solution to create a ordereddictionary
    def firstUniqChar(self, s: str) -> int:
        ordered_dict = OrderedDict()
        for index in range(len(s)):
            ordered_dict.add(s[index], index)
        last_unique = ordered_dict.pointer
        
        if last_unique != ordered_dict.head:
            return ordered_dict.head.next.index
        return -1
        
class Node:
    def __init__(self, key,index, val):
        self.key = key
        self.val = val
        self.index = index
        self.next = None
        self.before = None
class OrderedDict:
    def __init__(self):
        self.head = Node(0, 0, 0)
        self.pointer = self.head
        self.tail = Node(0, 0, 0)
        self.head.next = self.tail
        self.tail.before = self.head
        self.dict = {}
    def add(self, key, index):
        if key in self.dict:
            if self.dict[key].val == 1:
                if self.pointer == self.dict[key]:
                    self.pointer = self.dict[key].before
                self.dict[key].val += 1
                self.move(self.dict[key])
            else:
                self.dict[key].val += 1
        else:
            new_node = Node(key,index, 1)
            self.pointer.next.before = new_node
            new_node.next = self.pointer.next
            self.pointer.next = new_node
            new_node.before = self.pointer
            self.pointer = self.pointer.next
            print(self.pointer.key)
            self.dict[key] = new_node
                
                
    def move(self, node):
        node.next.before = node.before
        node.before.next = node.next
        node.next = self.tail
        self.tail.before.next = node
        node.before = self.tail.before
        self.tail.before = node
class Solution1:
    def firstUniqChar(self, s):
        dict_s = {}
        for letter in s:
            if letter in dict_s:
                dict_s[letter] += 1
            else:
                dict_s[letter] = 1
        for index in range(len(s)):
            if dict_s[s[index]] == 1:
                return index
        return -1