class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1, 2, 3
        #    t  i
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        t = i - 1
        j = n - 1
        while j > t and nums[j] <= nums[t]:
            j -= 1
        nums[t], nums[j] = nums[j], nums[t]
        l, r = t + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1