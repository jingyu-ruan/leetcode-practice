import heapq
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        heapq.heapify(nums)
        while nums:
            num = heapq.heappop(nums)
            if num > 0 and res == num:
                res += 1

        return res