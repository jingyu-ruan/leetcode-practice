class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            for c in coins:
                if i > c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1