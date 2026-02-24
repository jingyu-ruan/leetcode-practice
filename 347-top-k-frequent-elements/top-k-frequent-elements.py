from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        lst = [(a, b) for a, b in freq.items()]
        lst.sort(key=lambda x: x[1], reverse=True)
        res = []
        j = 0
        for i in range(k):
            res.append(lst[j][0])
            j += 1
        return res