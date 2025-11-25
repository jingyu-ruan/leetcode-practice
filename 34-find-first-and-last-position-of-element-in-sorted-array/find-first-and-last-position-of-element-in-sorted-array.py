class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        start, end = -1, -1
        while l <= r: # 确定左界
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else: # nums[m] == target
                if m == 0 or nums[m-1] != target:
                    start = m
                    break
                else:
                    r = m - 1

        l, r = 0, len(nums) - 1
        while l <= r: # 确定右界
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else: # nums[m] == target
                if m == len(nums) - 1 or nums[m+1] != target:
                    end = m
                    break
                else:
                    l = m + 1

        return [start, end]