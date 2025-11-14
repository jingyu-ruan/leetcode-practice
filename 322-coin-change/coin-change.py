class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        coin_set = set(coins)

        for i in range(1, amount + 1):
            if i in coin_set:
                dp[i] = 1
            else:

                for c in coins:
                    if i > c and dp[i-c] != -1:
                        dp[i] = min(dp[i], dp[i-c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1