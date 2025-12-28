class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            # 情况1: 中间值大于右边值，说明最小值肯定在右半边（类似悬崖跌落）
            # 例如 [3, 4, 5, 1, 2] 中的 5 > 2
            if nums[m] > nums[r]:
                l = m + 1
                
            # 情况2: 中间值小于右边值，说明 m 到 r 是递增的，最小值在 m 或 m 左边
            # 例如 [5, 1, 2, 3, 4] 中的 2 < 4
            elif nums[m] < nums[r]:
                r = m
                
            # 情况3: 中间值等于右边值，无法判断，只能保守缩减 r
            # 解决 [1, 0, 1, 1, 1] 的关键
            else:
                r -= 1
                
        return nums[l]