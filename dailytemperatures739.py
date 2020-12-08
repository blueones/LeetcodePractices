class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for i in range(len(T))]
        stack = []
        for index,temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                popped = stack.pop()
                result[popped] = index - popped
            stack.append(index)
        return result