from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        res = []
        for j in range(k):
            max_key = max(freq, key = freq.get)
            res.append(max_key)
            freq[max_key] = -1

        return res
