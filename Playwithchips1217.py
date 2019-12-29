class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        singleN=0
        doubleN=0
        for i in chips:
            if i%2==1:
                singleN+=1
            else: doubleN+=1
        return max(singleN,doubleN)