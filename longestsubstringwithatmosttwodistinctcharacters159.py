class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        visited = {}
        max_length = 0
        queue = deque()
        for cha in s:
            if len(visited) == 2 and cha not in visited:
                while len(visited) == 2:
                    popped = queue.popleft()
                    visited[popped] -= 1
                    if visited[popped] == 0:
                        visited.pop(popped)
                
            
            queue.append(cha)
            if cha in visited:
                visited[cha] += 1
            else:
                visited[cha] = 1
            max_length = max(max_length, len(queue))
        return max_length
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        covered = defaultdict()
        left = right = 0
        max_length = 0
        while right < len(s):
            
            if s[right] not in covered and len(covered) == 2:
                covered_list = sorted(covered, key = lambda i:covered[i])
                topop = covered_list[0]
                left = covered[topop]+1
                covered.pop(topop)
            covered[s[right]] = right
            max_length = max(max_length, right-left+1)
            right += 1
        return max_length