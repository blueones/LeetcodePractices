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
        
        

        

    def peek(self) -> int:
        """
        Get the front element.
        """
        tempStack = []
        while self.stack:
            tempStack.append(self.stack.pop(-1))
        queueFront = tempStack.pop(-1)
        tempStack.append(queueFront)
        while tempStack:
            self.stack.append(tempStack.pop(-1))
        return queueFront
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.length == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()