class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            res = max(res, cur)
        return res