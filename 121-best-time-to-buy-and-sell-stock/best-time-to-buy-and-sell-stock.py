class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return res