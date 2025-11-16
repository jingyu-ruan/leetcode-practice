class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matc = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in matc:
                return [matc[need], i]
            matc[num] = i