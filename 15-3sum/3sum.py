class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return None
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    val_l = nums[l]
                    val_r = nums[r]
                    l += 1
                    r -= 1
                    while l < r and nums[l] == val_l:
                        l += 1
                    while l < r and nums[r] == val_r:
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
