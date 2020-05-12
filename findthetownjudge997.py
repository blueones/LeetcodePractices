class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #first attempt O(N)
        if N == 1:
            return 1
        normal = set()
        potential = dict()
        for pair in trust:
            normal.add(pair[0])
            if pair[0] in potential:
                potential.pop(pair[0])
                
            if pair[1] in normal:
                continue
            else:
            
                if pair[1] in potential:
                    potential[pair[1]].append(pair[0])
                else:
                    potential[pair[1]] = [pair[0]]
        for candidate in potential:
            people = potential[candidate]
            if len(people) == N-1:
                return candidate
        return -1
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = [0 for i in range(N+1)]
        for verge in trust:
            in_degree[verge[0]] -= 1
            in_degree[verge[1]] += 1
        for index in range(1, N+1):
            
            if in_degree[index] == N-1:
                return index
        return -1