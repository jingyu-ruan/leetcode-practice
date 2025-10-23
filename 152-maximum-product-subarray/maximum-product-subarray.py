class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        cur_num = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            cur_num = nums[i]
            temp_max = cur_max
            temp_min = cur_min
            cur_max = max(cur_num, temp_max * cur_num, temp_min * cur_num)
            cur_min = min(cur_num, temp_max * cur_num, temp_min * cur_num)
            res = max(res, cur_max)

        
        return res