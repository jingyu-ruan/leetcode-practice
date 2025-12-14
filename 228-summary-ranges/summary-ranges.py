# from collections import deque
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # nums = deque(nums)
        nums.append(float('-inf'))
        res = []
        l = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1:
                continue
            else:
                if i - l > 1:
                    res.append(f'{nums[l]}->{nums[i - 1]}')
                else:
                    res.append(f'{nums[l]}')
                l = i
        
        return res
