class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #transaction multiple times
        #simple one pass
        boughtPrice = float("inf")
        profit = 0
        for price in prices:
            if price < boughtPrice:
                boughtPrice = price
            elif price >= boughtPrice:
                profit += price - boughtPrice
                boughtPrice = price
        return profit