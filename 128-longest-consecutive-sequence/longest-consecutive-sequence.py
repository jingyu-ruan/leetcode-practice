class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        length = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                streak = 1
                cur = i
                while cur + 1 in nums_set:
                    streak += 1
                    cur += 1
                
                length = max(length, streak)

        return length