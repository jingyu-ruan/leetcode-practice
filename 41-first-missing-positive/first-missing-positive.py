class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        bucket = set()
        for i, v in enumerate(nums):
            if v > 0:
                bucket.add(v)
        
        res = 1
        while True:
            if res not in bucket:
                return res
            res += 1