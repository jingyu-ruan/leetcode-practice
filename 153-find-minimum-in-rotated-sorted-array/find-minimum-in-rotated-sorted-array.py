class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if m - 1 >= 0 and m + 1 < len(nums) and nums[m - 1] > nums[m] and nums[m + 1] > nums[m]:
                return nums[m]

            if nums[l] <= nums[m]: # 左侧单调递增
                if nums[l] <= nums[r]:
                    return nums[l]
                else:
                    l = m + 1
            else: # 右侧单调递增
                r = m - 1
