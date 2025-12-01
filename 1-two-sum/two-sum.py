class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        need = dict()
        idx = dict()
        for i in range(n):
            if nums[i] in need:
                return [idx[target - nums[i]], i]
            need[target - nums[i]] = nums[i]
            idx[nums[i]] = i
            

