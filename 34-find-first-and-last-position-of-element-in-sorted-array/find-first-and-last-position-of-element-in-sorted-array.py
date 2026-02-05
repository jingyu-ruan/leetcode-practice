class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def search(left):
            l, r = 0, n - 1
            idx = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    idx = m
                    if left:
                        r = m - 1
                    else:
                        l = m + 1
            return idx

        return [search(True), search(False)]
            