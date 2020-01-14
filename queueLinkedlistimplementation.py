class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self,val):
        if self.isEmpty():
            self.head=self.tail=Node(val)
            #print("first time head and tail", self.head.data,self.tail.data)
        else:
            oldtail=self.tail
            self.tail=Node(val)
            oldtail.next=self.tail
        #print(self.head.data,self.tail.data)
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            head=self.head
            self.head=head.next
            if self.isEmpty():
                self.tail=self.head
            return head.data
    def isEmpty(self):
        return self.head==None
linkedlist1=LinkedList()
linkedlist1.enqueue(3)
linkedlist1.enqueue(4)
linkedlist1.enqueue(5)
linkedlist1.enqueue(6)
print(linkedlist1.dequeue())
print(linkedlist1.dequeue())
print(linkedlist1.dequeue())
print(linkedlist1.dequeue())