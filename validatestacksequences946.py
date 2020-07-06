class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed_deque = deque()
        
        index_pop = 0
        index_push = 0
        while index_push < len(pushed) or index_pop < len(popped):
            if len(pushed_deque)!= 0 and pushed_deque[-1] == popped[index_pop]:
                pushed_deque.pop()
                index_pop += 1
            elif index_push < len(pushed):
                pushed_deque.append(pushed[index_push])
                index_push+= 1
            else:
                return False
        return True
                