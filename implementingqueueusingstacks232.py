class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.length = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.length += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tempStack = []
        while self.stack:
            tempStack.append(self.stack.pop(-1))
        queueFront = tempStack.pop(-1)
        while tempStack:
            self.stack.append(tempStack.pop(-1))
        self.length -= 1
        return queueFront
        
class MyQueue1:
    #GOOD PERFORMANCE COMPARED WITH MYQUEUE 1. USE A STACK FOR INPUTTING AND ANOTHER STACK FOR CACHE(to pop from. refill from store stack when empty.)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackStore = []
        self.stackCache = []
        self.length = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackStore.append(x)
        self.length += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stackCache == []:
            while self.stackStore != []:           
                self.stackCache.append(self.stackStore.pop(-1))
        self.length -= 1
        return self.stackCache.pop(-1)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stackCache == []:
            while self.stackStore != []:           
                self.stackCache.append(self.stackStore.pop(-1))
        return self.stackCache[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length == 0 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()