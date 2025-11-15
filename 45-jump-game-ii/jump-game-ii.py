class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [float('inf')] * m
        dp[0] = 0

        for i in range(1, m):
            for j in range(0, i):
                if i - j <= nums[j]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]