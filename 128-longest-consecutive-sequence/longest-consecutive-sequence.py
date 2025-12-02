class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in num_set:
            if i - 1 not in num_set:
                cur = 1
                k = i + 1
                while k in num_set:
                    cur += 1
                    k += 1
                res = max(res, cur)

        return res