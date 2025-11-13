class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for x in nums[1:]:
            #if x < 0:
            #    cur_max, cur_min = cur_min, cur_max

            cur_max, cur_min = max(x, cur_max * x, cur_min * x), min(x, cur_min * x, cur_max * x)

            res = max(res, cur_max)
        
        return res