class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i]
                nums[i], nums[target - 1] = nums[target - 1], nums[i]
        
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        
        return n + 1