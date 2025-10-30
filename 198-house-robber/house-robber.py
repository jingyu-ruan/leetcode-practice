class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        # res = 0

        for i in range(2, len(nums)):
            for j in range(0, i - 1):
                dp[i] = max(dp[j] + nums[i], nums[i], dp[i])
                # res = max(res, dp[i])

        return max(dp)