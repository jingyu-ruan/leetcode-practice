class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp_len = [1] * n
        # dp_max = [float('-inf')] * n
        # dp_max[0] = nums[0]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_len[i] = max(dp_len[i], dp_len[j] + 1)

        return max(dp_len)