class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
        for _ in range(cnt):
            nums.append(0)