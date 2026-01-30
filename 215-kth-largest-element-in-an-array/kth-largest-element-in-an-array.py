import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-i for i in nums]
        heapq.heapify(neg)
        for _ in range(k - 1):
            heapq.heappop(neg)
        return - neg[0]