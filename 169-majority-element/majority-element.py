from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        reach = n // 2 + 1
        for i in nums:
            dic[i] += 1
            if dic[i] == reach:
                return i