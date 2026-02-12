class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        cur_max = nums[0]
        cur_min = nums[0]
        for i in range(1, n):
            cur_max, cur_min = max(cur_max * nums[i], nums[i], cur_min * nums[i]), min(cur_max * nums[i], nums[i], cur_min * nums[i])
            res = max(res, cur_max)
        
        return res