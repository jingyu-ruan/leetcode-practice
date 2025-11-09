class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_set = set(nums)
        l, r = 0, len(nums) - 1
        if target in nums_set:
            # l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        else:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target and nums[m+1] > target:
                    return m + 1
                elif nums[m] < target and nums[m+1] < target:
                    l = m + 1
                elif nums[m] > target and nums[m+1] > target:
                    r = m - 1                    