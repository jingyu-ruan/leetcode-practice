class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if target > nums[n - 1]:
            return n
        if target < nums[0]:
            return 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                if m - 1 >= 0 and nums[m-1] < target:
                    return m
                r = m - 1
            else:
                return m

        