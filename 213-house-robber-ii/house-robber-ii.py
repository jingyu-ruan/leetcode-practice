class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])  
        for i in range(2, len(nums) - 1):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        dp2 = [0] * (len(nums))
        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, len(nums)):
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

        return max(dp[len(nums) - 2], dp2[len(nums) - 1])
      