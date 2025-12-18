class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums
        max_val = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i-1] + dp[i])
            max_val = max(max_val, dp[i])
        
        return max_val
