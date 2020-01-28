class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lenS = len(prices)
        if lenS == 0:
            return 0
        minPrice = float("inf")
        profit = 0
        for i in range(lenS):
            if prices[i]< minPrice:
                minPrice = prices[i]
            elif prices[i] > minPrice:
                profit = max (profit, prices[i]-minPrice)
        return profit