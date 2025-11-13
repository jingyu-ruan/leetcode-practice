class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[-1][i] = n - i
        for j in range(m + 1):
            dp[j][-1] = m - j

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r+1][c+1], dp[r+1][c], dp[r][c+1])

        
        return dp[0][0]