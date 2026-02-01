class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = n - 1
        while r > 0 and nums[r-1] >= nums[r]:
            r -= 1
        
        if r == 0:
            nums.reverse()
            return
        
        j = n - 1
        while j >= r and nums[j] <= nums[r-1]:
            j -= 1
        
        nums[r-1], nums[j] = nums[j], nums[r-1]
        left = r          
        right = n - 1     
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        