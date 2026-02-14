class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for x in nums:
            if x != 0:
                nums[cur] = x
                cur += 1
        
        for i in range(cur, len(nums)):
            nums[i] = 0