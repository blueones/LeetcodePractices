class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.before = None


class doublyLinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def enqueue(self,valueN):
        newN = Node(valueN)
        if self.head == None:
            self.head = newN
            self.tail = newN
        elif self.head != None:
            newN.next = self.head
            self.head.before = newN
            self.head = newN
        self.length += 1
    def dequeue(self):
        if self.tail == None:
            return "this queue is empty now"
        elif self.tail != None:
            returnN = self.tail
            if self.tail == self.head:
                self.tail = self.head = None
            elif self.tail != self.head:
                self.tail.before.next = None
                self.tail = self.tail.before
            self.length -= 1
            return returnN.val
        

class doublyLinkedListStack:
    def __init__(self):
        self.head = None
        self.length = 0
    def push(self, valueN):
        newN = Node(valueN)
        if self.head == None:
            self.head = newN
        elif self.head != None:
            newN.next = self.head
            self.head.before = newN
            self.head = newN
        self.length += 1
    def pop(self):
        if self.head == None:
            raise Exception("the list is empty now")
        elif self.head != None:
            returnN = self.head
            self.head = self.head.next
            if self.head !=None:
                self.head.before = None
            self.length -= 1
            return returnN.val
try:
    dllQueue = doublyLinkedListQueue()
    dllStack = doublyLinkedListStack()
    dllQueue.enqueue(1)
    dllQueue.enqueue(2)
    dllQueue.enqueue(3)
    dllQueue.enqueue(4)
    print(dllQueue.dequeue())
    print(dllQueue.dequeue())
    print(dllQueue.dequeue())
    print(dllQueue.dequeue())
    print(dllQueue.dequeue())
    dllStack.push(2)
    dllStack.push(3)
    print(dllStack.pop())
    print(dllStack.pop())
    print(dllStack.pop())
except:
    print(Exception)
