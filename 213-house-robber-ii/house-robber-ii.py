class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        # pick first
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n - 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i], dp[i-3] + nums[i])

        dp2 = [0] * n
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i], dp2[i-3] + nums[i])
        
        return max(max(dp), max(dp2))
        