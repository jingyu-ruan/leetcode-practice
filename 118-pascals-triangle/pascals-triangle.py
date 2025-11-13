class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            dp = [1] * (i+1)
            if i >= 2:
                for j in range(1, i):
                    dp[j] = res[-1][j-1] + res[-1][j]
            res.append(dp)

        return res