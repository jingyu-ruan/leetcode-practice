class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # 如果 k 足够大，退化为 122（无限次交易）
        if k >= n // 2:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i] - prices[i-1])
            return res

        # k 不大，使用 DP
        buy = [-10**15] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j-1] - price)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]
