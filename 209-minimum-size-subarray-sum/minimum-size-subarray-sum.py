class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)
        l = 0
        total = 0
        for r in range(n):
            total += nums[r]
            while l <= r and total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0