class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.dblist = DoublelyLinkedList()
        
        

    def push(self, x: int) -> None:
        new = self.dblist.add(x)
        self.stack.append(new)

    def pop(self) -> int:
        popped = self.stack.pop(-1)
        while popped.exist == False:
            popped = self.stack.pop(-1)
        self.dblist.remove(popped)
        return popped.key
        
        

    def top(self) -> int:
        while self.stack[-1].exist != True:
            self.stack.pop(-1)
        return self.stack[-1].key

    def peekMax(self) -> int:
        return self.dblist.peekMax()

    def popMax(self) -> int:

        return self.dblist.popMax()
class Node:
    def __init__(self, key):
        self.key = key
        self.exist = True
        self.next = None
        self.before = None
class DoublelyLinkedList:
    def __init__(self):
        self.head = Node(float("inf"))
        self.tail = Node(float("-inf"))
        self.head.next = self.tail
        self.tail.before = self.head
    def add(self, key):
        new_node = Node(key)
        current = self.head
        while key < current.key:
            current = current.next
        current.before.next = new_node
        new_node.before = current.before
        current.before = new_node
        new_node.next = current
        return new_node
    def remove(self, node):
        node.next.before = node.before
        node.before.next = node.next
        node.exist = False
    def peekMax(self):
        return self.head.next.key
    def popMax(self):
        max_node = self.head.next
        max_node.exist = False
        self.head.next = max_node.next
        max_node.next.before = self.head
        
        return max_node.key