class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        left = [0] * n
        right = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            left[i] = max(left[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i+1], max_price - prices[i])
            max_price = max(max_price, prices[i])
        
        res = 0
        for i in range(n):
            res = max(res, left[i] + right[i])
        
        return res