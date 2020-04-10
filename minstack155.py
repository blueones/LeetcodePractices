class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        current_min = self.getMin()
        
        if self.stack and x>=current_min:
            self.stack.append((x,current_min))
        else:
            self.stack.append((x,x))
        
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()