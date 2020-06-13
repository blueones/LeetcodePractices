class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def find_subarray(index):
            total = 0
            for i in range(index, len(arr)):
                total += arr[i]
                if total == target:
                    return i-index+1
            return -1
        shortest_target_subarray = list()
        for index in range(len(arr)):
            shortest = find_subarray(index)
            shortest_target_subarray.append(shortest)
        shortest = float("inf")
        for index,length in enumerate(shortest_target_subarray):
            if length != -1:
                for search in range(index+length, len(shortest_target_subarray)):
                    if shortest_target_subarray[search]!= -1:
                        current_length = length + shortest_target_subarray[search]
                        shortest = min(current_length, shortest)
        if shortest == float("inf"):
            return -1
        return shortest
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def find_subarray(index):
            total = 0
            for i in range(index, len(arr)):
                total += arr[i]
                if total == target:
                    return i-index+1
            return -1
        shortest_target_subarray = list()
        for index in range(len(arr)):
            shortest = find_subarray(index)
            shortest_target_subarray.append(shortest)
        shortest = float("inf")
        
        shortest_target_subarray[-1] = (shortest_target_subarray[-1], -1) if shortest_target_subarray[-1] == -1 else (shortest_target_subarray[-1], shortest_target_subarray[-1])
        current_smallest_length = shortest_target_subarray[-1][1] 
        
        for index in range(len(shortest_target_subarray)-2, -1, -1):
            current_len = shortest_target_subarray[index]
            if current_len != -1:
                
                if current_smallest_length != -1:
                    current_smallest_length = min(current_smallest_length, current_len)
                else:
                    current_smallest_length = current_len
                shortest_target_subarray[index]= (current_len, current_smallest_length)
                 # shortest_target_subarray[index+current_len][1]
            else:
                shortest_target_subarray[index]= (current_len, current_smallest_length)   
        print(shortest_target_subarray)
        for index in range(len(shortest_target_subarray)):
            length = shortest_target_subarray[index][0]
            if length != -1:
                if index+length < len(shortest_target_subarray) and shortest_target_subarray[index+length][1]!= -1:
                    current_total_length = shortest_target_subarray[index][0] + shortest_target_subarray[index+length][1]
                    shortest = min(shortest, current_total_length)
        if shortest == float("inf"):
            return -1
        return shortest