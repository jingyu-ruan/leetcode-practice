class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # cur_pos = 0
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums) - 1):
            if not dp[i]:
                continue
            
            cur_val = nums[i]

            for j in range(i + 1, min(cur_val + i + 1, len(nums))):
                dp[j] = True
            
            if dp[-1]:
                return True

        return dp[-1]