class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_num = prices[0]

        for i in range(1, len(prices)):
            dp[i] = prices[i] - min_num
            min_num = min(min_num, prices[i])

        return max(dp)