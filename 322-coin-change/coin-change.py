class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        inf = amount + 1
        dp = [0] + amount * [inf]
        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != inf else -1