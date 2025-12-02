import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        heap = []
        for i, f in freq.items():
            heapq.heappush(heap, (f, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for f, i in heap:
            res.append(i)
        
        return res