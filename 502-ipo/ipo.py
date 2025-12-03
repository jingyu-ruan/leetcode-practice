import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # invested = set()
        n = len(capital)
        cur = 0
        # doable = set()
        # cur_max = 0
        comb = []
        heap = []
        for i in range(n):
            comb.append((-profits[i], capital[i]))
        comb.sort(key = lambda x: x[1])

        for i in range(k):
            while cur < n and comb[cur][1] <= w:
                heapq.heappush(heap, comb[cur])
                cur += 1

            if not heap:
                break

            p, c = heapq.heappop(heap)
            p = -p
            w += p
        
        return w
            
            

