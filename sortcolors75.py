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

class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums)-1
        pointer = 0
        while pointer <= two:
            
                if nums[pointer] == 0:
                    nums[pointer],nums[zero] = nums[zero], nums[pointer]
                    zero += 1
                    pointer += 1
                elif nums[pointer] == 2:
                    nums[pointer],nums[two] = nums[two],nums[pointer]
                    two -= 1
                else:
                    pointer += 1
                    
            