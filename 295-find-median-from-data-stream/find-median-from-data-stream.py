import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        while len(self.small) - len(self.large) >= 2:
            k = - heapq.heappop(self.small)
            heapq.heappush(self.large, k)
        
        while self.small and self.large and -self.small[0] > self.large[0]:
            s = -heapq.heappop(self.small)
            l = heapq.heappop(self.large)
            heapq.heappush(self.small, -l)
            heapq.heappush(self.large, s)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()