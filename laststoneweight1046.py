class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def helper(list_stones):
            #output a new list of stones
            
            list_stones[-1],list_stones[-2]= 0, abs(list_stones[-1]-list_stones[-2])
            list_stones.sort()
            return list_stones
        stones.sort()
        while len(stones)>1 and stones[-2]!= 0:
            stones = helper(stones)
        return stones[-1]