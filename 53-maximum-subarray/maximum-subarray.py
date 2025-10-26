class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        
        l = 0
        r = 1
        max_sum = 0
        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)

