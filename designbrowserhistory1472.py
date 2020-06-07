class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = self.head
        self.current = self.head
        

    def visit(self, url: str) -> None:
        new_visit = Node(url)
        old_next = self.current.next
        if old_next:
            old_next.before = None
        self.current.next = new_visit
        new_visit.before = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        old_current = self.current
        while steps>0 and self.current!= None:
            old_current = self.current
            self.current = self.current.before
            steps -= 1
        if self.current:
            return self.current.val
        self.current = old_current
        return old_current.val

    def forward(self, steps: int) -> str:
        old_current = self.current
        while steps>0 and self.current!= None:
            old_current = self.current
            self.current = self.current.next
            steps -= 1
        if self.current:
            return self.current.val
        self.current = old_current
        return old_current.val

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.before = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)