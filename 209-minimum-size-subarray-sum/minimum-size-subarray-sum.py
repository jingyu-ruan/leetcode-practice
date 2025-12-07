class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        # n = len(nums)
        # cur_len = 0
        cur_sum = 0
        res = float('inf')
        for i, v in enumerate(nums):
            cur_sum += v
            # cur_len += 1
            while cur_sum >= target:
                cur_sum -= nums[l]
                l += 1
                # cur_len -= 1
                res = min(res, i - l + 2)
        
        return res if res != float('inf') else 0