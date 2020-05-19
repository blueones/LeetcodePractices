class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days_now = 1
        if self.stack == []:
            self.stack.append([price, 1])
            
        else:
            
            if self.stack[-1][0] <= price:
                
                while self.stack and self.stack[-1][0] <= price:
                    
                    past_price, days = self.stack.pop()
                    days_now += days
            
            self.stack.append([price, days_now])
        return days_now


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)