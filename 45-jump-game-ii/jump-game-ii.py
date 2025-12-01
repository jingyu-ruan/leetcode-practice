class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [float('inf')] * n
        dp[0] = 0
        reach = nums[0]

        for i in range(n):
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                dp[j] = min(dp[j], 1 + dp[i])

        return dp[-1]