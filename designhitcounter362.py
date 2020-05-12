from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = 0
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
            self.counter += 1
        else:
            self.queue.append([timestamp, 1])
            while self.queue and self.queue[0][0] <= timestamp - 300:
                popped = self.queue.popleft()
                self.counter -= popped[1]
            self.counter += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and self.queue[0][0] <= timestamp - 300:
            popped = self.queue.popleft()
            self.counter -= popped[1]
        return self.counter
        
