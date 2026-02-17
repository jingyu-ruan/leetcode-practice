class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        gap = float('inf')
        for i in range(0, n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if abs(total - target) < gap:
                    gap = abs(total - target)
                    res = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        
        return res