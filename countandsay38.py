class Solution:
    def countAndSay(self, n: int) -> str:
        def countSay(current):
            len_current = len(current)
            index = 0
            starting = ""
            while index < len_current:
                count = 1
                digit = current[index]
                while index+1 < len_current and current[index] == current[index+1]:
                    index += 1
                    count += 1
                starting += str(count)
                starting += current[index]
                index += 1
            return starting
        times = 1
        current = "1"
        while times< n:
            current = countSay(current)
            times += 1
        return current