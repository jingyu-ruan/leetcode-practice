class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        
        for num in num_set:
            cur_len = 0
            if num - 1 not in num_set:
                cur_len += 1
                k = num + 1
                while k in num_set:
                    cur_len += 1
                    k += 1
                res = max(res, cur_len)

        return res    