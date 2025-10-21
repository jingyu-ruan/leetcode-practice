from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # 跳过重复的起点，但保留第一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的 left 和 right，移动到新值
                    lv, rv = nums[left], nums[right]
                    while left < right and nums[left] == lv:
                        left += 1
                    while left < right and nums[right] == rv:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res
