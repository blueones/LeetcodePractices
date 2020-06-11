class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.before = None
class DoublelyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = self.head
    def append_left(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.before = new_node
            self.head = self.head.before
        else:
            self.head = new_node
            self.tail = new_node
            
    def append(self, value):
        new_node = Node(value)
        
        new_node.before = self.tail
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node
    def pop(self):
        if self.tail == None:
            return None
        current_node = self.tail
        if self.tail.before:
            self.tail = self.tail.before
            self.tail.next.before = None
            self.tail.next = None
        else:
            self.tail = None
        
        return current_node.val
    def pop_left(self):
        if self.head == None:
            return None
        current_node = self.head
        if self.head.next:
            self.head= self.head.next
            self.head.before.next = None
            self.head.before = None
        else:
            self.head = None
        return current_node.val
    def is_empty(self):
        if self.head == None:
            return True
        return False
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        linkedlist = DoublelyLinkedlist()
        pointer = 0
        for num in nums:
            if num == 2:
                linkedlist.append(2)
            elif num == 1:
                linkedlist.append_left(1)
            else:
                nums[pointer] = 0
                pointer += 1
        while not linkedlist.is_empty():
            
            current = linkedlist.pop_left()
            nums[pointer] = current
            pointer += 1