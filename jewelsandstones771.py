class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_set = set()
        #record all kinds of jewels
        for stone in J:
            jewel_set.add(stone)
        #traverse S and record all the jewels in S
        ans = 0
        for stone in S:
            if stone in jewel_set:
                ans += 1
        return ans
class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        set_J = set(J)
        return sum([s in set_J for s in S])
class Solution1:
    def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))
class Solution3:
    def numJewelsInStones(self, J, S):
        return sum(map(S.count, J))