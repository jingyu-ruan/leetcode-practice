class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i, v in enumerate(nums):
            if v in cache:
                return [cache[v], i]
            cache[target - v] = i