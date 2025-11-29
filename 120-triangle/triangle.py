class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = []
        for i in range(n):
            dp.append([float('inf')] * (i + 1))

        dp[0][0] = triangle[0][0]
        for j in range(1, n):
            dp[j][0] = dp[j-1][0] + triangle[j][0]
            dp[j][-1] = dp[j-1][-1] + triangle[j][-1]
        
        for j in range(1, n):
            for k in range(1, j):
                dp[j][k] = triangle[j][k] + min(dp[j-1][k-1], dp[j-1][k])

        return min(dp[-1])