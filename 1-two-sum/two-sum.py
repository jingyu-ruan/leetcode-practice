class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        sum_index = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in sum_index:
                return [sum_index[need], i]
            sum_index[nums[i]] = i