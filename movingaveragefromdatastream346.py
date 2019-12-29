class MovingAverage1:

    def __init__(self, size):
        self.queueStream=list()
        self.windowsize=size
        self.queuesize=0
        

    def next(self, val):
        self.queueStream.append(val)
        self.queuesize+=1
        if self.queuesize<self.windowsize:
            return sum(self.queueStream)/self.queuesize
        else:
            total=0
            for indexofnum in range(self.queuesize, self.queuesize-self.windowsize, -1):
                total+=self.queueStream[indexofnum-1]
            return total/self.windowsize

        #append val to queue, enqueue
        #calculate from the newest one to size last ones
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
class MovingAverage2:#writing in array
    def __init__(self,size):
        self.stream=list()
        self.windowsize=size
        self.size=0
    def dequeue(self):
        self.stream.pop(0)
        self.size-=1
    def enqueue(self,val):
        self.stream.append(val)
        self.size+=1
    def next(self,val):
        self.enqueue(val)
        if self.size>self.windowsize:
            self.dequeue()
            return sum(self.stream[-self.windowsize:])/self.windowsize
        else:
            return sum(self.stream)/self.size
        #when self.stream's len is over self.window size, always dequeue. but enqueue first and then dequeue. then do the average calculation.
        

class MovingAverage3: #writing in linked list
    def __init__(self,size):
        self.windowsize=size
        self.linkedListQueue=linkedListQueue()
        self.size=0
        self.currentsum=0
    def next(self,val):
        #for queue smaller than window size
        if self.size<self.windowsize:
            self.size+=1
            self.linkedListQueue.enqueue(val)
            self.currentsum+=val
            return self.currentsum/self.size
        elif self.size==self.windowsize:
            oldfirstnode=self.linkedListQueue.first
            self.linkedListQueue.enqueue(val)
            self.linkedListQueue.dequeue()
            self.currentsum-=oldfirstnode.data
            self.currentsum+=val
            return self.currentsum/self.windowsize

        #for queue equal to window size

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedListQueue:
    def __init__(self):
        self.first=None
        self.last=None
    def enqueue(self,val):
        
        lastNode=self.last
        self.last=Node(val)
        if not self.isEmpty():
            lastNode.next=self.last
        else:
            self.first=self.last=Node(val)
    def dequeue(self):
        if self.isEmpty():
            return None
        firstNode=self.first
        self.first=self.first.next
        if self.isEmpty():
            self.last=None
        return firstNode.data
    def isEmpty(self):
        return self.first==None
