import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-i for i in nums]
        heapq.heapify(neg)
        for i in range(k):
            res = heapq.heappop(neg)
            if i == k - 1:
                return -res