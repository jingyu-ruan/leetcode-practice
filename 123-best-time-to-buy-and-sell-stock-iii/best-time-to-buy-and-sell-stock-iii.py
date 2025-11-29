class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        
        # 1. 从左往右：计算截止到第 i 天，做一笔交易的最大利润
        left_profits = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            # 更新最低买入价
            min_price = min(min_price, prices[i])
            # 今天的最大利润 = max(昨天的最大利润, 今天卖出的利润)
            left_profits[i] = max(left_profits[i-1], prices[i] - min_price)
            
        # 2. 从右往左：计算从第 i 天开始，做一笔交易的最大利润
        right_profits = [0] * n
        max_price = prices[-1]
        for i in range(n-2, -1, -1):
            # 更新最高卖出价
            max_price = max(max_price, prices[i])
            # 这里的最大利润 = max(明天的最大利润, 今天买入的利润)
            right_profits[i] = max(right_profits[i+1], max_price - prices[i])
            
        # 3. 找最佳切分点
        max_total_profit = 0
        for i in range(n):
            # 左边的利润 + 右边的利润
            max_total_profit = max(max_total_profit, left_profits[i] + right_profits[i])
            
        return max_total_profit