from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = Counter(nums)
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num, i in cnt.items():
            bucket[i].append(num)
        
        for c in range(len(nums), 0, -1):
            if bucket[c]:
                for num in bucket[c]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res