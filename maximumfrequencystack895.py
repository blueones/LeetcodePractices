#compare this question with LFU cache. because LFU cache needs to move element from frequency data structure, so we have to use linked list to achieve flexibility when inserting and removing.
#but since this is stack, so elements exist in all frequencies. 
class FreqStack:

    def __init__(self):
        self.dict_frequency = dict()
        self.max_frequency = 0
        self.dict_num = dict()

    def push(self, x: int) -> None:
        if x in self.dict_num:
            frequency_x = self.dict_num[x]
            if frequency_x+1 in self.dict_frequency:
                self.dict_frequency[frequency_x+1].append(x)
                
            else:
                self.dict_frequency[frequency_x+1] = deque()
                self.dict_frequency[frequency_x+1].append(x)
            self.dict_num[x] = frequency_x+1
            self.max_frequency = max(self.max_frequency, frequency_x+1)
        else:
            self.dict_num[x] = 1
            if 1 in self.dict_frequency:
                self.dict_frequency[1].append(x)
            else:
                self.dict_frequency[1] = deque()
                self.dict_frequency[1].append(x)
            self.dict_num[x] = 1
            self.max_frequency = max(self.max_frequency, 1)

    def pop(self) -> int:
        if self.max_frequency:
            stack = self.dict_frequency[self.max_frequency]
            ans = stack.pop()
            self.dict_num[ans] -= 1
            if not stack:
                self.max_frequency -= 1
            return ans
                