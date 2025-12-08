class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
            else:
                l += 1
