class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]



        return dp[-1][-1]